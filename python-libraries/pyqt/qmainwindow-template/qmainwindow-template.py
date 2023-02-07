"""QMainWindowを継承した画面開発テンプレート

[説明ページ]
https://tech.nkhn37.net/pyqt-qmainwindow-program-template/#QMainWindow
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QMainWindow):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        # 画面タイトルの設定
        self.setWindowTitle("ウィンドウタイトル")
        # 画面サイズの設定
        self.resize(640, 360)

        # ========== ここに画面要素を記載する ==========
        # ・メニューの追加
        # ・メニュー内のアクションの追加
        # ・ツールバーの追加
        # ・ステータスバーの追加
        # ...
        # ============================================

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
