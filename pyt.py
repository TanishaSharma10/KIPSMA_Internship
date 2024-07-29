import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Load the image of the gold ornament
img = cv2.imread('pil.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to enhance the text
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Apply dilation to thicken the text
kernel = np.ones((3, 3), np.uint8)
dilated = cv2.dilate(thresh, kernel, iterations=1)

# Write the pre-processed image to disk as a temporary file
filename = "{}.png".format("temp")
cv2.imwrite(filename, dilated)

# Load the image using pytesseract
text = pytesseract.image_to_string(cv2.imread(filename))

# Print the recognized text
print("Recognized Text: {}".format(text))

# Remove the temporary file
import os
os.remove(filename)

# # Display the output
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()