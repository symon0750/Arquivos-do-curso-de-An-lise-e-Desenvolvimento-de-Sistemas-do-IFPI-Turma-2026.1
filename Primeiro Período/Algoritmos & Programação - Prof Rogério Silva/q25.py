# 25. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.
m = int(input("Digite um valor em metros: "))
km = m // 1000
mc = m % 1000

print(f"{m} metros equivale à {km} quilômetros e {mc} metros.")