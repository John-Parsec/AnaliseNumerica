import matplotlib.pyplot as plt

def plot(data: list[(float, float)], output: str, label: str):
    x_data = [data[i][0] for i in range(len(data))]
    y_data = [data[i][1] for i in range(len(data))]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, marker='o', linestyle='-', color='b', label=label)
    plt.title('Resultado do ' + label)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.savefig(output)