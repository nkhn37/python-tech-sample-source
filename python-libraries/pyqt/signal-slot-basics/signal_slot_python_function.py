"""signalとslotの使用方法
基本的な使い方: Pythonの関数へ接続する

[説明ページ]
https://tech.nkhn37.net/pyqt-signal-slot-basics/#Python
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

        # ウィジェットの用意
        self.line_edit1 = qtw.QLineEdit()
        # signalとslotの設定 (printでコンソールへ出力)
        self.line_edit1.textChanged.connect(print)
        self.line_edit1.editingFinished.connect(lambda: print("編集終了"))

        # ウィジェットをレイアウトに追加
        main_layout.addWidget(self.line_edit1)
        main_layout.addStretch()

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
