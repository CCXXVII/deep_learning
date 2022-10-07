import cv2

img = cv2.imread("deneme_tahtasi.png")
#resize 32 32
img = cv2.resize(img, (32, 32))
