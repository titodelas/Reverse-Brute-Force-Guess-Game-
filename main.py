import random
import time
import os
import fade
from colorama import *
init(autoreset=True)

def adivinanza(dificultad):
    # Añadimos un menu de dificultades
    if dificultad == "facil":
        numero = random.randint(1, 50)
        intentos_max = 5
        tiempo_max = 30
    elif dificultad == "medio":
        numero = random.randint(1, 100)
        intentos_max = 7
        tiempo_max = 60
    elif dificultad == "dificil":
        numero = random.randint(1, 150)
        intentos_max = 10
        tiempo_max = 90
    elif dificultad == "personalizado":
        print("Introduce el rango máximo del número a adivinar:")
        maximo = int(input())
        numero = random.randint(1, maximo)
        print("Introduce el número máximo de intentos:")
        intentos_max = int(input())
        tiempo_max = 0
    elif dificultad == "infinito":
        numero = random.randint(1, 200)
        intentos_max = 0
        tiempo_max = 0
    elif dificultad == "extremo":
        numero = random.randint(1, 10)
        intentos_max = 1
        tiempo_max = 10
    else:
        print("Dificultad no válida.")
        return

    intentos = 0
    puntos = 0
    tiempo_inicio = time.time()

    print(f"{Fore.RESET}Adivina el número secreto del 1 al", maximo if dificultad == "personalizado" else 200 if dificultad not in [
          "extremo"] else 10, "en un máximo de", intentos_max if intentos_max > 0 else "infinitos" if dificultad != "extremo" else "1", "intentos.")

    while True:
        intentos += 1
        if intentos > intentos_max and intentos_max > 0:
            print("Te has quedado sin intentos. El número secreto era", numero)
            if dificultad == "extremo":
                print("Se apagará el ordenador en 3 segundos.")
                time.sleep(3)
                # Te apaga el ordenador si fallas
                os.system("shutdown /s /t 0")
            break

        if tiempo_max > 0 and (time.time() - tiempo_inicio) > tiempo_max:
            print("Se ha agotado el tiempo. El número secreto era", numero)
            break

        intento = int(input("Intento #" + str(intentos) + ": "))

        if intento == numero:
            print("¡Acertaste el número en", intentos, "intentos!")
            if intentos <= intentos_max and puntos > 0:
                print("Ganaste", puntos, "puntos.")
            break
        elif intento < numero:
            print("El número secreto es más grande.")
        else:
            print("El número secreto es más pequeño.")

        if dificultad not in ["personalizado", "infinito", "extremo"]:
            puntos -= 10
            if intentos == intentos_max:
                puntos -= 20
            elif intentos == int(intentos_max/2):
                puntos += 10
            elif intentos == int(intentos_max/4):
                puntos += 20

            if puntos < 0:
                puntos = 0
                print("Tienes", puntos, "puntos")

os.system('cls')
print(fade.pinkred("""

8888888888 888             888888 888     888 8888888888 .d8888b.   .d88888b.  
888        888               "88b 888     888 888       d88P  Y88b d88P" "Y88b 
888        888                888 888     888 888       888    888 888     888 
8888888    888                888 888     888 8888888   888        888     888 
888        888                888 888     888 888       888  88888 888     888 
888        888                888 888     888 888       888    888 888     888 
888        888                88P Y88b. .d88P 888       Y88b  d88P Y88b. .d88P 
8888888888 88888888           888  "Y88888P"  8888888888 "Y8888P88  "Y88888P"  
                            .d88P                                              
                          .d88P"       github.com/titodelas                                         
                         888P"                                                 

                        Selecciona la dificultad 
╔═══════════════════════════════════════════════════════════════════════╗
║   facil            > 10 Intentos | 1 - 50  | 100 puntos | 30 segundos ║
║   medio            > 7 Intentos  | 1 - 100 | 150 puntos | 60 segundos ║
║   dificil          > 5 Intentos  | 1 - 150 | 200 puntos | 90 segundos ║
║   infinito         > ∞ Intentos  | 1 - 200 |     --     | ∞ segundos  ║
║   extremo          > 1 Intento   | 1 - 10  |     --     | 10 segundos ║
║   personalizada    > Intentos, Rango y Tiempo personalizable          ║
╚═══════════════════════════════════════════════════════════════════════╝"""))
dificultad = input(f'{Fore.RED}Introduce tu dificultat >> ')

adivinanza(dificultad)
