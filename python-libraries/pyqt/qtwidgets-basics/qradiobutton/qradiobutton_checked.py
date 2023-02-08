"""画面開発で使えるQtWidgets
QRadioButton: ラジオボタン
チェック状態で表示 checked

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_checked-2
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton")
        self.resize(320, 240)

        # ===== QRadioButton チェック状態で表示
        radio_button = qtw.QRadioButton("チェック", self, checked=True)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
