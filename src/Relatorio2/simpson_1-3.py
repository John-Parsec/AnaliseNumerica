import sympy as sp

def simpson_mult(f: sp.Expr, lim_inf: sp.Float, lim_sup: sp.Float, n_segments: int) -> sp.Float:
    """Calcula a integral de uma função f no intervalo [lim_inf, lim_sup] usando a regra de Simpson 1/3 múltipla

    Args:
        f (sp.Expr): Expressão a ser integrada
        lim_inf (sp.Float): Limite inferior da integral
        lim_sup (sp.Float): Limite superior da integral
        segments (int): Número de segmentos

    Returns:
        sp.Float: Integral da função f no intervalo [lim_inf, lim_sup]
    """
    x = sp.symbols('x')
    h = (lim_sup - lim_inf)/n_segments
    
    # xn de cada segmento
    segments_xn = []
    for i in range(n_segments+1):
        segments_xn.append(lim_inf + (i*h))
    
    # Somatorio de cada segmento para f(x) par
    sum_par = 0
    for i in range(2, len(segments_xn) - 1, 2):
        sum_par += f.subs(x, segments_xn[i]).evalf()
        
    # Somatorio de cada segmento para f(x) impar
    sum_impar = 0
    for i in range(1, len(segments_xn) - 1, 2):
        sum_impar += f.subs(x, segments_xn[i]).evalf()
    
    return (h/3)*(f.subs(x, segments_xn[0]).evalf() + (4*sum_impar) + (2*sum_par) + f.subs(x, segments_xn[-1]).evalf())

def simpson_1_3(f: sp.Expr, lim_inf: sp.Float, lim_sup: sp.Float) -> sp.Float:
    """Calcula a integral de uma função f no intervalo [lim_inf, lim_sup] usando a regra de Simpson 1/3

    Args:
        f (sp.Expr): Expressão a ser integrada
        lim_inf (sp.Float): Limite inferior da integral
        lim_sup (sp.Float): Limite superior da integral

    Returns:
        sp.Float: Integral da função f no intervalo [lim_inf, lim_sup]
    """
    x = sp.symbols('x')
    mean = (lim_inf + lim_sup)/2
    
    fx0 = f.subs(x, lim_inf).evalf()
    fx1 = f.subs(x, mean).evalf()
    fx2 = f.subs(x, lim_sup).evalf()
    
    # (b - a)*(f(a) + (4*f((a+b)/2))+ f(b))/6
    return (lim_sup - lim_inf)*(fx0 + (4*fx1) + fx2)/6

def main():
    # Exercício 11.1
    input = "inputs/simpson_1-3/exercicio_11.1.txt"
    output = "outputs/simpson_1-3/exercicio_11.1.txt"
    
    # Exercício 11.6
    #input = "inputs/simpson_1-3/exercicio_11.6.txt"
    #output = "outputs/simpson_1-3/exercicio_11.6.txt"
    
    # Exercício 11.11
    #input = "inputs/simpson_1-3/exercicio_11.11.txt"
    #output = "outputs/simpson_1-3/exercicio_11.11.txt" 
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
    
    f = sp.sympify(entrada[0])
    lim_inf = sp.sympify(entrada[1]).evalf()
    lim_sup = sp.sympify(entrada[2]).evalf()
    divs = int(entrada[3])
    
    with open(output, 'w') as out_file:
        integral_simples = simpson_1_3(f, lim_inf, lim_sup)
        integral_mult = simpson_mult(f, lim_inf, lim_sup, divs)
        
        out_file.write(f"Integral simples por Simpson 1/3: {integral_simples}\n")
        out_file.write(f"Integral múltipla por Simpson 1/3: {integral_mult}\n")

if __name__ == "__main__":
    main()