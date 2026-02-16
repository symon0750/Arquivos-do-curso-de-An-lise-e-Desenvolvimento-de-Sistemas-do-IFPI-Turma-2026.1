# 29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde

m = int(input("Digite um número inteiro de meses: "))

a = m // 12
mc = m % 12

print(f"{m} meses equivale à {a} anos e {mc} meses")