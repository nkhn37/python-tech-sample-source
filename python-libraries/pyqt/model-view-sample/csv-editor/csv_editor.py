import csv
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class CsvTableModel(qtc.QAbstractTableModel):
    """CSVデータ用テーブルモデル"""

    # エラーシグナル
    error = qtc.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.filepath = None
        self._header = None
        self._data = None

    def csv_open(self, filepath):
        """CSVファイルを読み込みデータをセットする

        Args:
            filepath: CSVファイルパス
        """
        if filepath:
            self.filepath = filepath
            error = ""
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    csv_reader = csv.reader(f)
                    self._header = next(csv_reader)
                    self._data = list(csv_reader)
            except Exception as ex:
                error = f"ファイルを開けませんでした。: {ex}"

            if error:
                self.error.emit(error)
                return False

            return True

    def csv_save(self, filename=None):
        """CSVファイルを保存する"""
        if filename:
            target_file = filename
        else:
            target_file = self.filepath

        if target_file:
            error = ""
            try:
                with open(target_file, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(self._header)
                    writer.writerows(self._data)
            except Exception as ex:
                error = f"ファイルを開けませんでした。: {ex}"

            if error:
                self.error.emit(error)
                return False

            # 保存に成功したら現在のファイルパスを更新
            self.filepath = target_file
            return True

    # ===== QAbstractTableModelを使う際に最低限必要なメソッド
    # rowCount, column, data
    def rowCount(self, parent):
        """テーブルの行数を返却する"""
        return len(self._data)

    def columnCount(self, parent):
        """テーブルの列数を返却する"""
        return len(self._header)

    def data(self, index, role):
        """index, roleで指定されるセルのデータを返却する"""
        if role in (
            qtc.Qt.ItemDataRole.DisplayRole,
            qtc.Qt.ItemDataRole.EditRole,
        ):
            return self._data[index.row()][index.column()]

    # ===== データのソート関連メソッド
    # headerData, sort
    def headerData(self, section, orientation, role):
        """ヘッダーデータを返却する"""
        if (
            orientation == qtc.Qt.Orientation.Horizontal
            and role == qtc.Qt.ItemDataRole.DisplayRole
        ):
            return self._header[section]
        else:
            return super().headerData(section, orientation, role)

    def sort(self, column, order):
        # ソートを実行する前に必要
        self.layoutAboutToBeChanged.emit()
        # データをソートする
        self._data.sort(key=lambda x: x[column])
        if order == qtc.Qt.SortOrder.DescendingOrder:
            self._data.reverse()
        # ソート後に必要
        self.layoutChanged.emit()

    # ===== 書き込み対応のためのメソッド
    # flags, setData
    def flags(self, index):
        """フラグの設定"""
        return super().flags(index) | qtc.Qt.ItemFlag.ItemIsEditable

    def setData(self, index, value, role):
        """データを設定する"""
        if index.isValid() and role == qtc.Qt.ItemDataRole.EditRole:
            # valueをindexに該当するセルに設定する
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        else:
            return False

    # ===== 行追加／行削除用メソッド
    # insertRows, removeRows
    def insertRows(self, row, count, parent):
        """行追加"""
        self.beginInsertRows(parent or qtc.QModelIndex(), row, row + count - 1)
        new_row = [""] * len(self._header)
        for _ in range(count):
            self._data.insert(row, new_row)
        self.endInsertRows()

    def removeRows(self, row, count, parent):
        """行削除"""
        self.beginRemoveRows(parent or qtc.QModelIndex(), row, row + count - 1)
        for _ in range(count):
            del self._data[row]
        self.endRemoveRows()

    # ===== 列追加／列削除用メソッド
    # insertColumns, removeColumns
    def insertColumns(self, column, count, parent, col_name=""):
        """列追加"""

        if col_name:
            self.beginInsertColumns(
                parent or qtc.QModelIndex(), column, column + count - 1
            )
            new_column = [""] * count
            new_header = [col_name] * count
            self._header[column : column + count - 1] = new_header
            for i, _ in enumerate(self._data):
                self._data[i][column : column + count - 1] = new_column
            self.endInsertColumns()

    def removeColumns(self, column, count, parent):
        """列削除"""
        self.beginRemoveColumns(parent or qtc.QModelIndex(), column, column + count - 1)
        del self._header[column : column + count]
        for i, _ in enumerate(self._data):
            del self._data[i][column : column + count]
        self.endRemoveColumns()


class View(qtw.QWidget):
    """MainView"""

    def __init__(self):
        """Viewコンストラクタ"""
        super().__init__()

        # ===== 画面要素の定義
        # テーブルビューの生成
        self.table_view = qtw.QTableView()
        # ソート可否の設定
        self.table_view.setSortingEnabled(True)

        layout = qtw.QVBoxLayout()
        self.label = qtw.QLabel("", self)
        layout.addWidget(self.label)
        layout.addWidget(self.table_view)
        self.setLayout(layout)

    def show_error_message(self, error):
        """エラーダイアログ表示"""
        qtw.QMessageBox.critical(None, "エラー", error)

    def show_col_input_dialog(self):
        """列名指定ダイアログ"""
        col_name, input_ok = qtw.QInputDialog.getText(self, "列名指定", "新規列名を入力してください。")

        if input_ok:
            return col_name
        else:
            return ""


class MainWindow(qtw.QMainWindow):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        # 画面タイトルの設定
        self.setWindowTitle("CSVエディタ")
        # 画面サイズの設定
        self.resize(640, 360)

        # モデルを生成
        self.model = None
        # Viewを生成
        self.view = View()
        # CentralWidgetへ設定
        self.setCentralWidget(self.view)

        # [ファイル]メニュー
        self.file_menu = self.menuBar().addMenu("ファイル(&F)")
        # [編集]メニュー
        self.edit_menu = self.menuBar().addMenu("編集(&E)")

        # ===== [ファイル]メニューのアクションの追加
        # [ファイルを開く...] アクション
        self.open_action = qtg.QAction(
            "ファイルを開く...",
            self,
            triggered=self.select_file,
            shortcut=qtg.QKeySequence("Ctrl+O"),
        )
        self.file_menu.addAction(self.open_action)

        # [保存] アクション
        self.save_action = qtg.QAction(
            "保存",
            self,
            triggered=self.save_file,
            shortcut=qtg.QKeySequence("Ctrl+S"),
            enabled=False,
        )
        self.file_menu.addAction(self.save_action)

        # [名前を付けて保存...] アクション
        self.save_as_action = qtg.QAction(
            "名前を付けて保存",
            self,
            triggered=self.save_file_as,
            shortcut=qtg.QKeySequence("Ctrl+Shift+S"),
            enabled=False,
        )
        self.file_menu.addAction(self.save_as_action)

        # [終了] アクション
        self.quit_action = self.file_menu.addAction("終了", self.close)

        # ===== [編集]メニューのアクション追加
        # [上に行を追加する] アクション
        self.insert_above_action = qtg.QAction(
            "上に行を追加する",
            self,
            triggered=self.insert_above,
            enabled=False,
        )
        self.edit_menu.addAction(self.insert_above_action)

        # [下に行を追加する] アクション
        self.insert_below_action = qtg.QAction(
            "下に行を追加する",
            self,
            triggered=self.insert_below,
            enabled=False,
        )
        self.edit_menu.addAction(self.insert_below_action)

        # [行を削除する] アクション
        self.remove_rows_action = qtg.QAction(
            "行を削除する",
            self,
            triggered=self.remove_rows,
            enabled=False,
        )
        self.edit_menu.addAction(self.remove_rows_action)

        # [左に列を追加する] アクション
        self.insert_left_action = qtg.QAction(
            "左に列を追加する",
            self,
            triggered=self.insert_left,
            enabled=False,
        )
        self.edit_menu.addAction(self.insert_left_action)

        # [右に列を追加する] アクション
        self.insert_right_action = qtg.QAction(
            "右に列を追加する",
            self,
            triggered=self.insert_right,
            enabled=False,
        )
        self.edit_menu.addAction(self.insert_right_action)

        # [列を削除する] アクション
        self.remove_columns_action = qtg.QAction(
            "列を削除する",
            self,
            triggered=self.remove_columns,
            enabled=False,
        )
        self.edit_menu.addAction(self.remove_columns_action)

        # 画面表示
        self.show()

    def select_file(self):
        """対象ファイルを選択する"""
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "ファイルを開く",
            qtc.QDir.currentPath(),
            "CSVファイル (*.csv);;すべてのファイル (*)",
            "CSVファイル (*.csv)",
            options=qtw.QFileDialog.Option.DontUseNativeDialog
            | qtw.QFileDialog.Option.DontResolveSymlinks,
        )
        # ファイル読み込み
        if filename:
            if not self.model:
                # モデルが生成されていない場合に生成
                self.model = CsvTableModel()
                self.model.error.connect(self.view.show_error_message)

            # ファイルをオープンして、モデルをセットする
            if self.model.csv_open(filename):
                self.view.table_view.setModel(self.model)
                # アクションの有効化
                self.save_action.setEnabled(True)
                self.save_as_action.setEnabled(True)
                self.insert_above_action.setEnabled(True)
                self.insert_below_action.setEnabled(True)
                self.remove_rows_action.setEnabled(True)
                self.insert_left_action.setEnabled(True)
                self.insert_right_action.setEnabled(True)
                self.remove_columns_action.setEnabled(True)
                # ファイルパス更新
                self.view.label.setText(f"{filename}")

    def save_file_as(self):
        """名前を付けて保存する"""
        # ファイルダイアログを表示
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self,
            "ファイルを保存する",
            qtc.QDir.currentPath(),
            "CSVファイル (*.csv);;すべてのファイル (*)",
            "CSVファイル (*.csv)",
            qtw.QFileDialog.Option.DontUseNativeDialog
            | qtw.QFileDialog.Option.DontResolveSymlinks,
        )
        # ファイル書き込み
        if filename and self.model:
            if self.model.csv_save(filename):
                # ファイルパス更新
                self.view.label.setText(f"{filename}")

    def save_file(self):
        """上書き保存する"""
        if self.model:
            self.model.csv_save()

    def insert_above(self):
        """選択行の上に行を追加する"""
        selected = self.view.table_view.selectedIndexes()
        row = selected[0].row() if selected else 0
        self.model.insertRows(row, 1, None)

    def insert_below(self):
        """選択行の下に行を追加する"""
        selected = self.view.table_view.selectedIndexes()
        row = selected[-1].row() if selected else self.model.rowCount(None)
        self.model.insertRows(row + 1, 1, None)

    def remove_rows(self):
        """選択行を削除する"""
        selected = self.view.table_view.selectedIndexes()
        num_rows = len(set(i.row() for i in selected))
        if selected:
            self.model.removeRows(selected[0].row(), num_rows, None)

    def insert_left(self):
        """選択列の左に列を追加する"""
        col_name = self.view.show_col_input_dialog()
        if col_name:
            selected = self.view.table_view.selectedIndexes()
            column = selected[0].column() if selected else 0
            self.model.insertColumns(column, 1, None, col_name)

    def insert_right(self):
        """選択列の右に列を追加する"""
        col_name = self.view.show_col_input_dialog()
        if col_name:
            selected = self.view.table_view.selectedIndexes()
            column = selected[-1].column() if selected else self.model.columnCount(None)
            self.model.insertColumns(column + 1, 1, None, col_name)

    def remove_columns(self):
        """選択列を削除する"""
        selected = self.view.table_view.selectedIndexes()
        num_columns = len(set(i.column() for i in selected))
        if selected:
            self.model.removeColumns(selected[0].column(), num_columns, None)


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
