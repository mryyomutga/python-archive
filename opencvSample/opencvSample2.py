import cv2
import numpy as np
from matplotlib import pyplot as plot

cascade_f = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cascade_e = cv2.CascadeClassifier("haarcascade_eye.xml")

# カメラをキャプチャする
cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

# print(cap.get(3), cap.get(4))
cap.set(3,1366)
cap.set(4, 768)
overlay = cv2.imread("../../img/icon.jpg")

def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    global overlay
    while True:
        # retは画像を取得成功フラグ
        ret, frame = cap.read()

        # フレームをリサイズ
        # sizeは例えば(800, 600)
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)
        
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # eyes
        # eyes = cascade_e.detectMultiScale(frame,scaleFactor=1.2,minNeighbors=2,minSize=(10,10))
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (64, 255, 255), thickness=2)

        # face
        face = cascade_f.detectMultiScale(frame,scaleFactor=1.2,minNeighbors=3,minSize=(10,10))
        for (x, y, w, h) in face:
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 128, 64), thickness=2)
            # overlay = cv2.resize(overlay, (w, h))
            frame[y:y+h,x:x+w] = overlay[0:w,0:h]
        
        # 鏡のように映るか否か
        if mirror is True:
            frame = frame[:,::-1]

        # cv2.imshow("face", gray)
        # フレームを表示する
        cv2.imshow("camera capture", frame)
        cv2.moveWindow("camera capture", 0, 0)

        # plot.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # plot.show()

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27: # ESCキーで終了
            break

    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_camera()
