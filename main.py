import pyautogui
import time
import random
import os
import argparse

# Lista de palabras
lista = [
    "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", 
    "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", 
    "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", 
    "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve", "treinta"
]

# Valores predeterminados
DEFAULT_TIEMPO_ENTRE_PALABRA = 3
DEFAULT_TIEMPO_ENTRE_LETRA = 0.08

# Función principal para lanzar palabras
def lanzar_palabras(tiempo_entre_letra, tiempo_entre_palabra, celular=False):
    """
    Función que escribe palabras de una lista en un campo de texto,
    con la opción de simular clics si se ejecuta en un celular.
    """
    for palabra in lista:
        palabra = " " + palabra + " " + random.choice(lista)

        if celular:
            pyautogui.click(1700, 119)

        for letra in palabra:
            pyautogui.press(letra)
            time.sleep(tiempo_entre_letra)

        pyautogui.press('enter')
        time.sleep(tiempo_entre_palabra)

        if celular:
            pyautogui.click(1700, 119)
            time.sleep(1.2)
            pyautogui.click(1855, 119)
            time.sleep(0.5)

# Argumentos del script
parser = argparse.ArgumentParser(description="Script para escribir palabras y opcionalmente apagar la PC")
parser.add_argument("-sd", "--shutdown", action="store_true", help="Apagar la PC después de ejecutar el script")
parser.add_argument("-cell", "--cellphone", action="store_true", help="El script se ejecutará en el celular")
parser.add_argument("-all", "--all", action="store_true", help="El script se ejecutará en computadora y luego en celular")
args = parser.parse_args()

# Pausa inicial
time.sleep(3)

# Lógica de ejecución según los argumentos
if args.cellphone:
    lanzar_palabras(DEFAULT_TIEMPO_ENTRE_LETRA, 4, celular=True)

elif args.all:
    lanzar_palabras(DEFAULT_TIEMPO_ENTRE_LETRA, DEFAULT_TIEMPO_ENTRE_PALABRA)
    lanzar_palabras(DEFAULT_TIEMPO_ENTRE_LETRA, 4, celular=True)

else:
    lanzar_palabras(DEFAULT_TIEMPO_ENTRE_LETRA, DEFAULT_TIEMPO_ENTRE_PALABRA)

# Opción de apagar la PC
if args.shutdown:
    print("Apagando la PC...")
    os.system("shutdown /s /t 1")
