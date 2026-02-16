print("Digite as coordenadas do ponto 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Digite as coordenadas do ponto 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

d = ( ( ( x2 - x1 )**2 ) + ( ( y2 - y1 )**2 ) )**0.5

print(f"A distância entre os pontos 1 e 2 é {d:.2f} .")