"""socket通信の基本的な使い方
サーバー側プログラム (TCP)

[説明ページ]
https://tech.nkhn37.net/python-socket-basic/#TCP
"""
import socket


def tcp_server_program():
    host = "127.0.0.1"
    port = 50000

    # ソケット作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # バインド(ソケットにIPとポート番号を紐づけ)
        server_socket.bind((host, port))
        # 同時接続を1つ待機
        server_socket.listen(1)

        while True:
            # 接続を待機
            conn, address = server_socket.accept()
            with conn:
                while True:
                    # データを受信 (データの最大バイトを1,024)
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"data: {data}, address:{address}")


def main():
    tcp_server_program()


if __name__ == "__main__":
    main()
