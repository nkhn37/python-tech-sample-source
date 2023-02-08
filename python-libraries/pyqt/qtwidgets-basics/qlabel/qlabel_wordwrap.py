"""画面開発で使えるQtWidgets
QLabel: ラベル
折り返しを設定する wordWrap=True

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_wordWrapTrue
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

        # ===== QLabel 折り返しを設定する
        label = qtw.QLabel("QLabel サンプル xxxxx yyyyy zzzzz", self, wordWrap=True)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
