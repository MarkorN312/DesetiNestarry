from PIL import Image
import pytesseract
from PIL import ImageGrab
from pynput.mouse import Listener
import logging
import pyautogui

counter = 0
coordinates = []

def get_text():
    global coordinates
    im=ImageGrab.grab(bbox=(coordinates))
    im.save("C:/Users/severyn.marek20/Desktop/test.png",'PNG')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\severyn.marek20\Desktop\Tesseract-OCR\tesseract.exe'
    im = Image.open("C:/Users/severyn.marek20/Desktop/test.png")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(text.replace('-', ' ').replace('0', 'o'))
    return text.replace('-', ' ').replace('0', 'o').replace('|', 'l')

def on_click(x, y, button, pressed):
    global counter
    if counter > 1:
        listener.stop()
        print(coordinates)
        text = get_text()
        pyautogui.write(text[0:len(text) - 10], interval=0.025)
    if pressed:
        coordinates.append(pyautogui.position()[0])
        coordinates.append(pyautogui.position()[1])
        counter += 1

with Listener(on_click=on_click) as listener:
    listener.join()
