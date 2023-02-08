"""画面開発で使えるQtWidgets
QCheckBox: チェックボックス
ショートカットキーの設定 shortcut

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_shortcut-2
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox")
        self.resize(320, 240)

        # ===== QCheckBox ショートカットキーの設定
        checkbox = qtw.QCheckBox("チェック", self, shortcut=qtg.QKeySequence("Ctrl+P"))

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
