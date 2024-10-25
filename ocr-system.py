# import the opencv library
#from typing import Sized
import os
from gtts import gTTS
import cv2
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# define a video capture object
vid = cv2.VideoCapture(0)
count = 1
while(True):
    
    # Capture the video frame by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        image_name = "image/frame{}.jpg".format(count)
        cv2.imwrite(image_name,frame)
        count += 1
        image = cv2.imread(r"{}".format(image_name))
        image1 = cv2.cvtColor(image ,cv2.COLOR_BGR2RGB)
        image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(image1)
        print(text)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()



language = "ar"
 
myobj = gTTS(text = text, lang = language, slow = False)

myobj.save("objet.mp3")

os.system(r"C:\Users\ihebt\OneDrive\Bureau\ocr\objet.mp3")


