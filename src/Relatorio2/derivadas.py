import sympy as sp

def derivada_progressiva(f: sp.Expr, ponto: sp.Float, H: sp.Float) -> sp.Float:
    """Calcula a derivada progressiva de uma função f em um ponto x.

    Args:
        f (sp.Expr): Expressão da função f(x)
        ponto (sp.Float): Ponto x onde a derivada será calculada
        H (sp.Float): Valor de h

    Returns:
        sp.Float: Derivada progressiva de f(x) no ponto x
    """
    x = sp.Symbol('x')
    
    f_x1, f_x, h = sp.symbols("f_x1 f_x h")
    
    derivada = sp.simplify("(f_x1 - f_x)/h")
    
    return derivada.subs(f_x1, f.subs(x, ponto + H).evalf()).subs(f_x, f.subs(x, ponto).evalf()).subs(h, H).evalf()

def derivada_retardada(f: sp.Expr, ponto: sp.Float, H: sp.Float) -> sp.Float:
    """Calcula a derivada retardada de uma função f em um ponto x.

    Args:
        f (sp.Expr): Expressão da função f(x)
        ponto (sp.Float): Ponto x onde a derivada será calculada
        H (sp.Float): Valor de h

    Returns:
        sp.Float: Derivada progressiva de f(x) no ponto x
    """
    x = sp.Symbol('x')
    
    f_x1, f_x, h = sp.symbols("f_x1 f_x h")
    
    derivada = sp.simplify("(f_x - f_x1)/h")
    
    return derivada.subs(f_x1, f.subs(x, ponto - H).evalf()).subs(f_x, f.subs(x, ponto).evalf()).subs(h, H).evalf()

def derivada_central(f: sp.Expr, ponto: sp.Float, H: sp.Float) -> sp.Float:
    """Calcula a derivada central de uma função f em um ponto x.

    Args:
        f (sp.Expr): Expressão da função f(x)
        ponto (sp.Float): Ponto x onde a derivada será calculada
        H (sp.Float): Valor de h

    Returns:
        sp.Float: Derivada progressiva de f(x) no ponto x
    """
    x = sp.Symbol('x')
    
    f_x1, fpx1, h = sp.symbols("f_x1 fpx1 h")
    
    derivada = sp.simplify("(fpx1 - f_x1)/(2*h)")
    
    return derivada.subs(f_x1, f.subs(x, ponto - H).evalf()).subs(fpx1, f.subs(x, ponto + H).evalf()).subs(h, H).evalf()

def derivada_segunda_ordem(f: sp.Expr, ponto: sp.Float, H: sp.Float) -> sp.Float:
    """Calcula a derivada de segunda ordem de uma função f em um ponto x.

    Args:
        f (sp.Expr): Expressão da função f(x)
        ponto (sp.Float): Ponto x onde a derivada será calculada
        H (sp.Float): Valor de h

    Returns:
        sp.Float: Derivada progressiva de f(x) no ponto x
    """
    return (derivada_progressiva(f, ponto, H) - derivada_retardada(f, ponto, H))/ H 

def main():
    # Exercício 8.1.2
    input = "inputs/derivadas/exemplo_8.1.2_i.txt"
    output = "outputs/derivadas/exemplo_8.1.2_i.txt"
    
    input = "inputs/derivadas/exemplo_8.1.2_ii.txt"
    output = "outputs/derivadas/exemplo_8.1.2_ii.txt"
    
    input = "inputs/derivadas/exemplo_8.1.2_iii.txt"
    output = "outputs/derivadas/exemplo_8.1.2_iii.txt" 
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
        
    f = sp.sympify(entrada[0])
    x = sp.sympify(entrada[1]).evalf()
    h = sp.sympify(entrada[2]).evalf()
    
    d_progressiva = derivada_progressiva(f, x, h)
    d_retardada = derivada_retardada(f, x, h)
    d_central = derivada_central(f, x, h)
    d_segunda = derivada_segunda_ordem(f, x, h)
    
    with open(output, 'w') as out_file:    
        out_file.write(f"Derivada progressiva: {d_progressiva}\n")
        out_file.write(f"Derivada retardada: {d_retardada}\n")
        out_file.write(f"Derivada central: {d_central}\n")
        out_file.write(f"Derivada de segunda ordem: {d_segunda}\n")
    
if __name__ == "__main__":
    main()