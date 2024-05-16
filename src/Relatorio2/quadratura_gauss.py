from typing import TextIO
import sympy as sp
from sympy.integrals.quadrature import gauss_legendre

def quadratura_gauss(f: sp.Expr, lim_inf: sp.Float, lim_sup: sp.Float, n_pontos: int, file: TextIO) -> sp.Float:
    """Calcula a integral de uma função f no intervalo [lim_inf, lim_sup] usando a quadratura de Gauss

    Args:
        f (sp.Expr): Expressão a ser integrada
        lim_inf (sp.Float): Limite inferior da integral
        lim_sup (sp.Float): Limite superior da integral
        pontos (int): Número de pontos para a quadratura de Gauss
        file (TextIO): Arquivo de saída

    Returns:
        sp.Float: Integral da função f no intervalo [lim_inf, lim_sup]
    """
    
    x = sp.symbols('x')
    
    xn, wn = gauss_legendre(n_pontos, 5)
    
    # Novos valores de x e dx para a integral
    xd = ( (lim_sup + lim_inf) + (lim_sup - lim_inf) * x)/ 2
    dxd = (lim_sup - lim_inf) / 2
    
    f = f.subs(x, xd)
    f = f * dxd 

    # Tabela mostrando a evolução da integral
    file.write(f"{'i':<4} | {'xn':<9} | {'wn':<9} | {'f(xn)':<15} | {'integral':<10}\n")
    file.write("-" * 70 + "\n")
    
    # Integral
    integral = 0
    for i in range(len(xn)):    
        integral += f.subs(x, xn[i]) * wn[i]
        file.write(f"{i:<4} | {str(xn[i]):<9} | {str(wn[i]):<9} | {str(f.subs(x, xn[i])):<15} | {str(integral):<10}\n")

    return integral

def main():
    # Exercício 11.1
    input = "inputs/quadratura_gauss/exercicio_11.1.txt"
    output = "outputs/quadratura_gauss/exercicio_11.1.txt"
    
    # Exercício 11.6
    # input = "inputs/quadratura_gauss/exercicio_11.6.txt"
    # output = "outputs/quadratura_gauss/exercicio_11.6.txt"
    
    # Exercício 11.11
    # input = "inputs/quadratura_gauss/exercicio_11.11.txt"
    # output = "outputs/quadratura_gauss/exercicio_11.11.txt" 
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
    
    f = sp.simplify(entrada[0])
    lim_inf = sp.sympify(entrada[1]).evalf()
    lim_sup = sp.sympify(entrada[2]).evalf()
    n_pontos = int(entrada[3])
    
    with open(output, 'w') as out_file:
        integral = quadratura_gauss(f, lim_inf, lim_sup, n_pontos, out_file)
        out_file.write(f"\nIntegral por quadratura de Gauss - {n_pontos} pontos: {integral}\n")
        
if __name__ == "__main__":
    main()