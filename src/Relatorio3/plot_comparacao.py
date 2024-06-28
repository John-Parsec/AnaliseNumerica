import sympy as sp
import matplotlib.pyplot as plt
from euler import euler
from euler_modificado import euler_modificado
from heun import heun
from ralston import ralston
from runge_kutta import runge_kutta_terceira_ordem, runge_kutta_quarta_ordem

def plot_all(data: list[(float, float)], output: str, labels: list):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
    
    for i in range(6):
        x, y = zip(*data[i])
        ax.plot(x, y, label=labels[i], color=colors[i])
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend()
    
    plt.savefig(output)

def plot_all_side(data: list[(float, float)], output: str, labels: list[str]):
    fig, ax = plt.subplots(2, 3, figsize=(10, 6), sharey=True)
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
    
    for i in range(len(data)):
        x, y = zip(*data[i])
        ax[i // 3, i % 3].plot(x, y, label=labels[i], color=colors[i])
        ax[i // 3, i % 3].set_title(f'Método de {labels[i]}')
        ax[i // 3, i % 3].set_xlabel('x')
        ax[i // 3, i % 3].grid(True)
    
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
results.append(runge_kutta_terceira_ordem(f, amplitude, limite_inf, limite_sup, valor_inicial))
results.append(runge_kutta_quarta_ordem(f, amplitude, limite_inf, limite_sup, valor_inicial))

plot_all(results, "outputs/exercicio_12.10_comparacao.png", ["Euler", "Euler Modificado", "Heun", "Ralston", "Runge-Kutta 3ª Ordem", "Runge-Kutta 4ª Ordem"])
plot_all_side(results, "outputs/exercicio_12.10_comparacao_lado-a-lado.png", ["Euler", "Euler Modificado", "Heun", "Ralston", "Runge-Kutta 3ª Ordem", "Runge-Kutta 4ª Ordem"])