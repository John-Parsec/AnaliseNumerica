import sympy as sp
import numpy as np

def eliminacao_de_gauss(matrizA: np.ndarray, matrizB: np.ndarray) -> np.ndarray:
    """Resolve um sistema de equações lineares utilizando o método da eliminação de Gauss.

    Args:
        matrizA (np.ndarray): matriz de coeficientes
        matrizB (np.ndarray): matriz de termos independentes

    Returns:
        np.ndarray: vetor solução
    """
    if matrizA is None or matrizB is None:
        raise ValueError("matrizA e matrizB não podem ser None")
    
    if not isinstance(matrizA, np.ndarray) or not isinstance(matrizB, np.ndarray):
        try:
            matrizA = np.array(matrizA)
            matrizB = np.array(matrizB)
        except:
            raise ValueError("matrizA e matrizB devem ser do tipo numpy.ndarray")
    
    if matrizA.shape[0] != matrizA.shape[1]:
        raise ValueError("A matriz A deve ser quadrada")
    
    if matrizA.shape[0] != matrizB.shape[0]:
        raise ValueError("O número de linhas de A deve ser igual ao número de linhas de B")
    
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
        
        matrizB = sp.Matrix(entrada[0].split(' '))
        
        matrizA = sp.Matrix([])
        for i in range(1, len(entrada)):
            matrizA = matrizA.row_insert(i-1, sp.Matrix([entrada[i].split(' ')]))
    
    matrizA = np.array(matrizA)
    matrizB = np.array(matrizB)
    
    result = eliminacao_de_gauss(matrizA, matrizB)
    
    result = [round(float(i), 5) for i in result]
        
    with open(output, 'w') as file:
        file.write(str(result))
    
if __name__ == "__main__":
    main()