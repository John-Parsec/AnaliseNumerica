import sympy as sp
import numpy as np
import eliminacao_gauss as eg

def inversao_gauss(matrizA: sp.Matrix, matrizB: sp.Matrix) -> sp.Matrix:
    matrizA = np.array(matrizA).astype(float)
    matrizB = np.array(matrizB).astype(float)
    
    A_inv = np.linalg.inv(matrizA)
    matrizX = np.dot(A_inv, matrizB)
    
    return sp.Matrix(matrizX)

def main():
     ## Exercício 5.5
    input = "inputs/inversao_gauss/exercicio-5.5.txt"
    output = "outputs/inversao_gauss/exercicio-5.5.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()

    if entrada == "":
        return None
    else:
        entrada = entrada.split('\n')
        
        matrizB = sp.Matrix(entrada[0].split(' '))
        
        matrizA = sp.Matrix([])
        for i in range(2, len(entrada)):
            matrizA = matrizA.row_insert(i-2, sp.Matrix([entrada[i].split(' ')]))
    
    result = inversao_gauss(matrizA, matrizB)
    
    result = [round(float(i), 9) for i in result]
        
    with open(output, 'w') as file:
        file.write(str(result))
    
if __name__ == '__main__':
    main()