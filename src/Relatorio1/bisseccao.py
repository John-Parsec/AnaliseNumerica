import sympy as sp

def bisseccao(f, a, b, tol) -> float:
    """Funcao que calcula a raiz de uma funcao f(x) pelo metodo da bisseccao

    Args:
        f (function): funcao a ser avaliada
        a (float): limite inferior
        b (float): limite superior
        tol (float): taxa de tolerancia (erro absoluto)

    Returns:
        float: raiz da funcao f(x)
    """
    x = sp.symbols('x')
    
    k = 1
    
    while True:
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        
        c = (a + b) / 2
        
        fc = f.subs(x, c)
        
        aprox = abs(b - a)
        aprox_relativa = aprox/abs(b)
        
        if fc == 0:
            return c
        
        if aprox_relativa < tol:
            return c
        
        k += 1
        
        if fa * fc < 0:
            b = c
        elif fc * fb < 0: 
            a = c
        else:
            return None

def main():
    ### Exercício 3.3
    ## g(0.1)
    input = "inputs/bisseccao/exercicio_3.3-0.1.txt"
    output = "outputs/bisseccao/exercicio_3.3-0.1.txt"
    
    ## g(0.9)
    # input = "inputs/bisseccao/exercicio_3.3-0.9.txt"
    # output = "outputs/bisseccao/exercicio_3.3-0.9.txt"
    
    ### Exercício 3.6
    # input = "inputs/bisseccao/exercicio_3.6.txt"
    # output = "outputs/bisseccao/exercicio_3.6.txt"
    
    ### Exercício 3.8
    ## A
    # input = "inputs/bisseccao/exercicio_3.8-A.txt"
    # output = "outputs/bisseccao/exercicio_3.8-A.txt"
    
    ## B
    # input = "inputs/bisseccao/exercicio_3.8-B.txt"
    # output = "outputs/bisseccao/exercicio_3.8-B.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada == "":
        return None
    else:
        entrada = entrada.split('\n')
        if len(entrada) == 4:
            f = sp.sympify(entrada[0])
            a = sp.sympify(entrada[1])
            b = sp.sympify(entrada[2])
            tol = sp.sympify(entrada[3])
        else:
            return
    
    raiz = bisseccao(f, a, b, tol)
    
    with open(output, 'w') as file:    
        if raiz:
            result = f.subs(sp.symbols('x'), raiz)
            
            if result == 0:
                file.write(f"Raiz: {raiz}\n")
            else:
                file.write(f"Raiz aproximada: {raiz}\n")
        else:
            file.write("Não foi possível encontrar a raiz.\n")
    
if __name__ == '__main__':
    main()