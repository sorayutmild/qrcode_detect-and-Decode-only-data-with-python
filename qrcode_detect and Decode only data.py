import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
while(True):
    ret, img = cap.read()
    #code = decode(img)
    for barcode in decode(img):
        data = barcode.data.decode()
        print(data)
    cv2.imshow('img',img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()