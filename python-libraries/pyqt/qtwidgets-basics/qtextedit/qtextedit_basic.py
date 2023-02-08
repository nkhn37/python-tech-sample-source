"""画面開発で使えるQtWidgets
QTextEdit: テキストエディット欄
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#i-5
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

        # ===== QTextEdit 基本的な使い方
        textedit = qtw.QTextEdit(self)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
