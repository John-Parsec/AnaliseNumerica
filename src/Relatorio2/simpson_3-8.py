import sympy as sp

# ((b-a)/8)*(f(x0) + (3*f(x1)) + (3*f(x2))+ f(x3))
def simpson_3_8(f, lim_inf, lim_sup, file): 
    x = sp.symbols('x')
    
    h = (lim_sup - lim_inf)/3
    
    # xn de cada segmento
    segments = []
    for i in range(4):
        segments.append(lim_inf + (i*h))
    
    # calcula o valor de cada f(xn)
    f_xns = []
    for n in segments:
        f_xn = f.subs(x, n).evalf()
        
        f_xns.append(f_xn)
        
        file.write(f"f({x}, {n}) : {str(f_xn)}\n")
    
    return ((lim_sup - lim_inf)/8)*(f_xns[0] + (3*f_xns[1]) + (3*f_xns[2]) + f_xns[3])

def main():
    # Exercício 8.1.2
    input = "inputs/simpson_3-8/exercicio_11.1.txt"
    output = "outputs/simpson_3-8/exercicio_11.1.txt"
    
    # Exercício 11.6
    #input = "inputs/simpson_3-8/exercicio_11.6.txt"
    #output = "outputs/simpson_3-8/exercicio_11.6.txt"
    
    # Exercício 11.11
    #input = "inputs/simpson_3-8/exercicio_11.11.txt"
    #output = "outputs/simpson_3-8/exercicio_11.11.txt" 
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
    
    f = sp.sympify(entrada[0])
    lim_inf = sp.sympify(entrada[1]).evalf()
    lim_sup = sp.sympify(entrada[2]).evalf()
    
    with open(output, 'w') as out_file:
        integral = simpson_3_8(f, lim_inf, lim_sup, out_file)
        
        out_file.write("\n")
        out_file.write(f"Integral por Simpson 3/8: {integral}\n")

if __name__ == "__main__":
    main()