"""カスタムsignalとslotの作成方法

[説明ページ]
https://tech.nkhn37.net/pyqt-signal-slot-custom/#signalslot
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class FormWindow(qtw.QWidget):
    """フォームウィンドウ"""

    # strのシグナルを定義
    submitted = qtc.pyqtSignal(str)

    def __init__(self):
        """コンストラクタ"""
        super().__init__()
        # 画面タイトルの設定
        self.setWindowTitle("フォーム")
        # レイアウトの設定
        layout = qtw.QHBoxLayout()
        self.setLayout(layout)

        # ウィジェットの生成
        self.line_edit = qtw.QLineEdit()
        self.submit_button = qtw.QPushButton("登録", clicked=self.on_submit)

        # レイアウト配置
        layout.addWidget(self.line_edit)
        layout.addWidget(self.submit_button)

    def on_submit(self):
        """登録ボタン用スロット"""
        # ボタン押下時にline_editに入力された値を送信
        self.submitted.emit(self.line_edit.text())
        # フォームウィンドウを閉じる
        self.close()


class MainWindow(qtw.QWidget):
    """メインウィンドウ"""

    def __init__(self):
        super().__init__()
        # 画面タイトルの設定
        self.setWindowTitle("カスタムスロットの作成")
        # 画面サイズの設定
        self.resize(320, 100)

        # メインレイアウトの設定
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)

        # ウィジェットの生成
        self.label = qtw.QLabel("文字列表示欄")
        self.change_button = qtw.QPushButton("変更")
        self.change_button.clicked.connect(self.on_change)

        # レイアウト配置
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.change_button)
        main_layout.addStretch()

        # 画面表示
        self.show()

    def on_change(self):
        """フォーム呼び出し用スロット"""
        # フォームウィンドウをインスタンス化
        self.form_window = FormWindow()
        # フォームウィンドウのシグナルをラベルのsetTextに接続
        self.form_window.submitted.connect(self.label.setText)
        # フォームウィンドウを表示
        self.form_window.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
