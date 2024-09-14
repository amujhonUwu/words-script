import pyautogui
import time
import random

lista = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once","doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", 
         "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", 
         "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve", "treinta"]

time.sleep(3)

for palabra in lista:
    palabra = palabra + " " + random.choice(lista)
    for letra in palabra:
        pyautogui.press(letra)
        time.sleep(0.08)
    pyautogui.press('enter')
    time.sleep(4)
