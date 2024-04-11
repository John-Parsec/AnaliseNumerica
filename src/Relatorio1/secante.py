import sympy as sp

x = sp.symbols('x')

def secante(f: sp.Expr, x0: sp.Float, x1: sp.Float, tol: sp.Rational) -> float:
    """Função que calcula a raiz de uma função f(x) utilizando o método da secante.

    Args:
        f (sp.Expr): Expressão da função a ser avaliada.
        x0 (sp.Float): Ponto inicial x0.
        x1 (sp.Float): Ponto inicial x1.
        tol (sp.Rational): Taxa de tolerancia (erro absoluto).

    Returns:
        float: Raiz da função f(x).
    """
    if x0 == x1:
        return None
    else:
        k = 1
        
        xk, fxk, xk_1, fxk_1 = sp.symbols("xk fxk xk_1 fxk_1")
        exp_sec = sp.simplify("((fxk*xk_1) - (fxk_1 *xk))/(fxk - fxk_1)")
        
        x0_val = x0
        x1_val = x1
        
        k+=1
        
        while True:
            fxk_val = f.subs(x, x1_val).evalf()
            fxk_1_val = f.subs(x, x0_val).evalf()
            
            xkpp_val = sp.simplify(exp_sec.subs(xk, x1_val).subs(fxk, fxk_val).subs(xk_1, x0_val).subs(fxk_1, fxk_1_val)).evalf() 
            
            if fxk_val == 0:
                return x1_val
            
            if abs(fxk_val.evalf()) < tol:
                return x1_val
            
            x0_val = x1_val
            x1_val = xkpp_val
            
            k += 1
    
def main():
    ### Exercício 3.3
    ## g(0.1)
    input = "inputs/secante/exercicio_3.3-0.1.txt"
    output = "outputs/secante/exercicio_3.3-0.1.txt"
    
    ## g(0.9)
    # input = "inputs/secante/exercicio_3.3-0.9.txt"
    # output = "outputs/secante/exercicio_3.3-0.9.txt"
    
    ### Exercício 3.6
    # input = "inputs/secante/exercicio_3.6.txt"
    # output = "outputs/secante/exercicio_3.6.txt"
    
    ### Exercício 3.8
    ## A
    # input = "inputs/secante/exercicio_3.8-A.txt"
    # output = "outputs/secante/exercicio_3.8-A.txt"
    
    ## B
    # input = "inputs/secante/exercicio_3.8-B.txt"
    # output = "outputs/secante/exercicio_3.8-B.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada == "":
        return None
    else:
        entrada = entrada.split('\n')
        if len(entrada) == 4:
            f = sp.simplify(entrada[0])
            x0 = sp.simplify(entrada[1])
            x1 = sp.simplify(entrada[2])
            tol = sp.simplify(entrada[3])
        else:
            return
    
    raiz = secante(f, x0, x1, tol)
    
    with open(output, 'w') as file:    
        if raiz:
            result = f.subs(sp.symbols('x'), raiz)
            
            if result == 0:
                file.write(f"Raiz: {raiz}\n")
            else:
                file.write(f"Raiz aproximada: {raiz}\n")
        else:
            file.write("Não foi possível encontrar a raiz.\n")
            
if __name__ == "__main__":
    main()