"""コンテナウィジェットの使い方
タブウィジェット: QTabWidget

[説明ページ]
https://tech.nkhn37.net/pyqt-container-widgets/#_QTabWidget
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
        self.setWindowTitle("QTabWidget")
        # 画面サイズの設定
        self.resize(640, 360)

        # メインレイアウトの設定
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        # ===== Tab1 の用意
        tab1 = qtw.QWidget(self)
        # タブ内のウィジェットの生成
        label = qtw.QLabel("Tab 1", self)
        line_edit = qtw.QLineEdit(self, placeholderText="入力してください。")
        checkbox = qtw.QCheckBox("チェック", self)
        button = qtw.QPushButton("登録", self)
        # タブ内のレイアウトの作成
        tab1_layout = qtw.QVBoxLayout()
        tab1.setLayout(tab1_layout)
        # ウィジェット配置
        tab1_layout.addWidget(label)
        tab1_layout.addWidget(line_edit)
        tab1_layout.addWidget(checkbox)
        tab1_layout.addWidget(button)
        tab1_layout.addStretch()

        # ===== Tab2 の用意
        tab2 = qtw.QWidget(self)
        # タブ内のウィジェットの生成
        label_2 = qtw.QLabel("Tab 2", self)
        text_edit_2 = qtw.QTextEdit(self)
        button_2 = qtw.QPushButton("登録", self)
        # タブ内のレイアウトの作成
        tab2_layout = qtw.QVBoxLayout()
        tab2.setLayout(tab2_layout)
        # ウィジェット配置
        tab2_layout.addWidget(label_2)
        tab2_layout.addWidget(text_edit_2)
        tab2_layout.addWidget(button_2)

        # ===== Tabウィジェットの用意
        tab_widget = qtw.QTabWidget(
            movable=True,
            tabPosition=qtw.QTabWidget.TabPosition.North,
            tabShape=qtw.QTabWidget.TabShape.Rounded,
        )
        # タブにウィジェットを追加
        tab_widget.addTab(tab1, "タブ 1")
        tab_widget.addTab(tab2, "タブ 2")

        # メインレイアウトに追加
        main_layout.addWidget(tab_widget)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
