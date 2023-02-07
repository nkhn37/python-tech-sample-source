"""QMainWindowを継承した画面開発テンプレートを用いた実装例
簡易テキストエディタ

[説明ページ]
https://tech.nkhn37.net/pyqt-qmainwindow-program-template/#QMainWindow-2
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QMainWindow):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        # 画面タイトルの設定
        self.setWindowTitle("Simple Text Editor")
        # 画面サイズの設定
        self.resize(640, 360)
        # central widgetの設定
        self.text_edit = qtw.QTextEdit()
        self.setCentralWidget(self.text_edit)

        # =============== メニューバー =================
        # ===== メニュー項目の追加
        # [ファイル]メニュー
        file_menu = self.menuBar().addMenu("ファイル(&F)")
        # [編集]メニュー
        edit_menu = self.menuBar().addMenu("編集(&E)")
        # [ヘルプ]メニュー
        help_menu = self.menuBar().addMenu("ヘルプ(&H)")
        # ...他メニューも必要に応じて追加

        # ===== [ファイル]メニューのアクションの追加
        # [ファイルを開く...] アクション
        open_action = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DirOpenIcon),
            "ファイルを開く...",
            self,
            triggered=self.open_file,
            shortcut=qtg.QKeySequence("Ctrl+O"),
        )
        file_menu.addAction(open_action)

        # [保存] アクション
        save_action = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DriveHDIcon),
            "保存",
            self,
            triggered=self.save_file,
            shortcut=qtg.QKeySequence("Ctrl+S"),
        )
        file_menu.addAction(save_action)

        # [終了] アクション
        quit_action = file_menu.addAction("終了", self.close)
        # ...他アクションも必要に応じて追加

        # ===== [編集]メニューのアクション追加
        # [元に戻す] アクション
        undo_action = qtg.QAction(
            "元に戻す",
            self,
            triggered=self.text_edit.undo,
            shortcut=qtg.QKeySequence("Ctrl+Z"),
        )
        edit_menu.addAction(undo_action)

        # [やり直し] アクション
        redo_action = qtg.QAction(
            "やり直し",
            self,
            triggered=self.text_edit.redo,
            shortcut=qtg.QKeySequence("Ctrl+Y"),
        )
        edit_menu.addAction(redo_action)

        # セパレータの追加
        edit_menu.addSeparator()

        # [切り取り] アクション
        cut_action = qtg.QAction(
            "切り取り",
            self,
            triggered=self.text_edit.cut,
            shortcut=qtg.QKeySequence("Ctrl+X"),
        )
        edit_menu.addAction(cut_action)

        # [コピー] アクション
        copy_action = qtg.QAction(
            "コピー",
            self,
            triggered=self.text_edit.copy,
            shortcut=qtg.QKeySequence("Ctrl+C"),
        )
        edit_menu.addAction(copy_action)

        # [貼り付け]
        paste_action = qtg.QAction(
            "貼り付け",
            self,
            triggered=self.text_edit.paste,
            shortcut=qtg.QKeySequence("Ctrl+V"),
        )
        edit_menu.addAction(paste_action)
        # ...他アクションも必要に応じて追加

        # ===== [ヘルプ]メニューのアクション追加
        help_action = qtg.QAction(
            self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogHelpButton),
            "ヘルプ",
            self,
            triggered=lambda: self.statusBar().showMessage("ヘルプは作成中です。"),
        )
        help_menu.addAction(help_action)

        # [XXXについて] アクション
        help_menu.addAction("XXXについて", self.show_about_dialog)
        # ...他アクションも必要に応じて追加
        # =============================================

        # ================ ツールバー ==================
        toolbar = self.addToolBar("ツール")
        toolbar.setMovable(True)
        toolbar.setFloatable(False)
        toolbar.setAllowedAreas(
            qtc.Qt.ToolBarArea.TopToolBarArea | qtc.Qt.ToolBarArea.BottomToolBarArea
        )
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        toolbar.addAction(help_action)
        # =============================================

        # =============== ステータスバー ===============
        self.statusBar().showMessage("ようこそ!")
        # =============================================

        # 画面表示
        self.show()

    def open_file(self):
        """ファイルを開く"""
        # ファイルダイアログを表示
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "ファイルを開く",
            qtc.QDir.currentPath(),
            "テキストファイル (*.txt);;すべてのファイル (*)",
            "テキストファイル (*.txt)",
            options=qtw.QFileDialog.Option.DontUseNativeDialog
            | qtw.QFileDialog.Option.DontResolveSymlinks,
        )
        # ファイル読み込み
        if filename:
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    self.text_edit.setText(f.read())
            except Exception as ex:
                selected = qtw.QMessageBox.critical(
                    self,
                    "ファイルオープンエラー",
                    f"ファイルが開けませんでした: {ex}",
                    qtw.QMessageBox.StandardButton.Ok,
                    qtw.QMessageBox.StandardButton.Ok,
                )

    def save_file(self):
        """ファイルを保存する"""
        # ファイルダイアログを表示
        filename, _ = qtw.QFileDialog.getSaveFileName(
            self,
            "ファイルを保存する",
            qtc.QDir.currentPath(),
            "テキストファイル (*.txt);;すべてのファイル (*)",
            "テキストファイル (*.txt)",
            qtw.QFileDialog.Option.DontUseNativeDialog
            | qtw.QFileDialog.Option.DontResolveSymlinks,
        )
        # ファイルの保存
        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(self.text_edit.toPlainText())
            except Exception as ex:
                selected = qtw.QMessageBox.critical(
                    self,
                    "ファイルオープンエラー",
                    f"ファイルが開けませんでした: {ex}",
                    qtw.QMessageBox.StandardButton.Ok,
                    qtw.QMessageBox.StandardButton.Ok,
                )

    def show_about_dialog(self):
        """Aboutダイアログ表示"""
        qtw.QMessageBox.about(self, "プログラム名", "プログラムの説明内容を記載する...")


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
