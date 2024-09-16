import pyautogui
import time
import random
import os
import argparse

lista = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", 
         "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", 
         "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve", "treinta"]

# Argumentos del script
parser = argparse.ArgumentParser(description="Script para escribir palabras y opcionalmente apagar la PC")
parser.add_argument("-sd", "--shutdown", action="store_true", help="Apagar la PC después de ejecutar el script")
args = parser.parse_args()

time.sleep(3)

for palabra in lista:
    palabra = palabra + " " + random.choice(lista)
    for letra in palabra:
        pyautogui.press(letra)
        time.sleep(0.08)
    pyautogui.press('enter')
    time.sleep(4)

if args.shutdown:
    print("Apagando la PC...")
    os.system("shutdown /s /t 1") 

