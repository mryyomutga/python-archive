# -*- coding: utf-8 -*-
import socket

RECV_BUF = 1024	# データ受け取りバッファ

def main():
	# IPv4/TCPのソケットを設定
	cliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Address already in useを回避
	cliSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

	# ポートとアドレスの設定
	# 任意のアドレスは''
	host = "localhost"
	port = 8000
	# 設定したアドレスとポートに接続する
	cliSocket.connect((host, port))

	while True:
		# 送信バイト数取得時のエラー回避のためutf-8でencode
		sent_message = input("Send: ").encode("utf-8")
		# sent_messageをサーバーに送信
		while True:
			# 送信したバイト数を取得
			sent_len = cliSocket.send(sent_message)
			# 全データの送信完了
			if sent_len == len(sent_message):
				break
			# 送信できなかった分だけ再度送信
			sent_message = sent_message[sent_len:]

		# クライアントの切断
		if len(sent_message) == 0:
			break
		elif sent_message == "END":
			break

		# データ受け取り
		try:
			# 1024バイトのデータを取得
			# byte型で受信するためdecodeしてstr型に変換
			recv_message = cliSocket.recv(RECV_BUF).decode()
			print("Recv: {}".format(recv_message))
		except OSError:
			break
		
	# サーバーとの接続が終了
	cliSocket.close()
	print("Bye")

if __name__ == "__main__":
	main()

