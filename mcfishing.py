import cv2
import pyautogui

def hookinit(x, y, w, h, n):
    pyautogui.screenshot("fishing_" + str(n)+ ".png", region = (x, y, w, h))
    img = cv2.imread("fishing_" + str(n) + ".png")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)
    cv2.imshow("img_" + str(n), binary)
    num = cv2.countNonZero(binary)
    return num

(x_0,y_0) = pyautogui.size()
x = x_0 * (0.50 - 0.04 / 2)
y = y_0 * 0.28
w = x_0 * 0.04
h = y_0 * 0.18
i = 0
pyautogui.sleep(5)
num_0 = hookinit(x, y, w, h, 0)

while(1):
    num = hookinit(x, y, w, h, 1)
    if(num_0 < 100):
        pyautogui.click(button='right')
        pyautogui.sleep(2)
        num_0 = hookinit(x, y, w, h, 0)
        continue
    if(num < 0.7 * num_0):
        i = i + 1
        print("Hooked!" + str(i))
        print(num_0)
        pyautogui.click(button='right')
        pyautogui.sleep(1)
        pyautogui.click(button='right')
        pyautogui.sleep(2)
        num_0 = hookinit(x, y, w, h, 0)
    cv2.waitKey(100)
