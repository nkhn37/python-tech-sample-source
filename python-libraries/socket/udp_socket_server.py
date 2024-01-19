"""socket通信の基本的な使い方
サーバー側プログラム (UDP)

[説明ページ]
https://tech.nkhn37.net/python-socket-basic/#UDP
"""
import socket


def udp_server_program():
    host = "127.0.0.1"
    port = 50000

    # ソケット作成
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # バインド(ソケットにIPとポート番号を紐づけ)
        server_socket.bind((host, port))

        while True:
            # データを受信 (データの最大バイトを1,024)
            data, address = server_socket.recvfrom(1024)
            print(f"data: {data}, address:{address}")


def main():
    udp_server_program()


if __name__ == "__main__":
    main()
