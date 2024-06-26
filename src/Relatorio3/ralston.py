import sympy as sp

def ralston(f, h, a, b, y0):
    x = sp.Symbol('x')
    y = sp.Symbol('y')

    results = []
    
    # adiciona o primeiro valor
    xi = a
    yi = y0
    results.append((xi, yi))
    
    # calcula os valores de x e y para cada iteração
    while xi < b:
        k1 = f.subs(x, xi).subs(y, yi).evalf()
        k2 = f.subs(x, xi + (h*3/4)).subs(y, yi + (k1*h*3/4)).evalf()
        yi = yi + (k1/3 + (k2*2/3))*(h)
        xi += h
        results.append((xi, yi))
    
    return results

def main():
    # Exercício 12.3
    input = "inputs/ralston/exercicio_12.3.txt"
    output = "outputs/ralston/exercicio_12.3.txt"
    
    # Exercício 12.10
    # input = "inputs/ralston/exercicio_12.10.txt"
    # output = "outputs/ralston/exercicio_12.10.txt"
    
    # Exercício 12.16.1
    # input = "inputs/ralston/exercicio_12.16_1.txt"
    # output = "outputs/ralston/exercicio_12.16_1.txt"
    
    # Exercício 12.16.2
    # input = "inputs/ralston/exercicio_12.16_2.txt"
    # output = "outputs/ralston/exercicio_12.16_2.txt" 
        
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
        results = ralston(f, amplitude, limite_inf, limite_sup, valor_inicial)
        
        out_file.write(f"Resultado do metodo de Ralston:\n[\n")
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