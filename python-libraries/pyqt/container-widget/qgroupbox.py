"""コンテナウィジェットの使い方
グループボックス: QGroupBox

[説明ページ]
https://tech.nkhn37.net/pyqt-container-widgets/#_QGroupBox
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
        self.setWindowTitle("QGroupWidget")
        # 画面サイズの設定
        self.resize(640, 360)

        # メインレイアウトの設定
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        # GroupBoxウィジェットの用意
        groupbox = qtw.QGroupBox(
            "ボタンリスト",
            checkable=False,
            checked=False,
            alignment=qtc.Qt.AlignmentFlag.AlignLeft,
            flat=False,
        )
        group_layout = qtw.QHBoxLayout()
        groupbox.setLayout(group_layout)
        group_layout.addWidget(qtw.QPushButton("登録"))
        group_layout.addWidget(qtw.QPushButton("更新"))
        group_layout.addWidget(qtw.QPushButton("削除"))

        # メインレイアウトに追加
        main_layout.addWidget(groupbox)
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
