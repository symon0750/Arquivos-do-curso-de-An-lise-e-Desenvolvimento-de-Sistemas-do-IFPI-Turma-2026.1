# 18. Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)
from math import pi

r = float(input("Digite o valor do raio: "))
c = 2 * pi * r

print(f"O valor do comprimento desse círculo é {c:.2f}")