# Made for "Don't Tap the White Tile"

import pyautogui
import time
time.sleep(5)

########
# Tested on 1920x1080 screen. May need to adjust parameters depending on device.
########

pyautogui.PAUSE = 0
while True:
    x, y = pyautogui.position()
    if x >= 2400:
        pyautogui.moveTo(1517, y)
        x, y = pyautogui.position()
    if pyautogui.pixel(x, y)[0] == 83:
        quit()
    if pyautogui.pixel(x, y)[0] == 17 and pyautogui.pixel(x, y-10)[0] == 17:
        pyautogui.click()
        pyautogui.moveTo(1517, y)
    else:
        pyautogui.moveRel(265, 0)
