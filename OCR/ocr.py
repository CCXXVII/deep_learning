import cv2
import pytesseract
resim = cv2.imread("stajBook5.jpeg")
def ocr_islem(resim):
    yazi = pytesseract.image_to_string(resim)
    return yazi
def grayscale(resim):
    gray_scl = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    return gray_scl
def noise(resim):
    blur = cv2.medianBlur(resim, 5)
    return blur
def threshold(resim):
    thresh_hld = cv2.threshold(resim, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh_hld
resim = grayscale(resim)
resim = noise(resim)
resim = threshold(resim)
print(ocr_islem(resim))