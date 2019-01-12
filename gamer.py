from pynput.keyboard import Key, Controller
import time
from PIL import ImageGrab
from PIL import Image
keyboard = Controller()
x = 4535
time.sleep(5)
def typechar(string):
    #function for typing characters of a string
    for s in string:
        keyboard.press(s)
        keyboard.release(s)
        time.sleep(0.12) 


def ctrldel():
    #send ctrl-a and delete
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release(Key.ctrl)
    keyboard.release('a')
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

while x < 4550:
    x += 1
    y = str(x)
    e = len(y)
    if e == 1:
        hh = '000' + y
    if e == 2:
        hh == '00' + y
    if e == 3:
        hh = '0' + y
    if e == 4:
        hh = y
    typechar(hh)
    print(hh)
    #screen cords for my monitor, format should be top left to bottom right
#Pressed at (935, 258)left
#Released at (1220, 404)right
    box =(935,258,1120,404) #portaion of screen to grab.
    pilss = ImageGrab.grab(box)
    time.sleep(.5)
    rgb_im = pilss.convert('RGB')
    #determine the rbg value of the 50 50 pxiel
    #from the box selected
    r,g,b = rgb_im.getpixel((50,50))
    print((r, g ,b ))
    if(g >= 250 & b >= 250):
        #if not red
        print("Found! Code is " + hh)
        break;
    ctrldel()
    time.sleep(.5)

        
    
