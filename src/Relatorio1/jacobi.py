import sympy as sp

def variacao(vet_1, vet_0):
    k1_norm_inf = vet_1.norm(sp.oo)
    
    sk1_k0_norm_inf = (vet_1 - vet_0).norm(sp.oo)
    
    return sk1_k0_norm_inf, (sk1_k0_norm_inf / k1_norm_inf).evalf()

def jacobi(matrizB: sp.Matrix, vetorG: sp.Matrix, tol: float, vetor_inical: sp.Matrix = None) -> sp.Matrix:
    """Função que calcula o método de Jacobi

    Args:
        matrizB (sp.Matrix): Matriz B.
        vetorG (sp.Matrix): Vetor G.
        tol (float): Taxa de tolerancia de erro.
        vet_inical (sp.Matrix, optional): Vetor inicial. Default None.

    Returns:
        sp.Matrix: Vetor solução do sistema linear.
    """
    n = sp.shape(matrizB)[0]
    
    if vetor_inical is None:
        vetor_inical = sp.zeros(n, 1)
    
    
    vet_0 = vetor_inical.copy()
    
    vet_1 = matrizB * vet_0 + vetorG
    
    erro_abs, erro_rel = variacao(vet_1, vet_0)
    
    while(erro_abs > tol or erro_rel > tol):
        vet_0 = vet_1.copy()
        
        vet_1 = matrizB * vet_0 + vetorG
        
        erro_abs, erro_rel = variacao(vet_1, vet_0)
        
    return vet_0

def main():
    ## Exercício 5.1
    input = "inputs/jacobi/exercicio-5.1.txt"
    output = "outputs/jacobi/exercicio-5.1.txt"
    
    ## Exercício 5.2
    # input = "inputs/jacobi/exercicio-5.2.txt"
    # output = "outputs/jacobi/exercicio-5.2.txt"
    
    ## Exercício 5.5
    # input = "inputs/jacobi/exercicio-5.5.txt"
    # output = "outputs/jacobi/exercicio-5.5.txt"

    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada == "":
        return None
    else:
        entrada = entrada.split('\n')
        haveX0 = entrada[0].split(' ')[0] == 'x0'
        
        if haveX0:
            n = sp.simplify(entrada[1])
            x0 = sp.Matrix(entrada[0].split(' ')[1:])
            tol = sp.simplify(entrada[2])
            b = sp.Matrix(entrada[3].split(' '))
        else:
            n = sp.simplify(entrada[0])
            tol = sp.simplify(entrada[1])
            b = sp.Matrix(entrada[2].split(' '))
            x0 = None

        matrizX = sp.Matrix([])
        for i in range(n):
            nome = 'x' + str(i)
            matrizX = matrizX.row_insert(i, sp.Matrix([sp.symbols(nome)]))
        
        matrizA = sp.Matrix([])
        for i in range(4, len(entrada)):
            if haveX0:
                matrizA = matrizA.row_insert(i-4, sp.Matrix([entrada[i].split(' ')[0:]]))
            else:
                matrizA = matrizA.row_insert(i-4, sp.Matrix([entrada[i-1].split(' ')[0:]]))
                
        if not haveX0:
            matrizA = matrizA.row_insert(n-1, sp.Matrix([entrada[len(entrada)-1].split(' ')[0:]]))
    
    matrizB = sp.zeros(n)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                matrizB[i,j] = -matrizA[i,j]/matrizA[i,i]
    
    n = sp.shape(matrizA)[0]
    
    vetorG = b.copy()
    
    for i in range(n):
        vetorG[i,0] /= matrizA[i,i]
    
    result = jacobi(matrizB, vetorG, tol, x0)
    
    with open(output, 'w') as file:
        for i in range(n):
            file.write(f'{round(float(result[i]), 5)}\n')

if __name__ == "__main__":
    main()

    
    