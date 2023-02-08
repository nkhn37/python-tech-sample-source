"""画面開発で使えるQtWidgets
QDateTimeEdit: 日付エディット
日時フォーマットの指定 displayFormat

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_displayFormat
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit")
        self.resize(320, 240)

        # ===== QDateTimeEdit 日時フォーマットの指定
        datetimebox = qtw.QDateTimeEdit(
            self,
            date=qtc.QDate.currentDate(),
            time=qtc.QTime(0, 0),
            displayFormat="yyyy-MM-dd HH:mm:ss",
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
