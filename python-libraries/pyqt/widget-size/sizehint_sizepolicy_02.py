"""ウィジェット(Widget)のサイズを制御する方法
サイズヒント(sizeHint)とサイズポリシー(sizePolicy)を使用する
設定例2: 可能な限り広いスペースを確保するがサイズヒントよりは小さくならない

[説明ページ]
https://tech.nkhn37.net/pyqt-widget-size-control/#i-6
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
        self.setWindowTitle("ウィジェットのサイズを制御する")
        # 画面サイズの設定
        self.resize(640, 360)

        # レイアウトの作成
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        # ウィジェットの用意
        textedit = qtw.QTextEdit(self)
        print(textedit.sizeHint())
        # サイズヒントよりも小さくならないが拡張する
        textedit.setSizePolicy(
            qtw.QSizePolicy.Policy.MinimumExpanding,
            qtw.QSizePolicy.Policy.MinimumExpanding,
        )
        button = qtw.QPushButton("登録", self)

        # レイアウトにウィジェットを設定
        layout.addWidget(textedit)
        layout.addWidget(button)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
