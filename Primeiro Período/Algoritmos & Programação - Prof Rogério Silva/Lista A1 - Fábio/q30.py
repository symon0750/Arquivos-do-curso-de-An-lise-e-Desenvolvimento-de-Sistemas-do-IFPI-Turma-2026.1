# 30. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde
m = int(input("Digite um número inteiro de minutos: "))

d = m // 1440

r = m % 1440

h = r // 60

mc = r % 60 

print(f"{m} minutos equivale à {d} dias, {h} horas e {mc} minutos.")