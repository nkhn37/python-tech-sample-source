"""画面開発で使えるQtWidgets
QLineEdit: エディット欄
クリアボタンの表示 clearButtonEnabled=True

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_clearButtonEnabledTrue
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

        # ===== QLineEdit クリアボタンの表示
        line_edit = qtw.QLineEdit(self, clearButtonEnabled=True)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
