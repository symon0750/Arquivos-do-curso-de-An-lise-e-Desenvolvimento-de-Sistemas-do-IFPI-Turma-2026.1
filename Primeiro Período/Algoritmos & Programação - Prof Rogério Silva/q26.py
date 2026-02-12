#26. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

d = int(input("Digite um número de dias: "))
s = d // 7
ds = d % 7

print(f"{d} dias equivale à {s} semanas e {ds} dias.")