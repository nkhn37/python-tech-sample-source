"""画面開発で使えるQtWidgets
QTextEdit: テキストエディット欄
折り返し設定 lineWrapMode, lineWrapColumnOrWidth

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_lineWrapMode_lineWrapColumnOrWidth
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        self.resize(320, 240)

        # ===== QTextEdit 折り返し設定
        textedit = qtw.QTextEdit(
            self,
            lineWrapMode=qtw.QTextEdit.LineWrapMode.FixedColumnWidth,
            lineWrapColumnOrWidth=20,
        )

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
