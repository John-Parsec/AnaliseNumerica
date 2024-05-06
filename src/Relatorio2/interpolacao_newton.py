import sympy as sp
from typing import TextIO

def dif_dividida(pontos: list[sp.Point], indexes: list[int]) -> sp.Float:
    """Calcula a diferença dividida

    Args:
        pontos (list[sp.Point]): Lista de pontos
        indexes (list[int]): Índices dos pontos

    Returns:
        sp.Float: Diferença dividida
    """
    n = len(indexes)
    
    if n == 2:
        return (pontos[indexes[0]].y - pontos[indexes[1]].y)/(pontos[indexes[0]].x - pontos[indexes[1]].x)
    elif n == 1:
        return pontos[indexes[0]].y
    else:
        return (dif_dividida(pontos, indexes[1:])-dif_dividida(pontos, indexes[:-1]))/(pontos[indexes[n-1]].x - pontos[indexes[0]].x)

def interpolacao_newton(pontos: list[sp.Point], file: TextIO) -> str:
    """Interpolação de Newton

    Args:
        pontos (list[sp.Point]): Lista de pontos
        file (TextIO): Arquivo de saída

    Returns:
        str: Polinomio interpolador
    """
    n = len(pontos)
    difs_divididas = []
    
    indexes = []
    for i in range(n):
        indexes.insert(0, i) 
        dif = dif_dividida(pontos, indexes)
        
        file.write(f"f({pontos[i].x}) = {float(dif)}\n")
        difs_divididas.append(dif)
    
    polinomio = ""
    
    for i in range(len(difs_divididas)):
        if i == 0:
            polinomio += str(float(difs_divididas[i].evalf())) + " + "
        else:
            polinomio += str(float(difs_divididas[i].evalf()))
            for j in range(i):
                polinomio += f"*(x - {pontos[j].x})"
                if j == i - 1:
                    if i != 1:
                        polinomio += ")"
                    if i < len(difs_divididas) - 1:
                        polinomio += " + ("
    
    polinomio = sp.sympify(polinomio)
    
    return str(polinomio)

def main():
    # Exercício 11.1    
    input = "inputs/interpolacao_newton/exercicio_10.2.txt"
    output = "outputs/interpolacao_newton/exercicio_10.2.txt"
    
    # Exercício 10.9
    # input = "inputs/interpolacao_newton/exercicio_10.9.txt"
    # output = "outputs/interpolacao_newton/exercicio_10.9.txt"
    
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
        polinimio = interpolacao_newton(pontos, out_file)
        
        out_file.write(f"\nf(x) = {polinimio}\n")

if __name__ == "__main__":
    main()