import sympy as sp

def interpolacao_lagrange(pontos):
    n = len(pontos)
    
    polinomio = 0
    for i in range(n):
        lagrange_i = lagrange(pontos, i)
        
        polinomio += pontos[i].y * lagrange_i
    
    return sp.simplify(sp.sympify(polinomio)).evalf()

def lagrange(pontos, k):
    x = sp.symbols('x')
    
    n = len(pontos)
    
    polinomio = 1
    
    for i in range(n):
        if i != k:
            polinomio *= (x - pontos[i].x)/(pontos[k].x - pontos[i].x)
            
    return polinomio

def main():
    # Exercício 11.1    
    input = "inputs/interpolacao_lagrange/exercicio_10.2.txt"
    output = "outputs/interpolacao_lagrange/exercicio_10.2.txt"
    
    # Exercício 10.9
    input = "inputs/interpolacao_lagrange/exercicio_10.9.txt"
    output = "outputs/interpolacao_lagrange/exercicio_10.9.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
    
    pontos = []
    
    for i in entrada:
        coord = i.split(' ')
        pontos.append(sp.Point(float(coord[0]), float(coord[1])))
    
    with open(output, 'w') as out_file:
        polinimio = interpolacao_lagrange(pontos)
        
        out_file.write(f"f(x) = {polinimio}\n")

if __name__ == "__main__":
    main()


