#!/usr/share/python3

import pyautogui as p
import time

time.sleep(5)
f = open('words.txt')
data = f.readlines()
p.click()

for i in data:
    i = i.strip()
    p.click()
    p.write(i)
    p.press('enter')
    time.sleep(0.5)
