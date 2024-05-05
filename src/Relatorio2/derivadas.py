import sympy as sp

def der_progressiva(f, ponto, H): 
    x = sp.Symbol('x')
    f_x1, f_x, h = sp.symbols("f_x1 f_x h")
    
    der = sp.simplify("(f_x1 - f_x)/h")     #Formula da derivada progressiva
    
    return der.subs(f_x1, f.subs(x, ponto + H).evalf()).subs(f_x, f.subs(x, ponto).evalf()).subs(h, H).evalf()

def der_retardada(f, ponto, H):
    x = sp.Symbol('x')
    f_x1, f_x, h = sp.symbols("f_x1 f_x h")
    
    der = sp.simplify("(f_x - f_x1)/h")     #Formula da derivada retardada
    
    return der.subs(f_x1, f.subs(x, ponto - H).evalf()).subs(f_x, f.subs(x, ponto).evalf()).subs(h, H).evalf()

def der_central(f, ponto, H): 
    x = sp.Symbol('x')
    f_x1, fpx1, h = sp.symbols("f_x1 fpx1 h")
    
    der = sp.simplify("(fpx1 - f_x1)/(2*h)")    #Formula da derivada central
    
    return der.subs(f_x1, f.subs(x, ponto - H).evalf()).subs(fpx1, f.subs(x, ponto + H).evalf()).subs(h, H).evalf()

def der_segunda_ordem(f, ponto, h):
    return (der_progressiva(f, ponto, h) - der_retardada(f, ponto, h))/ h

def main():
    # Exercício 8.1.2
    input = "inputs/derivadas/exercicio_8.1.2_i.txt"
    output = "outputs/derivadas/exercicio_8.1.2_i.txt"
    # input = "inputs/derivadas/exercicio_8.1.2_ii.txt"
    # output = "outputs/derivadas/exercicio_8.1.2_ii.txt"
    # input = "inputs/derivadas/exercicio_8.1.2_iii.txt"
    # output = "outputs/derivadas/exercicio_8.1.2_iii.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
        
    f = sp.sympify(entrada[0])
    x = sp.sympify(entrada[1]).evalf()
    h = sp.sympify(entrada[2]).evalf()
    
    progressiva = der_progressiva(f, x, h)
    retardada = der_retardada(f, x, h)
    central = der_central(f, x, h)
    segunda_ordem = der_segunda_ordem(f, x, h)
    
    with open(output, 'w') as out_file:
        out_file.write(f"Derivada progressiva: {progressiva}\n")
        out_file.write(f"Derivada retardada: {retardada}\n")
        out_file.write(f"Derivada central: {central}\n")
        out_file.write(f"Derivada de segunda ordem: {segunda_ordem}\n")

if __name__ == "__main__":
    main()