from collections import deque, namedtuple
from tabulate import tabulate
from colorama import Fore, Style
import tkinter as tk
from tkinter import filedialog, messagebox
import codecs
import os


def limpiar_pantalla():
    # Detecta el sistema operativo y ejecuta el comando adecuado
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y otros sistemas Unix
        os.system('clear')


# Definición de las particiones de memoria
Particion = namedtuple('Particion', ['id', 'inicio', 'tamano', 'id_proceso', 'fragmentacion_interna'])
particiones = [
    Particion(1, 0, 100, None, 0),   # Sistema Operativo
    Particion(2, 100, 250, None, 0), # Trabajos grandes
    Particion(3, 350, 150, None, 0), # Trabajos medianos
    Particion(4, 500, 50, None, 0)   # Trabajos pequeños
]

# Definición de la estructura del proceso
Proceso = namedtuple('Proceso', ['id', 'tamano', 'tiempo_arribo', 'tiempo_irrupcion'])

class Simulador:
    def __init__(self):
        self.cola_listos = deque()
        self.cola_suspendidos = deque()
        self.tiempo_actual = 0
        self.quantum = 3
        self.proceso_cpu = None
        self.tiempo_cpu = 0
        self.contador_procesos = 0
        self.cola_procesos = deque()
        self.multiprogramacion = 0
        #Utulizado para detectar un cambio de estado para saber cúando imprimir las tablas
        self.estado_actual = {
            "particiones": [],
            "cola_listos": [],
            "cola_suspendidos": [],
            "proceso_cpu": None}    
        #Diccionario donde guarda los datos de los procesos
        self.datos_procesos = {}
        #Contador de procesos terminados
        self.trabajos_terminados = 0

    def ha_ocurrido_cambio(self):
        nuevo_estado = {
            "particiones": [(p.id, p.id_proceso) for p in particiones],
            "cola_listos": [p.id for p in self.cola_listos],
            "cola_suspendidos": [p.id for p in self.cola_suspendidos],
            "proceso_cpu": self.proceso_cpu.id if self.proceso_cpu else None}

        if nuevo_estado != self.estado_actual:
            self.estado_actual = nuevo_estado
            return True
        return False

    def ejecutar_simulador(self):
        while self.cola_listos or self.cola_suspendidos or self.proceso_cpu or self.cola_procesos:
            self.admitir_nuevos_procesos()
            
            if not self.proceso_cpu and self.cola_listos:
                self.proceso_cpu = self.cola_listos.popleft()
                self.tiempo_cpu = 0
                print(f"Proceso {self.proceso_cpu.id} asignado a la CPU.")

            if self.proceso_cpu:
                self.tiempo_cpu += 1
                self.proceso_cpu = self.proceso_cpu._replace(tiempo_irrupcion=self.proceso_cpu.tiempo_irrupcion - 1)

                if self.proceso_cpu.tiempo_irrupcion == 0:
                    print(f"Proceso {self.proceso_cpu.id} terminado.")
                    self.trabajos_terminados += 1  
                    self.datos_procesos[self.proceso_cpu.id]["TF"] = self.tiempo_actual + 1
                    self.liberar_memoria(self.proceso_cpu.id)
                    self.proceso_cpu = None
                    self.tiempo_cpu = 0
                    if self.cola_listos:
                        self.proceso_cpu = self.cola_listos.popleft()
                        self.tiempo_cpu = 0
                        print(f"Proceso {self.proceso_cpu.id} asignado a la CPU.")
    

                elif self.tiempo_cpu == self.quantum:
                    print(f"Proceso {self.proceso_cpu.id} interrumpido por el quantum.")
                    self.cola_listos.append(self.proceso_cpu)
                    self.proceso_cpu = None
                    self.tiempo_cpu = 0
                    if self.cola_listos:
                        self.proceso_cpu = self.cola_listos.popleft()
                        self.tiempo_cpu = 0
                        print(f"Proceso {self.proceso_cpu.id} asignado a la CPU.")
                    
            self.tiempo_actual += 1
        self.imprimir_estado()
        self.generar_informe()