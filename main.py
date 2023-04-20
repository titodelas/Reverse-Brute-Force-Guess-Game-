import random
import time
import os


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

    print("Adivina el número secreto del 1 al", maximo if dificultad == "personalizado" else 200 if dificultad not in [
          "extremo"] else 10, "en un máximo de", intentos_max if intentos_max > 0 else "infinitos" if dificultad != "extremo" else "1", "intentos.")

    def mostrar_tiempo_restante(tiempo_total):
        while tiempo_total:
            minutos, segundos = divmod(tiempo_total, 60)
            tiempo = f"{minutos:02d}:{segundos:02d}"
            os.system("title " + "Tiempo Restante: " + tiempo)
            time.sleep(1)
            tiempo_total -= 1

        mostrar_tiempo_restante(tiempo_max)

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


dificultad = input("""
                                      Selecciona la dificultad 
                ╔═══════════════════════════════════════════════════════════════════════╗
                ║   facil            > 10 Intentos | 1 - 50  | 100 puntos | 30 segundos ║
                ║   medio            > 7 Intentos  | 1 - 100 | 150 puntos | 60 segundos ║
                ║   dificil          > 5 Intentos  | 1 - 150 | 200 puntos | 90 segundos ║
                ║   infinito         > ∞ Intentos  | 1 - 200 |     --     | ∞ segundos  ║
                ║   extremo          > 1 Intento   | 1 - 10  |     --     | 10 segundos ║
                ║   personalizada    > Intentos, Rango y Tiempo personalizable          ║
                ╚═══════════════════════════════════════════════════════════════════════╝
                
                                    Introduce tu dificultat >> """)
adivinanza(dificultad)
