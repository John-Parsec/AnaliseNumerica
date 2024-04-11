import sympy as sp
import numpy as np

def gauss_seidel(matrizA: sp.Matrix, vetorB: sp.Matrix, x0: sp.Matrix, tol: float, maxiter = 1000) -> sp.Matrix:
    """Soluciona um sistema linear utilizando o método de Gauss-Seidel.

    Args:
        matrizA (sp.Matrix): Matriz de coeficientes.
        vetorB (sp.Matrix): Vetor de termos independentes.
        x0 (sp.Matrix): Matriz de variáveis.
        tol (float): Taxa de tolerância.
        maxiter (int, opcional): Maximo de iterações. Default 1000.

    Returns:
        sp.Matrix: Vetor solução do sistema linear.
    """
    n = len(vetorB)
    
    x0 = np.array(x0).astype(float)
    matrizA = np.array(matrizA).astype(float)
    vetorB = np.array(vetorB).astype(float)
    
    for k in range(maxiter):
        x_old = np.copy(x0)
        for i in range(n):
            s1 = sum(matrizA[i, j] * x0[j] for j in range(i))
            s2 = sum(matrizA[i, j] * x_old[j] for j in range(i+1, n))
            x0[i] = (vetorB[i] - s1 - s2) / matrizA[i, i]

        if np.linalg.norm(x0 - x_old) < tol:
            break

    return sp.Matrix(x0)

def main():
    ## Exercício 5.1
    input = "inputs/gauss-seidel/exercicio-5.1.txt"
    output = "outputs/gauss-seidel/exercicio-5.1.txt"
    
    ## Exercício 5.2
    # input = "inputs/gauss-seidel/exercicio-5.2.txt"
    # output = "outputs/gauss-seidel/exercicio-5.2.txt"
    
    ## Exercício 5.5
    # input = "inputs/gauss-seidel/exercicio-5.5.txt"
    # output = "outputs/gauss-seidel/exercicio-5.5.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada == "":
        return None
    else:
        entrada = entrada.split('\n')
        
        have_x0 = entrada[0].split(' ')[0] == 'x0'
        
        if have_x0:
            n = sp.simplify(entrada[1]) 
            x0 = sp.Matrix(entrada[0].split(' ')[1:])
            tol = sp.simplify(entrada[2])
            b = sp.Matrix(entrada[3].split(' '))
        else:
            n = sp.simplify(entrada[0])
            tol = sp.simplify(entrada[1])
            b = sp.Matrix(entrada[2].split(' '))
            x0 = sp.Matrix([0]*n)

        matrizA = sp.Matrix([])        
        for i in range(4, len(entrada)):
            if have_x0:
                matrizA = matrizA.row_insert(i-4, sp.Matrix([entrada[i].split(' ')[0:]]))
            else:
                matrizA = matrizA.row_insert(i-4, sp.Matrix([entrada[i-1].split(' ')[0:]]))
        
        if not have_x0:
            matrizA = matrizA.row_insert(n-1, sp.Matrix([entrada[len(entrada)-1].split(' ')[0:]]))
    
    result = gauss_seidel(matrizA, b, x0, tol, 1000)
    
    result = [round(float(i), 5) for i in result]
        
    with open(output, 'w') as file:
        file.write(str(result))
    
if __name__ == '__main__':
    main()