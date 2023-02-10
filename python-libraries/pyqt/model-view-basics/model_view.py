"""Model-Viewを使ったアプリケーション開発
QObjectやQWidgetを継承したModel-Viewの実装

[説明ページ]
https://tech.nkhn37.net/pyqt-model-view-class-basics/#QObjectQWidgetModel-View
"""
import sys
from pathlib import Path

from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg
from PyQt6 import QtWidgets as qtw


class Model(qtc.QObject):
    """Modelクラス"""

    # エラー用シグナル定義
    error = qtc.pyqtSignal(str)

    def save(self, filename, content):
        """ファイル保存

        Args:
            filename: 保存対象ファイルパス
            content: 保存コンテンツ
        """
        error = ""
        file_path = Path(filename)
        if not filename:
            error = "ファイル名が空です。"
        elif file_path.exists():
            error = f"ファイルが存在しています。{filename}"
        else:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(content)
            except Exception as ex:
                error = f"ファイルを書き込めませんでした。: {ex}"

        if error:
            self.error.emit(error)


class View(qtw.QWidget):
    """Viewクラス"""

    # 実行シグナル定義
    submitted = qtc.pyqtSignal(str, str)

    def __init__(self):
        """Viewコンストラクタ"""
        super().__init__()

        # 画面要素の定義
        self.filename = qtw.QLineEdit()
        self.content = qtw.QTextEdit()
        self.save_button = qtw.QPushButton("保存", clicked=self.submit)

        # 画面レイアウトと要素の定義
        layout = qtw.QVBoxLayout()
        layout.addWidget(self.filename)
        layout.addWidget(self.content)
        layout.addWidget(self.save_button)
        # レイアウトの設定
        self.setLayout(layout)

    def submit(self):
        """保存実行"""
        self.submitted.emit(self.filename.text(), self.content.toPlainText())

    def show_error_message(self, error):
        """エラーダイアログ表示

        Args:
            error: エラーメッセージ
        """
        qtw.QMessageBox.critical(None, "エラー", error)


class MainWindow(qtw.QMainWindow):
    """メインウィンドウ"""

    def __init__(self):
        """メインウィンドウコンストラクタ"""
        super().__init__()

        # 画面タイトルの設定
        self.setWindowTitle("Model-Viewサンプル")
        # 画面サイズの設定
        self.resize(640, 360)

        # Viewをインスタンス化し、CentralWidgetへ設定
        self.view = View()
        self.setCentralWidget(self.view)

        # Modelをインスタンス化
        self.model = Model()

        # ModelとViewのsignal-slot接続
        self.view.submitted.connect(self.model.save)
        self.model.error.connect(self.view.show_error_message)

        # 画面表示
        self.show()


def main():
    """メイン関数"""
    app = qtw.QApplication(sys.argv)
    mv = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
