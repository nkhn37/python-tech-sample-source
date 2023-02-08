"""画面開発で使えるQtWidgets
QLineEdit: エディット欄
デフォルト値を設定する

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#i-4
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit")
        self.resize(320, 240)

        # ===== QLineEdit デフォルト値を設定する
        line_edit = qtw.QLineEdit("デフォルト値", self)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
