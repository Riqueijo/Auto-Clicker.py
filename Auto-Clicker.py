from pynput.mouse import Button, Controller
from time import sleep

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        #Stop listener
        return False

mouse = Controller()
posic = mouse.position
a=0
while a == 0:

    mouse.press(Button.left)
    mouse.release(Button.left)
    sleep(0.02)
    on_click(posic, ' ', 'left','yes')

