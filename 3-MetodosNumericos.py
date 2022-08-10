from cmath import sqrt
from math import e, log
import matplotlib.pyplot as plt
import numpy as np

t = int(input("Valor de t en el intervalo inferior: "))
intervalo_superior = int(input("Valor de t en el intervalo superior: "))
y = int(input("Valor de y en la condición inicial: "))
h = float(input("Valor de h: "))
metodo = ""
t_puntos = []
y_puntos_aprox = []
y_puntos_teoricos = []
t_map = np.linspace(0, 1, 100000)
ecuacion_diferencial = input("Escribe la ecuación diferencial de primer grado (con y' despejada): ")
ecuacion_solucion = input("Escribe la ecuación solución: ")
variables_ecuacion = {"pow": pow, "e": e, "sqrt": sqrt, "log": log, "sin": sin, "cos": cos, "tan". tan}
pasos = int((intervalo_superior - t) / h)


def solucion(t):
    variables_ecuacion["t"] = t
    y = eval(ecuacion_solucion, variables_ecuacion)
    return y

def f(t, y):
    variables_ecuacion["t"] = t
    variables_ecuacion["y"] = y
    z = eval(ecuacion_diferencial, variables_ecuacion)
    return z

def evaluar(t, y, h):
    for i in range(pasos):
        t = round(t + h, 2)
        y = round(solucion(t), 4)
        inserta_datos(t, y , t_puntos, y_puntos_teoricos)

def euler(t, y, h): 
    metodo = "Euler"
    for i in range(pasos):
        y = y + h*f(t, y)
        t = round(t + h, 2)
        t_puntos = []
        inserta_datos(t, y, t_puntos, y_puntos_aprox)

def euler_mejorado(t, y, h):
    metodo = "Euler mejorado"
    for i in range(pasos):
        y_asterisco = y + h*f(t,y)
        t_siguiente = round(t + h, 2)
        y = y + h*((f(t,y)+ f(t_siguiente, y_asterisco))/(2))
        t = round(t + h, 2)
        t_puntos = []
        inserta_datos(t, y, t_puntos, y_puntos_aprox)
        
def runge_kutta_4(t, y, h):
    metodo = "Runge Kutta de Orden 4"
    for i in range(pasos):
        k_1 = f(t, y)
        k_2 = f((t + 0.5*h), (y + 0.5*h*k_1))
        k_3 = f((t + 0.5*h), (y + 0.5*h*k_2))
        k_4 = f((t + h), (y + h*k_3))
        y = y + (h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
        t = round(t + h, 2)
        t_puntos = []
        inserta_datos(t, y, t_puntos, y_puntos_aprox)

def inserta_datos(t, y, t_array, y_array):
    t_array.append(round(t,4))
    y_array.append(round(y,4))

def seleccionar_metodo():
    func_name = input("""\nEscribe el nombre del método númerico a usar:
    Euler = euler
    Euler mejorado = euler_mejorado
    Runge Kutta de Orden 4 = runge_kutta_4
    """)
    evaluar(t, y, h)
    argsdict = {'t': t, 'y': y, 'h': h}
    globals()[func_name](**argsdict)


fig, ax = plt.subplot_mosaic([['left', 'right'],['left', 'right']], layout='constrained')

def definir_grafica(metodo):
    ax['right'].set_xlabel('Eje t')
    ax['right'].set_ylabel('Eje y')
    ax['right'].set_title("Métodos Numéricos - " + metodo)
    ax['right'].plot(t_map, solucion(t_map), label='Solución teórica', color='red')
    ax['right'].plot(t_puntos, y_puntos_teoricos, 'o', label='Puntos teóricos', color='blue')
    ax['right'].plot(t_puntos, y_puntos_aprox, 'o', label='Puntos aproximados', color='lime')
    ax['right'].legend()

def definir_tabla():
    ax['left'].axis('off')
    ax['left'].axis('tight')
    cell_text = []
    n_rows = len(y_puntos_aprox)
    for i in range(n_rows):
        row_data = [y_puntos_teoricos[i], y_puntos_aprox[i]]
        cell_text.append(row_data)
    the_table = ax['left'].table(cellText=cell_text,
                      rowLabels=t_puntos,
                      rowColours=None,
                      colLabels=["Teórico","Aproximado"],
                      loc='center')


seleccionar_metodo()
definir_grafica(metodo)
definir_tabla()
plt.show()



