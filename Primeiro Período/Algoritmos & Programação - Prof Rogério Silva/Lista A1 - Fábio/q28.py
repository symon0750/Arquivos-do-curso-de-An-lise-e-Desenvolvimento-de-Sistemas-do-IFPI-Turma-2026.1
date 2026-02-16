# 28. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

h = int(input("Digite um valor inteiro de horas: "))

s = h // 168

r = h % 168

d = r // 24

hc = r % 24

print(f"{h} horas equivale a {s} semanas, {d} dias e {hc} horas.")