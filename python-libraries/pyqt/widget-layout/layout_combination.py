"""ウィジェットのレイアウト方法
レイアウトの組み合わせ

[説明ページ]
https://tech.nkhn37.net/pyqt-widget-layout/#i
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layoutの組み合わせ")
        self.resize(320, 240)

        # レイアウトの作成とメインウィンドウへの設定
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        # ウィジェットを用意
        label1 = qtw.QLabel("ラベル", self)
        label2 = qtw.QLabel("入力欄: ", self)
        line_edit = qtw.QLineEdit(self, placeholderText="入力してください。")
        button = qtw.QPushButton("ボタン", self)

        # レイアウトにウィジェットを追加
        layout.addWidget(label1)
        # サブレイアウトを作成して追加
        sublayout = qtw.QHBoxLayout()
        sublayout.addWidget(label2)
        sublayout.addWidget(line_edit)
        layout.addLayout(sublayout)
        # 他のウィジェットを追加
        layout.addWidget(button)
        layout.addStretch()

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
