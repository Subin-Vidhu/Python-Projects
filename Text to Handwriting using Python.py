import pywhatkit as kit
import cv2

kit.text_to_handwriting("Hope you are doing well, Maaandu", save_to="C:/Users/pc/Pictures/RESULTS/handwriting.png")
img = cv2.imread("handwriting.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()