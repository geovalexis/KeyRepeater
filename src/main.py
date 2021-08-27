from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
key_to_repeat = "a"

while True:
    time.sleep(2) #Seconds to wait before pressing the key
    keyboard.press(key_to_repeat)
    keyboard.release(key_to_repeat)