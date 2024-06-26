import sympy as sp

def decomposicao_LU(matrizA: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
    """Decomposição LU de uma matriz de coeficientes.

    Args:
        matrizA: Matriz de coeficientes.

    Returns:
        uple[sp.Matrix, sp.Matrix]: (Matriz triangular inferior, Matriz triangular superior).
    """
    n = sp.shape(matrizA)[0]
    
    matL = sp.eye(n)
    matU = sp.eye(n)
    
    for i in range(n):
        matU[0, i] = matrizA[0, i]
        if i != 0:
            matL[i, 0] = matrizA[i, 0]/matrizA[0, 0]

    for i in range(n):
        for j in range(n):
            if i <= j and i != 0:
                matU[i,j] = matrizA[i,j]
                for k in range(0, i):
                    matU[i,j] -= matL[i,k]*matU[k,j]
                
            if i > j and j != 0:
                matL[i,j] = matrizA[i,j]
                for k in range(0, j):
                    matL[i,j] -= matL[i,k]*matU[k,j]
                matL[i,j] /= matU[j,j]
                
    return matL, matU

def solucao(matrizA, vetorB, matrizX) -> sp.Matrix:
    """Solução de um sistema linear.

    Args:
        matrizA (sp.Matrix): Matriz de coeficientes.
        vetorB (sp.Matrix): Vetor de termos independentes.
        matrizX (sp.Matrix): Matriz de variáveis.

    Returns:
        sp.Matrix: Matriz de solução.
    """
    n = sp.shape(matrizA)[0]
    variaveis = sp.symbols('x0:%d' % n)
    
    solucao = sp.solve(matrizA*matrizX - vetorB, variaveis)

    matriz_solucao = sp.Matrix([])
    for i in range(n):
        matriz_solucao = matriz_solucao.row_insert(i, sp.Matrix([solucao[variaveis[i]]]))
    
    return matriz_solucao

def fatoracao_LU(matrizA, vetorB, matrizX) -> sp.Matrix:
    """Fatoração LU de uma matriz de coeficientes.

    Args:
        matrizA (sp.Matrix): Matriz de coeficientes.
        vetorB (sp.Matrix): Vetpr de termos independentes.
        matrizX (sp.Matrix): Matriz de variáveis.

    Returns:
        sp.Matrix: Matriz de solução.
    """
    L, U = decomposicao_LU(matrizA)
    
    matrizY = matrizX.copy()
    
    matrizY = solucao(L, vetorB, matrizY)
    
    matriz_solucao = solucao(U, matrizY, matrizX)
    
    return matriz_solucao
    
def main():    
    ## Exercício 4.1
    input = "inputs/fatoracao_LU/exercicio_4.1.txt"
    output = "outputs/fatoracao_LU/exercicio_4.1.txt"
    
    ## Exercício 4.6
    # input = "inputs/fatoracao_LU/exercicio_4.6.txt"
    # output = "outputs/fatoracao_LU/exercicio_4.6.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada == "":
        return None
    else:
        entrada = entrada.split('\n')
        
        vetorB = sp.Matrix(entrada[0].split(' '))
        
        matrizX = sp.Matrix([])
        for i in range(len(vetorB)):
            nome = 'x' + str(i)
            matrizX = matrizX.row_insert(i, sp.Matrix([sp.symbols(nome)]))
        
        matrizA = sp.Matrix([])
        for i in range(1, len(entrada)):
            matrizA = matrizA.row_insert(i-1, sp.Matrix([entrada[i].split(' ')]))
            
    result = fatoracao_LU(matrizA, vetorB, matrizX)
    
    result = [round(float(i), 5) for i in result]
    
    with open(output, 'w') as file:    
        file.write(str(result))
    
if __name__ == '__main__':
    main()