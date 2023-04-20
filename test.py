import time, os

tiempo_max = 30
tiempo_inicio = time.time()

import time

def mostrar_tiempo_restante(tiempo_total):
    while tiempo_total:
        minutos, segundos = divmod(tiempo_total, 60)
        tiempo = f"{minutos:02d}:{segundos:02d}"
        os.system("title "+ "Tiempo Restante: " + tiempo)
        time.sleep(1)
        tiempo_total -= 1

mostrar_tiempo_restante(tiempo_max) # 5 minutos
