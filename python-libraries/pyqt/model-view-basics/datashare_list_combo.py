"""Model-Viewを使ったアプリケーション開発
PyQtで用意されているModel-Viewクラスの利用
使用例: リストとコンボボックスのデータ共有

[説明ページ]
https://tech.nkhn37.net/pyqt-model-view-class-basics/#i-3
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
        self.setWindowTitle("Qt Model-View")

        # ===== モデルを使った実装
        # データの定義
        list_data = ["item01", "item02", "item03", "item04", "item05"]

        # Modelを定義し、データを設定
        self.model = qtc.QStringListModel(list_data)

        # Viewの定義
        # リスト
        self.list_view = qtw.QListView()
        self.list_view.setModel(self.model)
        # コンボボックス
        self.combobox_view = qtw.QComboBox()
        self.combobox_view.setModel(self.model)

        # レイアウトを用意し部品を設定
        layout = qtw.QHBoxLayout()
        layout.addWidget(self.list_view)
        layout.addWidget(self.combobox_view)
        self.setLayout(layout)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
