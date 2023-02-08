"""画面開発で使えるQtWidgets
QPushButton: ボタン
ボタン押下した時に押下状態を保持(チェック状態で表示) checkable=True, checked=True

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_checkableTrue_checkedTrue
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPushButton")
        self.resize(320, 240)

        # ===== QPushButton ボタン押下した時に押下状態を保持（チェック状態で表示）
        push_button = qtw.QPushButton("クリック", self, checkable=True, checked=True)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
