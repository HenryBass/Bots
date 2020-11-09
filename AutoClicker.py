import pyautogui
import time

print("You will have 5 seconds to position your mouse before the clicker starts. Put your mouse into any corner of your screen to stop it.")
input("Start?")

time.sleep(5)
pyautogui.PAUSE = 0

while True:
    pyautogui.click()
