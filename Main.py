import cv2
import pytesseract
import re
import numpy as np
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image of the gold jewelry
image_path = 'pil.jpeg'
image = cv2.imread(image_path)

# Perform OCR using PyTesseract
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(image, config=custom_config)
# print(text)

# Filter the recognized text to only include text related to gold jewelry
gold_jewelry_keywords = ['GOLD','P23HIGE']
filtered_text = []
for line in text.split('\n'):
    for keyword in gold_jewelry_keywords:
        if re.search(keyword, line, re.IGNORECASE):
            filtered_text.append(line)
            break

# Print the filtered text
# print('Recognized text:')
# for line in filtered_text:
#     print(line)

my_string = ', '.join(filtered_text)
print(my_string[slice(10,17)])

    