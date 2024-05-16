import sympy as sp
from testes import verifica_integral

# Calcula a integral de f(x) no intervalo [lim_inf, lim_sup] com n segmentos
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

def trapezio_simples(f: sp.Expr, lim_inf: sp.Float, lim_sup: sp.Float) -> sp.Float:
    """Calcula a integral de f(x) no intervalo [lim_inf, lim_sup] com um segmento

    Args:
        f (sp.Expr): Expressão a ser integrada
        lim_inf (sp.Float): Limite inferior da integral
        lim_sup (sp.Float): Limite superior da integral

    Returns:
        sp.Float: Integral da função f no intervalo [lim_inf, lim_sup]
    """
    x = sp.symbols('x')
    
    # (b - a)*(f(a) + f(b))/2
    return (lim_sup - lim_inf)*(f.subs(x, lim_inf) + f.subs(x, lim_sup))/2

def main():
    # Exercício 11.1
    input = "inputs/integracao_trapezio/exercicio_11.1.txt"
    output = "outputs/integracao_trapezio/exercicio_11.1.txt"
    
    # Exercício 11.6
    # input = "inputs/integracao_trapezio/exercicio_11.6.txt"
    # output = "outputs/integracao_trapezio/exercicio_11.6.txt"
    
    # Exercício 11.11
    # input = "inputs/integracao_trapezio/exercicio_11.11.txt"
    # output = "outputs/integracao_trapezio/exercicio_11.11.txt" 
    
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
        integral_simples = trapezio_simples(f, lim_inf, lim_sup)
        integral_mult = trapezio_mult(f, lim_inf, lim_sup, n_pontos)
        
        # Testando se o resultado da integral simples está correto
        out_file.write(f"Integral Simples\n")
        verifica_integral(f, integral_simples, lim_inf, lim_sup, out_file)
        
        # Testando se o resultado da integral multipla está correto        
        out_file.write(f"Integral Multiplo\n")
        verifica_integral(f, integral_mult, lim_inf, lim_sup, out_file)
        
        out_file.write(f"Integral simples: " + str(integral_simples) + "")
        out_file.write(f"\nIntegral múltipla: " + str(integral_mult) + "")
        
if __name__ == "__main__":
    main()