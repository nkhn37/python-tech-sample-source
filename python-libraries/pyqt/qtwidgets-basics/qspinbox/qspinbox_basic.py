"""画面開発で使えるQtWidgets
QSpinBox: スピンボックス
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#i-10
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox")
        self.resize(320, 240)

        # ===== QSpinBox 基本的な使い方
        spinbox = qtw.QSpinBox(self, value=50, minimum=0, maximum=100)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
