# 19. Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)
from math import pi

r = float(input("Digite o valor do raio: "))
v = (4 * pi * r**3) / 3

print(f"O valor do volume dessa esfera é {v:.2f}")