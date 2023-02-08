"""画面開発で使えるQtWidgets
QTextEdit: テキストエディット欄
プレースホルダーテキストの表示 placeholderText

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_placeholderText-2
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        self.resize(320, 240)

        # ===== QTextEdit プレースホルダーテキストの表示
        textedit = qtw.QTextEdit(self, placeholderText="テキストを入力してください。")

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
