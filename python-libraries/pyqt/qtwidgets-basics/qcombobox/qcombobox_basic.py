"""画面開発で使えるQtWidgets
QComboBox: コンボボックス
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#i-9
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.resize(320, 240)

        # ===== QComboBox 基本的な使い方
        combobox = qtw.QComboBox(self)
        combobox.addItem("item 1", 1)
        combobox.addItem("item 2", "text")
        combobox.addItem("item 3", qtw.QWidget)
        combobox.insertItem(1, "item 1.5", 2)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()