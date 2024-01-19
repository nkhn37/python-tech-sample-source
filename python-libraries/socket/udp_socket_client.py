"""socket通信の基本的な使い方
クライアント側プログラム (UDP)

[説明ページ]
https://tech.nkhn37.net/python-socket-basic/#UDP
"""
import socket


def udp_client_program():
    host = "127.0.0.1"
    port = 50000

    # ソケット作成
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # メッセージの作成
        message = b"Message"

        # メッセージをサーバーに送信
        client_socket.sendto(message, (host, port))


def main():
    udp_client_program()


if __name__ == "__main__":
    main()
