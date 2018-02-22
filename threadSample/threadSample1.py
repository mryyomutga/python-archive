import threading
import time

# サブクラスを作ってスレッドを扱う
class MyThread(threading.Thread):
	"""threading.Threadを継承する"""
	def __init__(self, id):
		super(MyThread, self).__init__()
		self.id = id

	def run(self):
		""""runメソッドをオーバーライドする"""
		print("start sub thread{}".format(self.id))
		for i in range(5):
			time.sleep(1)
			print("sub thread {} : count : {}".format(self.id, i))

if __name__ == "__main__":
	# threading.Threadクラスを継承したサブクラスのインスタンスを生成
	th1 = MyThread(1)
	th2 = MyThread(2)
	# startメソッドを呼び出し、スレッドを実行
	th1.start()
	th2.start()
	print("start main thread")
	for i in range(5):
		time.sleep(1)
		print("main thread  : count :", i)
	# mainスレッドが終了したときにすべてのスレッドを終了させない
	th1.join()
	th2.join()
