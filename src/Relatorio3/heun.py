import sympy as sp

def heun(expressao, h, a, b, y0):
    x = sp.Symbol('x')
    y = sp.Symbol('y')

    results = []
    
    # adiciona o primeiro valor
    xi = a
    yi = y0
    results.append((xi, yi))
    
    # calcula os valores de x e y para cada iteração
    while xi < b:
        k = expressao.subs(x, xi).subs(y, yi).evalf()
        k1 = expressao.subs(x, xi + h).subs(y, yi + k*h).evalf()
        yi = yi + (k + k1)*(h/2)
        xi += h
        results.append((xi, yi))
    
    return results

def main():
    # Exercício 12.3
    input = "inputs/heun/exercicio_12.3.txt"
    output = "outputs/heun/exercicio_12.3.txt"
    
    # Exercício 12.10
    # input = "inputs/heun/exercicio_12.10.txt"
    # output = "outputs/heun/exercicio_12.10.txt"
    
    # Exercício 12.16.1
    # input = "inputs/heun/exercicio_12.16_1.txt"
    # output = "outputs/heun/exercicio_12.16_1.txt"
    
    # Exercício 12.16.2
    # input = "inputs/heun/exercicio_12.16_2.txt"
    # output = "outputs/heun/exercicio_12.16_2.txt" 
        
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
        results = heun(f, amplitude, limite_inf, limite_sup, valor_inicial)
        
        out_file.write(f"Resultsado do metodo de Heun:\n[\n")
        for i in range(len(results)):
            out_file.write(f"  {i}({results[i][0]:.5f}, {results[i][1]:.5f})")
            if i == len(results) - 1:
                out_file.write(f"\n]")
            else:
                out_file.write(f",")
            if (i + 1) % 4 == 0:
                out_file.write("\n")


if __name__ == "__main__":
    main()