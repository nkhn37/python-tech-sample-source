"""ウィジェットのレイアウト方法
グリッド状にレイアウト: QGridLayout

[説明ページ]
https://tech.nkhn37.net/pyqt-widget-layout/#QGridLayout
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        self.resize(320, 240)

        # グリッド(Grid)レイアウトの作成とメインウィンドウへの設定
        grid_layout = qtw.QGridLayout()
        self.setLayout(grid_layout)

        # ウィジェットを用意
        self.label = qtw.QLabel("ラベル", self)
        self.line_edit = qtw.QLineEdit(self, placeholderText="入力してください。")
        self.check = qtw.QCheckBox("チェック", self)
        self.button = qtw.QPushButton("ボタン", self)

        # レイアウトにウィジェットを追加
        grid_layout.addWidget(self.label, 0, 0)
        grid_layout.addWidget(self.line_edit, 0, 1)
        grid_layout.addWidget(self.check, 1, 0)
        grid_layout.addWidget(self.button, 1, 1)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
