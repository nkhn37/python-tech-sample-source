"""画面開発で使えるQtWidgets
QSpinBox: スピンボックス
プレフィックスとサフィックスの表示 prefix, suffix

[説明ページ]
https://tech.nkhn37.net/pyqt-widgets-list/#_prefix_suffix
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox")
        self.resize(320, 240)

        # ===== QSpinBox プレフィックスとサフィックスを表示
        spinbox = qtw.QSpinBox(
            self, value=50, minimum=0, maximum=100, prefix="¥", suffix="+ 税"
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
