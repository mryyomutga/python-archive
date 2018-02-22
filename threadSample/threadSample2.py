import threading
import time

# Threadクラスのインスタンスでスレッドを扱う

def myThreadFunc(id):
	"""スレッドで処理させる関数"""
	print("start sub thread{}".format(id))
	for i in range(5):
			time.sleep(1)
			print("sub thread {} : count : {}".format(id, i))

if __name__ == "__main__":
	# Threadクラスのインスタンスを生成
	# targetにスレッドで実行させる関数を指定
	th1 = threading.Thread(target=myThreadFunc, args=(1,))
	th2 = threading.Thread(target=myThreadFunc, args=(2,))
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