"""socket通信の基本的な使い方
クライアント側プログラム (TCP)

[説明ページ]
https://tech.nkhn37.net/python-socket-basic/#TCP
"""
import socket


def tcp_client_program():
    host = "127.0.0.1"
    port = 50000

    # ソケット作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # 接続
        client_socket.connect((host, port))

        # メッセージの作成
        message = b"Message"

        # メッセージをサーバーに送信
        client_socket.sendall(message)


def main():
    tcp_client_program()


if __name__ == "__main__":
    main()
