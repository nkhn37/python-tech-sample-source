"""signalとslotの使用方法
制約事項:引数の数
(slotの引数が渡すデータよりもすくない場合 → OK)

[説明ページ]
https://tech.nkhn37.net/pyqt-signal-slot-basics/#slotOK
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
        self.resize(320, 100)

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

    def func_args(self):
        """スロット"""
        print("func_args")


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
