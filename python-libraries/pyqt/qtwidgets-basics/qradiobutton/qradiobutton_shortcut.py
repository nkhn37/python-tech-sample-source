"""画面開発で使えるQtWidgets
QRadioButton: ラジオボタン
ショートカットキーの設定 shortcut

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_shortcut-3
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

        # ===== QRadioButton ショートカットキーの設定
        radio_button = qtw.QRadioButton("チェック", self, shortcut=qtg.QKeySequence("Ctrl+P"))

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
