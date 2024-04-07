import sympy as sp

def newton_raphson(f, x0, tol) -> float:
    """Funcao que calcula a raiz de uma funcao f(x) pelo metodo de Newton-Raphson

    Args:
        f (function): funcao a ser avaliada
        x0 (): valor inicial
        tol (float): taxa de tolerancia (erro absoluto)

    Returns:
        float: raiz da funcao f(x)
    """
    x = sp.symbols('x')
    
    k = 1
    
    xk, fxk, f_xk = sp.symbols("xk fxk f_xk")
    exp_rap = sp.simplify("xk - ((fxk)/(f_xk))")
    
    while True:
        xk_val = x0.evalf()
        
        # calculo de f(xk) e f'(xk)
        fxk_val = f.subs(x, xk_val).evalf()
        f_xk_val = sp.diff(f, x).subs(x, xk_val).evalf()
          
        # caso f(xk) = 0, então xk é a raiz
        if fxk_val == 0:
            return xk_val
        
        
        # verifica se o erro é menor que a tolerância
        if abs(fxk_val.evalf()) < tol:
            return xk_val
        
        # calcula o proximo ponto xk
        x0 = exp_rap.subs(xk, xk_val).subs(fxk, fxk_val).subs(f_xk, f_xk_val).evalf()
        k += 1

def main():
    ### Exercício 3.3
    ## g(0.1)
    input = "inputs/newton-raphson/exercicio_3.3-0.1.txt"
    output = "outputs/newton-raphson/exercicio_3.3-0.1.txt"
    
    ## g(0.9)
    # input = "inputs/newton-raphson/exercicio_3.3-0.9.txt"
    # output = "outputs/newton-raphson/exercicio_3.3-0.9.txt"
    
    ### Exercício 3.6
    # input = "inputs/newton-raphson/exercicio_3.6.txt"
    # output = "outputs/newton-raphson/exercicio_3.6.txt"
    
    ### Exercício 3.8
    ## A
    # input = "inputs/newton-raphson/exercicio_3.8-A.txt"
    # output = "outputs/newton-raphson/exercicio_3.8-A.txt"
    
    ## B
    # input = "inputs/newton-raphson/exercicio_3.8-B.txt"
    # output = "outputs/newton-raphson/exercicio_3.8-B.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada == "":
        return None
    else:
        entrada = entrada.split('\n')
        if len(entrada) == 3:
            x0 = sp.simplify(entrada[0])
            tol = sp.simplify(entrada[1])
            f = sp.simplify(entrada[2])
        else:
            return
    
    raiz = newton_raphson(f, x0, tol)
    
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