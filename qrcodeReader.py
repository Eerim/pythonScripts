import cv2
import webbrowser
import time

image = cv2.imread("idax_qrcode.png")
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(image)
print("Redirecting... ", data)
time.sleep(2)
webbrowser.open(data)
