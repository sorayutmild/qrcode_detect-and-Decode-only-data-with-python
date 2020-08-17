import cv2
import numpy as np
from pyzbar.pyzbar import decode

path_data = "C:/Users/Acer/Downloads/QRCODE/data/" #Change it when use another computer 
h = 0
dataList = []   

def draw_boundary(img):
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img, [pts], True, (0,255,0), 5)
    coord = barcode.polygon
    return img, coord

cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    #code = decode(img)
    for barcode in decode(img):
        data = barcode.data.decode()
        print(data)
        img ,coord = draw_boundary(img)
        key = cv2.waitKey(1) & 0xFF # for next line
        if key == ord('1') and len(coord) == 4: # len(coord)==4 for capture only when it has box boundary(has qrcode)
            h+=1
            cv2.imwrite(path_data + 'Qrcode_' + str(h) + '.png', img)
            print("************************************QRcode_" + str(h) + "Collected*****************************************")
            dataList.append(data)
    cv2.imshow('img',img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
dataList = list(dict.fromkeys(dataList)) # delete duplicate data in dataList เอาไว้กันถ้ารูปมันเกิดซ้ำ
print(dataList)
cap.release()
cv2.destroyAllWindows()  
# Data collected

input("Press the <ENTER> key to continue...") #pause program

# Now, This is code for scan QRcode when car has already driven.
cap = cv2.VideoCapture(0)
while(True):
    ret, img = cap.read()
    for barcode in decode(img):
        data = barcode.data.decode()
        print(data)
        img ,coord = draw_boundary(img)
        if data in dataList:
            print("found")
    cv2.imshow('img', img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
cap.release()
cv2.destroyAllWindows()  