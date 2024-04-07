import sympy as sp
import numpy as np

def gauss_jordan(A: sp.Matrix, b: sp.Matrix) -> list:
    """
    Resolve o sistema linear Ax = b pelo método de Gauss-Jordan.

    Args:
        A (sp.Matrix): Matriz do sistema linear.
        b (sp.Matrix): Vetor do sistema linear.

    Returns:
        list: Vetor solução do sistema linear.
    """
    n = len(b)
    Ab = sp.Matrix(A.row_join(b))

    for i in range(n):
        # Pivoteamento parcial
        max_index = max(range(i, n), key=lambda j: abs(Ab[j, i]))
        Ab.row_swap(i, max_index)

        # Escalonamento
        for j in range(n):
            if i != j:
                Ab[j, :] = Ab[j, :] - Ab[j, i]/Ab[i, i]*Ab[i, :]

    x = [round(Ab[i, n]/Ab[i, i], 5) for i in range(n)]

    return x

def main():
     ## Exercício 4.1
    input = "inputs/gauss-jordan/exercicio_4.1.txt"
    output = "outputs/gauss-jordan/exercicio_4.1.txt"
    
    ## Exercício 4.6
    # input = "inputs/gauss-jordan/exercicio_4.6.txt"
    # output = "outputs/gauss-jordan/exercicio_4.6.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada == "":
        return None
    else:
        entrada = entrada.split('\n')
        
        matrizB = sp.Matrix(entrada[1].split(' '))
        
        matrizA = sp.Matrix([])
        for i in range(2, len(entrada)):
            matrizA = matrizA.row_insert(i-2, sp.Matrix([entrada[i].split(' ')]))
    
    result = gauss_jordan(matrizA, matrizB)
    
    with open(output, 'w') as file:
        file.write(str(result))
    
if __name__ == "__main__":
    main()