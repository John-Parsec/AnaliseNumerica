import sympy as sp

def euler(f, h, a, b, y0):
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    
    resultados = []
    
    # adiciona o primeiro valor
    xi = a
    yi = y0
    resultados.append((xi, yi))
    
    # calcula os valores de x e y para cada iteração
    while xi < b:
        yi = (yi + f.subs(x, xi).subs(y, yi)*h).evalf()
        xi += h
        
        resultados.append((xi, yi))
        
    
    return resultados

def main():
    # Exercício 12.3
    input = "inputs/euler/exercicio_12.3.txt"
    output = "outputs/euler/exercicio_12.3.txt"
    
    # Exercício 12.10
    # input = "inputs/euler/exercicio_12.10.txt"
    # output = "outputs/euler/exercicio_12.10.txt"
    
    # Exercício 12.16.1
    # input = "inputs/euler/exercicio_12.16_1.txt"
    # output = "outputs/euler/exercicio_12.16_1.txt"
    
    # Exercício 12.16.2
    # input = "inputs/euler/exercicio_12.16_2.txt"
    # output = "outputs/euler/exercicio_12.16_2.txt" 
        
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
        result = euler(f, amplitude, limite_inf, limite_sup, valor_inicial)
        
        out_file.write(f"Resultado do metodo de Euler\n[\n")
        for i in range(len(result)):
            out_file.write(f"  {i}({result[i][0]:.5f}, {result[i][1]:.5f})")
            if i == len(result) - 1:
                out_file.write(f"\n]")
            else:
                out_file.write(f",")
            if (i + 1) % 4 == 0:
                out_file.write("\n")

if __name__ == "__main__":
    main()