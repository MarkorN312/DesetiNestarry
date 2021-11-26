from PIL import Image
import pytesseract
from PIL import ImageGrab
from pynput.mouse import Listener
import logging
import pyautogui
import argparse
import random
import math

counter = 0
coordinates = []

def setup():
    ap = argparse.ArgumentParser()
    ap.add_argument("-r", "--random", required=False, help="random speed")
    ap.add_argument("-s", "--speed", required=False, help="words per minute")
    print(ap.parse_args())
    return vars(ap.parse_args())

def get_text():
    global coordinates
    im = ImageGrab.grab(bbox=(coordinates))
    im.save("C:/Users/severyn.marek20/Desktop/test.png",'PNG')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\severyn.marek20\Desktop\Tesseract-OCR\tesseract.exe'
    im = Image.open("C:/Users/severyn.marek20/Desktop/test.png")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(text.replace('-', ' ').replace('0', 'o'))
    return text.replace('-', ' ').replace('0', 'o').replace('|', 'l')

def manage_writing():
    text = get_text()
    if(setup()['--speed'] != None):
            time = len(text)/(60*setup()['--speed'])
    while text != '' or text != None:
        if(setup()['--random']):
            time = random.uniform(time - 0.05, time + 0.05)
        pyautogui.write(text, interval=time)
        text = get_text()

def on_click(x, y, button, pressed):
    global counter
    if counter > 1:
        listener.stop()
        print(coordinates)
        manage_writing()
    if pressed:
        coordinates.append(pyautogui.position()[0])
        coordinates.append(pyautogui.position()[1])
        counter += 1

with Listener(on_click=on_click) as listener:
    listener.join()