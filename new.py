import pytesseract
import cv2 # pip install opencv-python
import matplotlib.pyplot as plt 
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=cv2.imread('pipe.jpeg')
plt.imshow(img)
img2char = pytesseract.image_to_string(img)
print(img2char)
imgbox= pytesseract.image_to_boxes(img)
print(imgbox)
imgH, imgW,_=img.shape
img.shape
for boxes in imgbox.splitlines():
    boxes=boxes.split(' ')
    x,y,w, h=int(boxes[1]), int(boxes[2]),int(boxes[3]),int(boxes[4])
    cv2.rectangle(img,(x,imgH-y),(w,imgH-h), (0,0,255),3)
    
    
plt.imshow(img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))