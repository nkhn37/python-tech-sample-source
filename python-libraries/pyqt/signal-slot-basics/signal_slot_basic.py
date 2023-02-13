"""signalとslotの使用方法
基本的な使い方: ウィジェットのsignalをslotに接続する

[説明ページ]
https://tech.nkhn37.net/pyqt-signal-slot-basics/#signalslot-2
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
        self.setWindowTitle("signalとslotの基本")
        # 画面サイズの設定
        self.resize(320, 100)

        # メインレイアウトの設定
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        # ボタンウィジェットの用意
        self.quitbutton = qtw.QPushButton("終了")
        # clickedのシグナルをcloseのスロットに接続(connect)
        self.quitbutton.clicked.connect(self.close)

        # # === よりシンプルに記載する場合
        # # ボタンウィジェットの用意時に、signalとslotを設定
        # self.quitbutton = qtw.QPushButton("終了", clicked=self.close)

        # ウィジェットをレイアウトに追加
        main_layout.addWidget(self.quitbutton)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
