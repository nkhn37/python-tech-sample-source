"""ウィジェットのレイアウト方法
水平方向にレイアウト: QHBoxLayout

[説明ページ]
https://tech.nkhn37.net/pyqt-widget-layout/#QHBoxLayout
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout")
        self.resize(640, 240)

        # 水平(horizontal)レイアウトの作成とメインウィンドウへの設定
        horizontal_layout = qtw.QHBoxLayout()
        self.setLayout(horizontal_layout)

        # ウィジェットを用意
        label = qtw.QLabel("ラベル", self)
        line_edit = qtw.QLineEdit(self, placeholderText="入力してください。")
        check = qtw.QCheckBox("チェック", self)
        button = qtw.QPushButton("ボタン", self)

        # レイアウトにウィジェットを追加
        horizontal_layout.addWidget(label)
        horizontal_layout.addWidget(line_edit)
        horizontal_layout.addWidget(check)
        horizontal_layout.addWidget(button)
        horizontal_layout.addStretch()

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
