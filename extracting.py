import os
from gtts import gTTS
from matplotlib import pyplot as plt
import cv2
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = cv2.imread(r"test1.JPG")
image1 = cv2.cvtColor(image ,cv2.COLOR_BGR2RGB)
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
plt.imshow(image2)
text = pytesseract.image_to_string(image1)
print(text)
