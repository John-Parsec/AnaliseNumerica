import sympy as sp

# (b - a)*(f(a) + (4*f((a+b)/2))+ f(b))/6
def simpson_1_3(f, lim_inf, lim_sup):
    x = sp.symbols('x')
    mean = (lim_inf + lim_sup)/2
    
    fx0 = f.subs(x, lim_inf).evalf()
    fx1 = f.subs(x, mean).evalf()
    fx2 = f.subs(x, lim_sup).evalf()
    
    return (lim_sup - lim_inf)*(fx0 + (4*fx1) + fx2)/6

def main():
    # Exercício 11.1
    input = "inputs/simpson_1-3/exercicio_11.1_i.txt"
    output = "outputs/simpson_1-3/exercicio_11.1_i.txt"
    
    # Exercício 11.6
    #input = "inputs/simpson_1-3/exercicio_11.6_i.txt"
    #output = "outputs/simpson_1-3/exercicio_11.6_i.txt"
    
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
    divisoes = int(entrada[3])
    
    with open(output, 'w') as out_file:
        integral = simpson_1_3(f, lim_inf, lim_sup)
        
        out_file.write(f"Integral por Simpson 1/3: {integral}\n")
        

if __name__ == "__main__":
    main()