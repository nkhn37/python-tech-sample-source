"""画面開発で使えるQtWidgets
QLabel: ラベル
マージンを設定する margin

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_margin
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(320, 240)

        # ===== QLabel マージンを設定する
        label = qtw.QLabel("QLabel サンプル", self, margin=50)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
