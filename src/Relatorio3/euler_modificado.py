import sympy as sp
from plot import plot

def euler_modificado(f: sp.Expr, h: float, a: float, b: float, y0: float) -> list[(float, float)]:
    """Calcula a solução de uma equação diferencial ordinária de primeira ordem pelo método de Euler Modificado.

    Args:
        f (sp.Expr): Expressão da função f(x, y)
        h (float): Tamanho do passo
        a (float): Limite inferior do intervalo
        b (float): Limite superior do intervalo
        y0 (float): Valor inicial de y

    Returns:
        list[(float, float)]: Lista de tuplas (x, y) com os valores de x e y para cada iteração
    """
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    yi_2 = sp.Symbol('y')
    
    results = []
    
    # adiciona o primeiro valor
    xi = a
    yi = y0
    results.append((xi, yi))
    
    # calcula os valores de x e y para cada iteração
    while xi < b:
        yi_2 = (yi + f.subs(x, xi).subs(y, yi)*h/2)
        f = f.subs(x, xi + h/2).subs(y, yi_2)
        yi = (yi + f*h).evalf()
        xi += h
        results.append((xi, yi))
    
    return results

def main():
    # Exercício 12.3
    input = "inputs/euler_modificado/exercicio_12.3.txt"
    output = "outputs/euler_modificado/exercicio_12.3.txt"
    
    # Exercício 12.10
    # input = "inputs/euler_modificado/exercicio_12.10.txt"
    # output = "outputs/euler_modificado/exercicio_12.10.txt"
    
    # Exercício 12.16.1
    # input = "inputs/euler_modificado/exercicio_12.16_1.txt"
    # output = "outputs/euler_modificado/exercicio_12.16_1.txt"
    
    # Exercício 12.16.2
    # input = "inputs/euler_modificado/exercicio_12.16_2.txt"
    # output = "outputs/euler_modificado/exercicio_12.16_2.txt" 
        
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
        
    if len(entrada) != 4:
        print("Entrada invalida")
        return
    
    f = sp.sympify(entrada[0])
    amplitude = float(entrada[1])
    
    limite_inf, limite_sup = entrada[2].split(' ')
    limite_inf = float(limite_inf)
    limite_sup = float(limite_sup)
    
    if limite_inf >= limite_sup:
        print("Entrada invalida")
        return
    
    valor_inicial = float(entrada[3])
    
    with open(output, 'w') as out_file:    
        results = euler_modificado(f, amplitude, limite_inf, limite_sup, valor_inicial)
        
        out_file.write(f"Resultado do metodo de Euler Modificado:\n[\n")
        for i in range(len(results)):
            out_file.write(f"  {i}({results[i][0]:.5f}, {results[i][1]:.5f})")
            if i == len(results) - 1:
                out_file.write(f"\n]")
            else:
                out_file.write(f",")
            if (i + 1) % 4 == 0:
                out_file.write("\n")
    
    # plota e salva o gráfico dos resultados
    # plot(results, output.replace('.txt', '.png'), 'Método de Euler Modificado')

if __name__ == "__main__":
    main()