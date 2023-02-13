"""signalとslotの使用方法
制約事項:引数の数
(slotの引数が渡すデータよりも多い場合 → エラー)

[説明ページ]
https://tech.nkhn37.net/pyqt-signal-slot-basics/#slot
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        # 画面タイトルの設定
        self.setWindowTitle("signalとslotの基本: 制限")
        # 画面サイズの設定
        self.resize(640, 360)

        # メインレイアウトの設定
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        # ボタンウィジェットの用意
        self.quitbutton = qtw.QPushButton("ボタン")
        # clickedのシグナルをcloseのスロットに接続(connect)
        self.quitbutton.clicked.connect(self.func_args)

        # ウィジェットをレイアウトに追加
        main_layout.addWidget(self.quitbutton)
        main_layout.addStretch()

        # 画面表示
        self.show()

    def func_args(self, arg1, arg2, arg3):
        """スロット関数

        Args:
            arg1: 引数1
            arg2: 引数2
            arg3: 引数3
        """
        print("func_args")


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
