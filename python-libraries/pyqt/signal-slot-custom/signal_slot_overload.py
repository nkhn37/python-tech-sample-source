"""カスタムsignalとslotの作成方法
signalとslotのオーバーロード

[説明ページ]
https://tech.nkhn37.net/pyqt-signal-slot-custom/#signalslot-2
"""
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class FormWindow(qtw.QWidget):
    """フォームウィンドウ"""

    # シグナルを定義(オーバーロード)
    submitted = qtc.pyqtSignal([str], [int, str])

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
        text = self.line_edit.text()
        if text.isdigit():
            # 数値の場合は数値と文字列を返却する
            self.submitted[int, str].emit(int(text), text)
        else:
            # その他の場合は文字列のみ返却する
            self.submitted[str].emit(text)

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
        self.form_window.submitted[str].connect(self.on_submitted_str)
        self.form_window.submitted[int, str].connect(self.on_submitted_int_and_str)
        # フォームウィンドウを表示
        self.form_window.show()

    def on_submitted_str(self, text):
        """slot (strのsignal用)

        Args:
            text: 文字列
        """
        self.label.setText(text)

    def on_submitted_int_and_str(self, value, text):
        """slot (intとstrのsignal用)

        Args:
            value: 数値
            text: 文字列
        """
        disp_text = f"value:{value}, text:{text}"
        self.label.setText(disp_text)


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
