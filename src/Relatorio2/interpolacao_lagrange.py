import sympy as sp
from testes import verifica_polinomio

def interpolacao_lagrange(pontos: list[sp.Point]) -> sp.Expr:
    """Interpolação de Lagrange

    Args:
        pontos (list[sp.Point]): Lista de pontos

    Returns:
        sp.Expr: Polinomio interpolador
    """
    n = len(pontos)
    
    polinomio = 0
    for i in range(n):
        lagrange_i = lagrange(pontos, i)
        
        polinomio += pontos[i].y * lagrange_i
    
    return sp.simplify(sp.sympify(polinomio)).evalf()

def lagrange(pontos: list[sp.Point], k: int) -> sp.Expr:
    """Polinomio de Lagrange

    Args:
        pontos (list[sp.Point]): Lista de pontos
        k (int): Número do polinomio de Lagrange

    Returns:
        sp.Expr: Polinomio de Lagrange
    """
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
        polinomio = interpolacao_lagrange(pontos)
        
        out_file.write(f"f(x) = {polinomio}\n")
        
        if verifica_polinomio(polinomio, pontos, out_file):
            out_file.write(f"\nO polinomio passa por todos os pontos!")
        else:
            out_file.write(f"\nO polinomio não passa por todos os pontos! :(")

if __name__ == "__main__":
    main()


