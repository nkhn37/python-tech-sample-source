"""画面開発で使えるQtWidgets
QDateTimeEdit: 日付エディット
期間の最大・最小を設定 minimumDate, maximumDate

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_minimumDate_maximumDate
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

        # ===== QDateTimeEdit 期間の最大・最小を設定
        datetimebox = qtw.QDateTimeEdit(
            self,
            date=qtc.QDate.currentDate(),
            time=qtc.QTime(0, 0),
            calendarPopup=True,
            minimumDate=qtc.QDate(2000, 1, 1),
            maximumDate=qtc.QDate(2030, 12, 31),
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
