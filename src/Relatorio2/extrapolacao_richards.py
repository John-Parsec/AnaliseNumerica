import sympy as sp
from typing import TextIO

def extrapolacao_richards(f: sp.Expr, lim_inf: sp.Float, lim_sup: sp.Float, n1: int, n2: int, file: TextIO) -> sp.Float:
    """Calcula a integral de uma função f no intervalo [lim_inf, lim_sup] usando a extrapolação de Richardson

    Args:
        f (sp.Expr): Expressão a ser integrada
        lim_inf (sp.Float): Limite inferior da integral
        lim_sup (sp.Float): Limite superior da integral
        n1 (int): Número de segmentos para a primeira aproximação
        n2 (int): Número de segmentos para a segunda aproximação
        file (TextIO): Arquivo de saída

    Returns:
        sp.Float: Integral da função f no intervalo [lim_inf, lim_sup]
    """
    # Aproximações das integrais para n1 e n2, usando trapezios multiplos
    i1 = trapezio_mult(f, lim_inf, lim_sup, n1)
    i2 = trapezio_mult(f, lim_inf, lim_sup, n2)
    
    # Largura de cada segmento
    h1 = (lim_sup - lim_inf)/n1
    h2 = (lim_sup - lim_inf)/n2
    
    file.write(f"h1 = {h1}\n")
    file.write(f"h2 = {h2}\n\n")
    
    # I = I2 + ((I2 - I1)/((h1/h2)^2 - 1))    
    return i1, i2, h1, h2, i2 + ((i2 - i1)/((h1/h2)**2 - 1))

def trapezio_mult(f: sp.Expr, lim_inf: sp.Float, lim_sup: sp.Float, n_segments: int) -> sp.Float:
    """Calcula a integral de uma função f no intervalo [lim_inf, lim_sup] usando a regra do trapezio múltiplo

    Args:
        f (sp.Expr): Expressão a ser integrada
        lim_inf (sp.Float): Limite inferior da integral
        lim_sup (sp.Float): Limite superior da integral
        segments (int): Número de segmentos para a regra do trapezio múltiplo

    Returns:
        sp.Float: Integral da função f no intervalo [lim_inf, lim_sup]
    """
    x = sp.symbols('x')
    h = (lim_sup - lim_inf)/n_segments
    
    # xn de cada segmento
    segments = []
    for i in range(n_segments+1):
        segments.append(lim_inf + (i*h))
    
    # Somatorio de cada segmento para f(x)
    sum = 0
    for i in segments[1:-1]:
        sum += f.subs(x, i).evalf()
    
    return (h/2)*(f.subs(x, segments[0]).evalf() + (2*sum) + f.subs(x, segments[-1]).evalf())

def main():
    # Exercício 11.1
    input = "inputs/extrapolacao_richards/exercicio_11.1.txt"
    output = "outputs/extrapolacao_richards/exercicio_11.1.txt"
    
    # Exercício 11.6
    # input = "inputs/extrapolacao_richards/exercicio_11.6.txt"
    # output = "outputs/extrapolacao_richards/exercicio_11.6.txt"
    
    # Exercício 11.11
    # input = "inputs/extrapolacao_richards/exercicio_11.11.txt"
    # output = "outputs/extrapolacao_richards/exercicio_11.11.txt" 
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
    
    f = sp.simplify(entrada[0])
    lim_inf = sp.sympify(entrada[1]).evalf()
    lim_sup = sp.sympify(entrada[2]).evalf()
    n1 = int(entrada[3])
    n2 = int(entrada[4])
    
    with open(output, 'w') as out_file:
        i1, i2, h1, h2, integral = extrapolacao_richards(f, lim_inf, lim_sup, n1, n2, out_file)
        
        out_file.write(f"I({h1}) = {i1}\n")
        out_file.write(f"I({h2}) = {i2}\n")
        out_file.write(f"Integral: {integral}\n")
        
if __name__ == "__main__":
    main()