"""QtSqlのQSqlQueryModelの使い方
SQLiteデータベースでの使用例

[説明ページ]
https://tech.nkhn37.net/pyqt-qtsql-qsqlquerymodel/#i
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtSql as qts
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        # 画面タイトルの設定
        self.setWindowTitle("QSqlQueryModel")
        # 画面サイズの設定
        self.resize(640, 360)
        # DB接続
        self.db = None
        # レイアウト
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        # データベース接続
        self.db_connect()
        # 必要テーブルの存在チェック
        required_tables = {"product_info"}
        self.table_check(required_tables)

        # モデル(QSqlQueryModel)の作成
        self.product_info_model = qts.QSqlQueryModel()
        # モデルが取得するクエリを設定
        self.product_info_model.setQuery(
            "SELECT * FROM product_info ORDER BY id"
        )

        # 列名を設定
        column_names = ["ID", "製品コード", "顧客", "価格", "作成日付"]
        self.set_column_names(column_names)

        # ビュー(QTableView)を作成
        self.product_list_view = qtw.QTableView()
        # 作成したモデルを設定
        self.product_list_view.setModel(self.product_info_model)

        # ビューをレイアウトに追加
        self.layout().addWidget(self.product_list_view)

        # 画面表示
        self.show()

    def db_connect(self):
        """DB接続"""
        # データベースへの接続
        self.db = qts.QSqlDatabase.addDatabase("QSQLITE")
        print(f"DBドライバー一覧: {self.db.drivers()}")
        self.db.setDatabaseName("test.db")
        if not self.db.open():
            error = self.db.lastError().text()
            qtw.QMessageBox.critical(
                None,
                "DB接続エラー",
                "データベースファイルを開けませんでした。",
            )
            sys.exit(1)

    def table_check(self, required_tables):
        """テーブルが対象DBに存在するかをチェックする

        Args:
            required_tables: 必要テーブルの集合(set)
        """
        # データベースの情報を取得して対象テーブルの存在をチェック
        tables = self.db.tables()
        print(f"テーブル一覧: {tables}")
        missing_tables = required_tables - set(tables)
        if missing_tables:
            qtw.QMessageBox.critical(
                None,
                "DB存在確認エラー",
                f"必要なデータが存在しません: {missing_tables}",
            )
            sys.exit(1)

    def set_column_names(self, columns):
        """列名設定

        Args:
            columns: 列名リスト
        """
        for i, name in enumerate(columns):
            self.product_info_model.setHeaderData(
                i, qtc.Qt.Orientation.Horizontal, name
            )


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
