"""PySide概要
PySideを使用した簡単なサンプルプログラム

[説明ページ]
https://tech.nkhn37.net/pyqt-gui-programming-overview/#PySide
"""
import sys

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        """コンストラクタ"""
        super().__init__()
        self.setWindowTitle("Hello, World!")
        self.resize(320, 240)

        label = qtw.QLabel(self)
        label.setText("サンプルプログラム！")

        # 画面表示
        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
