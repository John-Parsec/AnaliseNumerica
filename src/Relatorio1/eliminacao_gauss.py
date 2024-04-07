import sympy as sp
import numpy as np

def eliminacao_de_gauss(matrizA, matrizB) -> np.array:
    matrizA = np.array(matrizA)
    matrizB = np.array(matrizB)
    n = matrizB.shape[0]

    # Eliminação gaussiana
    for i in range(n):
        for j in range(i + 1, n):
            factor = matrizA[j][i] / matrizA[i][i]
            matrizA[j][i:] = matrizA[j][i:] - (factor * matrizA[i][i:])
            matrizB[j] = matrizB[j] - (factor * matrizB[i])

    # Substituição regressiva
    matrizX = np.zeros(n)
    for i in range(n - 1, -1, -1):
        matrizX[i] = (matrizB[i] - np.dot(matrizA[i][i + 1:], matrizX[i + 1:])) / matrizA[i][i]

    return matrizX

def main():
    ## Exercício 4.1
    input = "inputs/eliminacao_gauss/exercicio_4.1.txt"
    output = "outputs/eliminacao_gauss/exercicio_4.1.txt"
    
    ## Exercício 4.6
    # input = "inputs/eliminacao_gauss/exercicio_4.6.txt"
    # output = "outputs/eliminacao_gauss/exercicio_4.6.txt"
    
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
    
    with open(output, 'w') as file:
        result = eliminacao_de_gauss(matrizA, matrizB)
        
        result = [round(float(i), 5) for i in result]
        
        file.write(str(result))
    
if __name__ == "__main__":
    main()