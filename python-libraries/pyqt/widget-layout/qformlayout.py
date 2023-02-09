"""ウィジェットのレイアウト方法
フォーム形式のレイアウト: QFormLayout

[説明ページ]
https://tech.nkhn37.net/pyqt-widget-layout/#QFormLayout
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout")
        self.resize(320, 240)

        # フォーム(form)レイアウトの作成とメインウィンドウへの設定
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # ウィジェットを用意
        self.label = qtw.QLabel("入力フォーム", self)
        self.line_edit1 = qtw.QLineEdit(self)
        self.line_edit2 = qtw.QLineEdit(self)
        self.button = qtw.QPushButton("ボタン", self)

        # フォームレイアウトへの配置
        form_layout.addRow(self.label)
        form_layout.addRow("入力 1", self.line_edit1)
        form_layout.addRow("入力 2", self.line_edit2)
        form_layout.addRow(self.button)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
