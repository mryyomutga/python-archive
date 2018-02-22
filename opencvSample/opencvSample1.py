import cv2
import matplotlib
import matplotlib.pyplot as plot
import numpy as np

# スケール変換した画像を取得する
def getResizeImage(scale=1):
	imgHeight = int(img.shape[0] * scale)
	imgWidth = int(img.shape[1] * scale)
	return cv2.resize(img, (imgWidth, imgHeight), interpolation=cv2.INTER_CUBIC)

# 平均化フィルタ
def cvtAve():
	return cv2.blur(img, ksize=(3,3))

# ガウシアンフィルタ
def gaussian():
	return cv2.GaussianBlur(img, ksize=(3,3), sigmaX=1.3)
	
# メディアンフィルタ
def median():
	return cv2.medianBlur(img, ksize=5)

# 一次微分
def firstDerivate():
	kernel = np.array([[0,0,0],
					   [-1,0,1],
					   [0,0,0]])
	return cv2.filter2D(img, cv2.CV_64F, kernel)

# prewitt
def prewitt():
	kernel = np.array([[-1,0,1],
					   [-1,0,1],
					   [-1,0,1]])
	return cv2.filter2D(img, cv2.CV_64F, kernel)

# sobel
def sobel(dx=1, dy=0):
	return cv2.Sobel(img, cv2.CV_32F, dx, dy, ksize=3)

if __name__ == "__main__":
	img = cv2.imread("./../img/icon.png")
	img = getResizeImage(3/7)
	# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

	img = cvtAve()
	# img = gaussian()
	# img = median()

	# img = firstDerivate()
	# img = prewitt()
	# img = sobel(0, 1)
	
	cv2.imshow("title", img)

	while True:
		if cv2.waitKey(10) == 27:
			break
	cv2.destroyAllWindows()
	
