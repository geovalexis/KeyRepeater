from pynput.keyboard import Key, Controller

keyboard = Controller()
keyboard.press("A")
keyboard.release("A")