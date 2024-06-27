import sympy as sp
import matplotlib.pyplot as plt
from euler import euler
from euler_modificado import euler_modificado
from heun import heun
from ralston import ralston
from runge_kutta import runge_kutta

def plot_all(data: list[(float, float)], output: str, labels: list):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x, y = zip(*data[0])
    ax.plot(x, y, label=labels[0])
    
    x, y = zip(*data[1])
    ax.plot(x, y, label=labels[1], color='orange')
    
    x, y = zip(*data[2])
    ax.plot(x, y, label=labels[2], color='green')
    
    x, y = zip(*data[3])
    ax.plot(x, y, label=labels[3], color='red')
    
    x, y = zip(*data[4])
    ax.plot(x, y, label=labels[4], color='purple')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend()
    
    plt.savefig(output)

def plot_all_side(data: list[(float, float)], output: str, labels: list[str]):
    fig, ax = plt.subplots(2, 3, figsize=(10, 6), sharey=True)
    
    x, y = zip(*data[0])
    ax[0, 0].plot(x, y, label=labels[0])
    ax[0, 0].set_title('Método de Euler')
    ax[0, 0].set_xlabel('x')
    ax[0, 0].set_ylabel('y')
    ax[0, 0].grid(True)
    
    x, y = zip(*data[1])
    ax[0, 1].plot(x, y, label=labels[1], color='orange')
    ax[0, 1].set_title('Método de Euler Modificado')
    ax[0, 1].set_xlabel('x')
    ax[0, 1].grid(True)
    
    x, y = zip(*data[2])
    ax[0, 2].plot(x, y, label=labels[2], color='green')
    ax[0, 2].set_title('Método de Heun')
    ax[0, 2].set_xlabel('x')
    ax[0, 2].grid(True)
    
    x, y = zip(*data[3])
    ax[1, 0].plot(x, y, label=labels[3], color='red')
    ax[1, 0].set_title('Método de Ralston')
    ax[1, 0].set_xlabel('x')
    ax[1, 0].set_ylabel('y')
    ax[1, 0].grid(True)
    
    x, y = zip(*data[4])
    ax[1, 1].plot(x, y, label=labels[4])
    ax[1, 1].set_title('Método de Runge-Kutta', color='purple')
    ax[1, 1].set_xlabel('x')
    ax[1, 1].grid(True)
    
    ax[1, 2].axis('off')
    fig.tight_layout()
    
    
    plt.savefig(output)

results = []

with open("inputs/euler/exercicio_12.10.txt", 'r') as file:
    entrada = file.read()

entrada = entrada.split('\n')

f = sp.sympify(entrada[0])
amplitude = float(entrada[1])

limite_inf, limite_sup = entrada[2].split(' ')
limite_inf = float(limite_inf)
limite_sup = float(limite_sup)

valor_inicial = float(entrada[3])

results.append(euler(f, amplitude, limite_inf, limite_sup, valor_inicial))
results.append(euler_modificado(f, amplitude, limite_inf, limite_sup, valor_inicial))
results.append(heun(f, amplitude, limite_inf, limite_sup, valor_inicial))
results.append(ralston(f, amplitude, limite_inf, limite_sup, valor_inicial))
results.append(runge_kutta(f, amplitude, limite_inf, limite_sup, valor_inicial))

plot_all(results, "outputs/exercicio_12.10_comparacao.png", ["Euler", "Euler Modificado", "Heun", "Ralston", "Runge-Kutta"])
plot_all_side(results, "outputs/exercicio_12.10_comparacao_lado-a-lado.png", ["Euler", "Euler Modificado", "Heun", "Ralston", "Runge-Kutta"])