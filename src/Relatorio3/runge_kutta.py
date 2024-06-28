import sympy as sp
from plot import plot

def runge_kutta_terceira_ordem(f: sp.Expr, h: float, a: float, b: float, y0: float) -> list[(float, float)]:
    """Calcula a solução de uma equação diferencial ordinária de primeira ordem pelo método de Runger-Kutta.

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

    results = []
    
    # adiciona o primeiro valor
    xi = a
    yi = y0
    results.append((xi, yi))
    
    # calcula os valores de x e y para cada iteração
    while xi < b:
        k1 = f.subs({x: xi, y: yi}).evalf()
        k2 = f.subs({x: xi + h / 2, y: yi + (h / 2) * k1}).evalf()
        k3 = f.subs({x: xi + h, y: yi - h * k1 + 2 * h * k2}).evalf()
        yi = yi + (k1 + 4 * k2 + k3) * (h / 6)
        xi += h
        results.append((xi, yi))
    
    return results

def runge_kutta_quarta_ordem(f: sp.Expr, h: float, a: float, b: float, y0: float) -> list[(float, float)]:
    """Calcula a solução de uma equação diferencial ordinária de primeira ordem pelo método de Runger-Kutta.

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

    results = []
    
    # adiciona o primeiro valor
    xi = a
    yi = y0
    results.append((xi, yi))
    
    # calcula os valores de x e y para cada iteração
    while xi < b:
        meioh = h/2
        k1 = f.subs(x, xi).subs(y, yi).evalf()
        k2 = f.subs(x, xi + meioh).subs(y, yi + (meioh*k1)).evalf()
        k3 = f.subs(x, xi + meioh).subs(y, yi + meioh*k2).evalf()
        k4 = f.subs(x, xi + h).subs(y, yi + h*k3).evalf()
        yi = yi + (k1 + 2*k2+2*k3+k4)*(h/6)
        xi += h
        results.append((xi, yi))
    
    return results

def main():
    # Exercício 12.3
    input = "inputs/runge_kutta/exercicio_12.3.txt"
    output = "outputs/runge_kutta/exercicio_12.3.txt"
    
    # Exercício 12.10
    # input = "inputs/runge_kutta/exercicio_12.10.txt"
    # output = "outputs/runge_kutta/exercicio_12.10.txt"
    
    # Exercício 12.16.1
    # input = "inputs/runge_kutta/exercicio_12.16_1.txt"
    # output = "outputs/runge_kutta/exercicio_12.16_1.txt"
    
    # Exercício 12.16.2
    # input = "inputs/runge_kutta/exercicio_12.16_2.txt"
    # output = "outputs/runge_kutta/exercicio_12.16_2.txt" 
        
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
    
    results_terceira_ordem = runge_kutta_terceira_ordem(f, amplitude, limite_inf, limite_sup, valor_inicial) 
    results_quarta_ordem = runge_kutta_quarta_ordem(f, amplitude, limite_inf, limite_sup, valor_inicial)
        
    with open(output, 'w') as out_file:
        out_file.write(f"Resultado do metodo de Runge-Kutta Terceira Ordem:\n[\n")
        for i in range(len(results_terceira_ordem)):
            out_file.write(f"  {i}({results_terceira_ordem[i][0]:.5f}, {results_terceira_ordem[i][1]:.5f})")
            if i == len(results_terceira_ordem) - 1:
                out_file.write(f"\n]")
            else:
                out_file.write(f",")
            if (i + 1) % 4 == 0:
                out_file.write("\n")
        
        out_file.write(f"\n\nResultado do metodo de Runge-Kutta Quarta Ordem:\n[\n")
        for i in range(len(results_quarta_ordem)):
            out_file.write(f"  {i}({results_quarta_ordem[i][0]:.5f}, {results_quarta_ordem[i][1]:.5f})")
            if i == len(results_quarta_ordem) - 1:
                out_file.write(f"\n]")
            else:
                out_file.write(f",")
            if (i + 1) % 4 == 0:
                out_file.write("\n")
                
    # plota e salva o gráfico dos resultados
    output_terceira_ordem = output.replace('.txt', '_terceira_ordem.png')
    output_quarta_ordem = output.replace('.txt', '_quarta_ordem.png')
    plot(results_terceira_ordem, output_terceira_ordem, 'Método de Runge-Kutta Terceira Ordem')
    plot(results_quarta_ordem, output_quarta_ordem, 'Método de Runge-Kutta Quarta Ordem')

if __name__ == "__main__":
    main()