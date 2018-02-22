import time
import socket
import multiprocessing
import threading

RECV_BUF = 1024	# データ受け取りバッファ

# マルチプロセス・マルチスレッド化
def worker_thread(srvSocket):
	"""クライアントとの接続処理を行うハンドラ"""
	while  True:
		cliSocket, (client_address, client_port) = srvSocket.accept()
		print("Client: {0}:{1}".format(client_address, client_port))
		
		while True:
			try:
				# 1024バイトのデータを取得
				# byte型で取得するためdecodeしてstr型に変換
				recv_message = cliSocket.recv(RECV_BUF).decode()
				print("Recv: {0} from {1}:{2}".format(recv_message, client_address, client_port))
			except OSError:
				break
				
			# クライアントの切断
			if len(recv_message) == 0:
				break
			elif recv_message == "END":
				break
				
			# recv_messageをクライアントに送信
			# 送信データがbyte型になるため、encodeする
			sent_message = recv_message.encode("utf-8")
			while True:
				# 送信したバイト数を取得
				sent_len = cliSocket.send(sent_message)
				# 全データの送信完了
				if sent_len == len(sent_message):
					break
				# 送信できなかった分だけ再度送信
				sent_message = sent_message[sent_len:]
			
			print("Send: {0} to {1}:{2}".format(recv_message, client_address, client_port))

		# クライアントとの接続が終了
		cliSocket.close()
		print("Bye: {0}:{1}".format(client_address, client_port))

def worker_process(srvSocket):
	"""クライアントの接続を行うハンドラ"""
	THREAD_NUMBER = 10
	for _ in range(THREAD_NUMBER):
		thread = threading.Thread(target=worker_thread, args=(srvSocket,))
		thread.start()
	while True:
		time.sleep(1)

def main():
	# IPv4/TCPのソケットを設定
	srvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Address already in useを回避
	srvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

	# ポートとアドレスの設定
	# 任意のアドレスは''
	host = "localhost"
	port = 8000
	# バインドする
	srvSocket.bind((host, port))

	# クライアントを待ち受ける数を設定
	srvSocket.listen(32)

	# プロセス数の設定
	PROCESS_NUMBER = multiprocessing.cpu_count()
	# 処理をワーカープロセスに託す
	for _ in range(PROCESS_NUMBER):
		process = multiprocessing.Process(target=worker_process,
								  args=(srvSocket, ))
		# デーモンプロセスにする
		process.daemon = True
		# スレッドの起動
		process.start()

	while True:
		time.sleep(1)

if __name__ == '__main__':
	main()
	