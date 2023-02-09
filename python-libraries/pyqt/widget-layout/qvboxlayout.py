"""ウィジェットのレイアウト方法
垂直方向にレイアウト: QVBoxLayout

[説明ページ]
https://tech.nkhn37.net/pyqt-widget-layout/#QVBoxLayout
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout")
        self.resize(320, 240)

        # 垂直(vertical)レイアウトの作成とメインウィンドウへの設定
        vertical_layout = qtw.QVBoxLayout()
        self.setLayout(vertical_layout)

        # ウィジェットを用意
        label = qtw.QLabel("ラベル", self)
        line_edit = qtw.QLineEdit(self, placeholderText="入力してください。")
        check = qtw.QCheckBox("チェック", self)
        button = qtw.QPushButton("ボタン", self)

        # レイアウトにウィジェットを追加
        vertical_layout.addWidget(label)
        vertical_layout.addWidget(line_edit)
        vertical_layout.addWidget(check)
        vertical_layout.addWidget(button)
        vertical_layout.addStretch()

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
