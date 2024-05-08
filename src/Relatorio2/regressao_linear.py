import sympy as sp
from typing import TextIO

def regressao_linear(pontos: list[sp.Point], file: TextIO) -> tuple[sp.Float, sp.Float, sp.Float, sp.Float, sp.Float]:
    """Calcula a regressão linear de uma lista de pontos

    Args:
        pontos (list[sp.Point]): Lista de pontos
        file (TextIO): Arquivo de saída

    Returns:
        tuple[sp.Float, sp.Float, sp.Float, sp.Float, sp.Float]: a0, a1, coeficiente de determinação, coeficiente de correlação, desvio padrão
    """
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    n = len(pontos)
    
    file.write(f"Somatorios:\n")
    file.write(f"{'x':<6} | {'y':<6} | {'xy':<7} | {'x^2':<7}\n")
    
    for i in pontos:
        sum_x += i.x
        sum_y += i.y
        sum_xy += i.x*i.y
        sum_x2 += i.x**2
        
        file.write(f"{str(sum_x):<6} | {str(sum_y):<6} | {str(sum_xy):<7} | {str(sum_x2):<7}\n")            
    
    #a0 e a1
    a1 = ((n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x**2)).evalf()
    a0 = ((sum_y - (a1*sum_x))/n).evalf()
    
    #Medidas de dispersao
    res = residuo(pontos, a0, a1)
    
    sr_ = sr(res)
    
    d_padrao = (desvio_padrao(sr_, n)).evalf()
    
    st_ = st(pontos, n, sum_y)
    
    cof_det = (coeficiente_determinacao(st_, sr_)).evalf()
    
    cof_cor = (sp.sqrt(cof_det)).evalf()
    
    return a0, a1, cof_det, cof_cor, d_padrao

def coeficiente_determinacao(st, sr):
    return (st - sr)/st

def sr(residuo):
    sr = 0
    
    for i in residuo:
        sr += i**2
        
    return sr

def st(pontos, n, sum_y):
    st = 0
    
    mean_y = sum_y/n
    for i in range(n):
        st += (pontos[i].y - mean_y)**2
        
    return st

def residuo(pontos, a0, a1):
    residuo = []
    
    for i in range(len(pontos)):
        residuo.append(pontos[i].y - (a0 + a1*pontos[i].x)) # y - (a0 + a1*x)
        
    return residuo

def desvio_padrao(Sr, n):
    if n == 2:
        return None
    
    return (Sr/(n-2))**(1/2)

def main():
    # Exercício 8.1.1
    input = "inputs/regressao_linear/exercicio_8.1.txt"
    output = "outputs/regressao_linear/exercicio_8.1.txt"
    
    # Exércicio 8.11
    # input = "inputs/regressao_linear/exercicio_8.11.txt"
    # output = "outputs/regressao_linear/exercicio_8.11.txt"
    
    with open(input, 'r') as file:
        entrada = file.read()
    
    if entrada is None:
        print("Erro ao abrir o arquivo")
        return
    
    entrada = entrada.split('\n')
        
    pontos = []
    
    for i in entrada:
        coord = i.split(' ')
        
        pontos.append(sp.Point(float(coord[0]), float(coord[1])))    
    
    with open(output, 'w') as out_file:
        a0, a1, coef_determinacao, coef_correlacao, desvio_padrao = regressao_linear(pontos, out_file)
        
        out_file.write(f"\n")
        out_file.write(f"f(x) = {a0} + {a1}x\n")
        out_file.write(f"a0 = {a0} | a1 = {a1}\n")
                
        out_file.write(f"r^2 = {coef_determinacao}\n")
        out_file.write(f"r = {coef_correlacao}\n")
        out_file.write(f"S(x/y) = {desvio_padrao}")

if __name__ == "__main__":
    main()