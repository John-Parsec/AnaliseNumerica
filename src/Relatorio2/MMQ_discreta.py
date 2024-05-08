import random
import sympy as sp
from typing import TextIO

def aproximacao_polinomial_MMQ_discreta(pontos: list[sp.Point], degree: int = None, file: TextIO = None) -> sp.Matrix:
    """Aproximação polinomial por MMQ discreta

    Args:
        pontos (list[sp.Point]): Lista de pontos
        degree (int, optional): Grau do polinomio. Default None.
        file (TextIO, optional): Arquivo de saída. Default None.

    Returns:
        sp.Matrix: Vetor de coeficientes
    """
    n = len(pontos)
    
    if degree is not None:
        # Define numeros aleatorios para a amostra
        random_indexes = random.sample(range(n), degree+2)
        random_indexes.sort()
        pontos = [pontos[i] for i in random_indexes]
    
    n = len(pontos)
    
    mat_UU = sp.zeros(n-1, n-1)
    vet_yU = sp.zeros(n-1, 1)
    vet_U = []
    
    vet_a = sp.Matrix([])   # vetor de simbolos
    for i in range(n-1):
        name = 'x' + str(i)
        vet_a = vet_a.row_insert(i, sp.Matrix([sp.symbols(name)]))
    
    vet_y = sp.zeros(n, 1)
    vet_x = sp.zeros(n, 1)
    for i in range(n):
        vet_y[i, 0] = pontos[i].y
        vet_x[i, 0] = pontos[i].x
    
    # matrizes U
    vet_U.append(sp.ones(n, 1))
    for i in range(1, n):
        vet_U.append(vet_U[i-1].copy())
        for j in range(n):
            vet_U[i][j, 0] *= vet_x[j, 0]
    
    if file:        
        # Printa a matriz U
        file.write("Matriz U:\n")
        for i in range(n):
            for j in range(n):
                file.write(f"{vet_U[i][j, 0]} ")
            file.write("\n")
            
        file.write("\n")
    
    # matrizUU
    for i in range(n-1):
        for j in range(n-1):
            if (i > j):
                mat_UU[i, j] = mat_UU[j, i]
            else:
                mat_UU[i, j] = vet_U[i].dot(vet_U[j]) # produto interno
        # vetor yU
        vet_yU[i, 0] = vet_y.dot(vet_U[i])
    
    if file:
        # Printa a matriz UU
        file.write("Matriz UU:\n")
        for i in range(n-1):
            for j in range(n-1):
                file.write(f"{mat_UU[i, j]} ")
            file.write("\n")
        
        file.write("\n")
    
    return resolve_sistema(mat_UU, vet_yU, vet_a)

# Resolve o sistema de matrizes
def resolve_sistema(matrizA, matrizB, matrizX):
    """Resolve o sistema de matrizes

    Args:
        matrizA (sp.Matrix): Matriz A
        matrizB (sp.Matrix): Matriz B
        matrizX (sp.Matrix): Matriz X

    Returns:
        sp.Matrix: Matriz solução
    """
    n = sp.shape(matrizA)[0]
    variaveis = sp.symbols('x0:%d' % n)
    
    solucao = sp.solve(matrizA*matrizX - matrizB, variaveis)
    
    matriz_solucao = sp.Matrix([])
    for i in range(n):
        matriz_solucao = matriz_solucao.row_insert(i, sp.Matrix([solucao[variaveis[i]]]))

    return matriz_solucao

def main():
    # Exercício 8.1
    input = "inputs/MMQ_discreta/exercicio_8.1.txt"
    output = "outputs/MMQ_discreta/exercicio_8.1.txt"
    
    # Exercício 8.5
    #input = "inputs/MMQ_discreta/exercicio_8.5.txt"
    #output = "outputs/MMQ_discreta/exercicio_8.5.txt"
    
    # Exercício 10.6
    #input = "inputs/MMQ_discreta/exercicio_10.6.txt"
    # output = "outputs/MMQ_discreta/exercicio_10.6_2.txt"
    
    random.seed(1)    
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
    
    if len(entrada[0].split(' ')[0]) == 1:
        degree = int(entrada[0])
    else:
        degree = None
        
    entrada = entrada[1:]
    
    pontos = []
    for i in entrada:
        coord = i.split(' ')
        pontos.append(sp.Point(float(coord[0]), float(coord[1])))   
    
    
    with open(output, 'w') as out_file:
        coeficiente_a = aproximacao_polinomial_MMQ_discreta(pontos, degree, out_file)
        size = len(coeficiente_a)
        
        # polinimo
        for i in range(size):
            if i == size-1:
                out_file.write(f"{coeficiente_a[i, 0]}x^{i})\n\n")
            elif i == 0:
                out_file.write(f"f(x) = {coeficiente_a[i, 0]} + (")
            else:
                out_file.write(f"{coeficiente_a[i, 0]}x^{i}) + (")
        
        # coeficientes
        for i in range(size):
            out_file.write(f"a{i} = {coeficiente_a[i, 0]}\n")

if __name__ == "__main__":
    main()