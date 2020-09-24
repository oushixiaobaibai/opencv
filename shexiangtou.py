import numpy as np
import cv2
#从摄像头获取图像数据
cap = cv2.VideoCapture(0)

while(True):
    # ret 读取成功Ture或失败False
    #frame 读取的图像内容
    #读取一帧数据
    ret,frame = cap.read()
    #变为灰度图
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    #waitKey功能是不断刷新图像，单位ms,返回值是当前键盘按键值
    #ord返回对应的ASCII数值
    if cv2.waitKey(1) & 0xfff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
