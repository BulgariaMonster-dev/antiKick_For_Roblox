import time
from config import waitTime as timme
from pynput.keyboard import Key, Controller

keyboard = Controller()

while(True):
    time.sleep(timme)
    keyboard.press('w')
    keyboard.release('w')
