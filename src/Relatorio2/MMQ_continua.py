import sympy as sp
from typing import TextIO
from MMQ_discreta import aproximacao_polinomial_MMQ_discreta

def aproximacao_polinomial_MMQ_continua(f: sp.Expr, degree: int, lim_inf: sp.Float, lim_sup: sp.Float, file: TextIO) -> sp.Matrix:
    """Aproximação polinomial de f(x) por MMQ contínua

    Args:
        f (sp.Expr): Função a ser aproximada
        degree (int): Grau do polinomio
        lim_inf (sp.Float): Limite inferior
        lim_sup (sp.Float): Limite superior
        file (TextIO): Arquivo de saída

    Returns:
        sp.Matrix: Vetor de coeficientes
    """
    x = sp.symbols('x')
    mat_X = sp.zeros(degree + 1, degree + 1)
    vet_fx = sp.zeros(degree + 1, 1)
    
    vet_A = sp.Matrix([])   # Vetor de simbolos
    for i in range(degree + 1):
        name = 'x' + str(i)
        vet_A = vet_A.row_insert(i, sp.Matrix([sp.symbols(name)]))
    
    for i in range (degree + 1):
        for j in range (degree + 1):
            if i > j:
                mat_X[i,j] = mat_X[j,i]
            else:
                mat_X[i,j] = sp.integrate(x**i * x**j, (x, lim_inf, lim_sup))   # Integral de x^i*x^j de limite_inf a limite_sup
        
        vet_fx[i,0] = sp.integrate(f * (x**i), (x, lim_inf, lim_sup))       # Integral de f(x)*x^i de limite_inf a limite_sup
        
        file.write(f"Integral de f(x)*x^{i} de {lim_inf} a {lim_sup}: {vet_fx[i,0]}\n")
        
    return resolve_sistema(mat_X, vet_fx, vet_A)

# Resolve o sistema de matrizes
def resolve_sistema(matrizA: sp.Matrix, matrizB: sp.Matrix, matrizX: sp.Matrix) -> sp.Matrix:
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

# Cria o polinomio a partir do vetor de coeficientes
def cria_polinomio(vet_a: sp.Matrix, var: sp.Symbol) -> sp.Expr:
    """Cria o polinomio a partir do vetor de coeficientes

    Args:
        vet_a (sp.Matrix): Vetor de coeficientes
        var (sp.Symbol): Variável

    Returns:
        sp.Expr: Polinomio
    """
    n = len(vet_a)
    
    polinomio = ""
    for i in range(n):
        if i == 0:
            polinomio += str(vet_a[i,0]) + " + (" 
        elif i == n-1:
            polinomio += str(vet_a[i,0]) + "* " + str(var) +"**" + str(i) + ")"
        else:
            polinomio += str(vet_a[i,0]) + "* "+ str(var) + "**" + str(i) + ") + ("
            
    return sp.sympify(polinomio)

def main():
    # Exercício 8.1
    input = "inputs/MMQ_continua/exercicio_8.1.txt"
    output = "outputs/MMQ_continua/exercicio_8.1.txt"
    
    # Exercício 8.5
    # input = "inputs/MMQ_continua/exercicio_8.5.txt"
    # output = "outputs/MMQ_continua/exercicio_8.5.txt"
    
    # Exercício 10.6
    # input = "inputs/MMQ_continua/exercicio_10.6_2.txt"
    # output = "outputs/MMQ_continua/exercicio_10.6_2.txt" 
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
        
    header = entrada[0].split(' ')
    f = ""
    
    degree = int(header[0])
    lim_inf = float(header[1])
    lim_sup = float(header[2])
    
    if len(header) >= 4:
        for i in range(3, len(header)):
            f += header[i]
        
    if(len(entrada) > 1):   # Se tiver pontos para aproximar, usamos MMQ discreta
        pontos = []
        
        for i in entrada[1:]:
            coord = i.split(' ')
            pontos.append(sp.Point(float(coord[0]), float(coord[1])))
        
        vet_a = aproximacao_polinomial_MMQ_discreta(pontos)
        x = sp.symbols('x')
        f = cria_polinomio(vet_a, x)
    
    with open(output, 'w') as out_file:
        out_file.write(f"Função: {f}\n\n")
        
        coeficiente_a = aproximacao_polinomial_MMQ_continua(f, degree, lim_inf, lim_sup, out_file)
        size = len(coeficiente_a)
        
        out_file.write(f"\n")
        
        # polinomio
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