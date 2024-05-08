import sympy as sp
from scipy.integrate import quad

def verifica_integral(f, integral, lim_inf, lim_sup, file = None):
    x = sp.symbols('x')
        
    resultado, erro = quad(sp.lambdify(x, f), lim_inf, lim_sup)     # Faz a integral pelo método quad()
        
    erro_rel = abs((resultado - integral)/integral)
    
    if file:
        file.write(f"Resultado da integral pela Quadratura Adaptativa de Gauss-Kronrod: {resultado}\n")
        file.write(f"Erro pela Quadratura Adaptativa de Gauss-Kronrod: {erro}\n")
        file.write(f"Erro relativo entre meu resultado e o da Quadratura Adaptativa de Gauss-Kronrod: {erro_rel}\n\n")
        
        return None
    else:
        return resultado, erro_rel
    
def verifica_polinomio(polinomio, pontos, file = None):
    x = sp.symbols('x')
    verify = True
    
    for x_, y_ in pontos:
        resultado = polinomio.subs(x, x_)
        
        file.write(f"\nf({float(x_)}) = {float(y_)}")
        
        if abs(resultado - float(y_)) > 1e-10:      #Verifica se são suficientemente proximos, ignorando erros de truncamento
            file.write(f"\nResultado do polinomio: {resultado}\n")
            verify = False
    
    return verify