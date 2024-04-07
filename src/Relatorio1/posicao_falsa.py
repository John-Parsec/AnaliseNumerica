import sympy as sp

def posicao_falsa(f, a, b, tol):
    x = sp.symbols('x')
    
    k = 1
    
    exp_falsa = sp.simplify("((ax * fbx) - (bx * fax)) / (fbx - fax)")
    ax, bx, fax, fbx = sp.symbols('ax bx fax fbx')
    
    while True:
        fa = f.subs(x, a)
        fb = f.subs(x, b)
        
        xk = exp_falsa.subs(ax, a).subs(bx, b).subs(fax, fa).subs(fbx, fb).evalf()
        
        fxk = f.subs(x, xk)
        
        aprox = abs(b - a)
        aprox_relativa = aprox/abs(b)
        
        if fxk == 0:
            return xk
        
        if aprox_relativa < tol or k > 1000:
            return xk

        k += 1
        
        if fa * fxk < 0:
            b = xk
        elif fb * fxk < 0:
            a = xk
        else:
            return None
        
def main():
    ### Exercício 3.3
    ## g(0.1)
    input = "inputs/posicao_falsa/exercicio_3.3-0.1.txt"
    output = "outputs/posicao_falsa/exercicio_3.3-0.1.txt"
    
    ## g(0.9)
    # input = "inputs/posicao_falsa/exercicio_3.3-0.9.txt"
    # output = "outputs/posicao_falsa/exercicio_3.3-0.9.txt"
    
    ### Exercício 3.6
    # input = "inputs/posicao_falsa/exercicio_3.6.txt"
    # output = "outputs/posicao_falsa/exercicio_3.6.txt"
    
    ### Exercício 3.8
    ## A
    # input = "inputs/posicao_falsa/exercicio_3.8-A.txt"
    # output = "outputs/posicao_falsa/exercicio_3.8-A.txt"
    
    ## B
    # input = "inputs/posicao_falsa/exercicio_3.8-B.txt"
    # output = "outputs/posicao_falsa/exercicio_3.8-B.txt"
    
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
    
    raiz = posicao_falsa(f, a, b, tol)
    
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