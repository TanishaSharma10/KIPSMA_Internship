import cv2
import pytesseract 
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = cv2.imread('pil.jpeg')

custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))