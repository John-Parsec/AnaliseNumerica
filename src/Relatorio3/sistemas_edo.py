import sympy as sp

def sistema_edo(fs: list[sp.Expr], h: float, a: float, b: float, y0: list[float]) -> list[tuple[float, list[float]]]:
    """Resolve um sistema de equações diferenciais ordinárias de primeira ordem pelo método de Runge-Kutta de quarta ordem.

    Args:
        fs (list[sp.Expr]): Lista de funções que representam o sistema de equações diferenciais ordinárias.
        h (float): Tamanho do passo.
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        y0 (list[float]): Lista de condições iniciais.

    Returns:
        list[tuple[float, list[float]]]: Lista de tuplas contendo o valor de x e o valor de y para cada iteração.
    """
    # Verificar se o número de funções é igual ao número de condições iniciais
    assert len(fs) == len(y0), "Número de funções deve ser igual ao número de condições iniciais"
    
    n = len(fs)  # número de funções no sistema
    x = sp.Symbol('x')
    y = sp.symbols('y0:%d' % n)

    results = []

    # adiciona o primeiro valor
    xi = a
    yi = y0[:]
    results.append((xi, yi[:]))

    # calcula os valores de x e y para cada iteração
    while xi < b:
        meioh = h / 2

        k1 = [f.subs({x: xi, **{y[i]: yi[i] for i in range(n)}}).evalf() for f in fs]
        k2 = [f.subs({x: xi + meioh, **{y[i]: yi[i] + meioh * k1[i] for i in range(n)}}).evalf() for f in fs]
        k3 = [f.subs({x: xi + meioh, **{y[i]: yi[i] + meioh * k2[i] for i in range(n)}}).evalf() for f in fs]
        k4 = [f.subs({x: xi + h, **{y[i]: yi[i] + h * k3[i] for i in range(n)}}).evalf() for f in fs]

        yi = [yi[i] + (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) * (h / 6) for i in range(n)]
        xi += h
        results.append((xi, yi[:]))

    return results

def ler_entrada(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    eqs = []
    i = 0
    
    while lines[i].strip():
        if lines[i].strip():
            eqs.append(lines[i].strip())
        i += 1

    i += 1
    
    params_dict = {}
    
    if "=" in lines[i]:
        params = lines[i].strip().split(',')
        params_dict = {p.split('=')[0].strip(): float(p.split('=')[1].strip()) for p in params}
        i += 2

    y0 = list(map(float, lines[i].strip().split(',')))

    i += 2
    
    a, b = map(float, lines[i].strip().split(','))

    i += 2
    h = float(lines[i].strip())

    return eqs, params_dict, y0, a, b, h

def main():
    # Exemplo 1
    input = "inputs/sistema_edo/exemplo_1.txt"
    output = "outputs/sistema_edo/exemplo_1.txt"
    
    # Exemplo 2
    # input = "inputs/sistema_edo/exemplo_2.txt"
    # output = "outputs/sistema_edo/exemplo_2.txt"
    
    # Exemplo 3
    # input = "inputs/sistema_edo/exemplo_3.txt"
    # output = "outputs/sistema_edo/exemplo_3.txt"
    
    eqs, params, y0, a, b, h = ler_entrada(input)
    
    fs = [sp.sympify(eq).subs(params) for eq in eqs]
    
    with open(output, 'w') as out_file:    
        results = sistema_edo(fs, h, a, b, y0)
        
        out_file.write(f"Resultado do metodo de Runge-Kutta:\n")
        
        for xi, yi in results:
            out_file.write(f"x = {xi:.2f}, y = {yi}\n")

if __name__ == "__main__":
    main()