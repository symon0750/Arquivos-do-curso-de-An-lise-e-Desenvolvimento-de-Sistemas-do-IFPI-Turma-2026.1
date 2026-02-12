# Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
# (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

v = int(input("Digite um valor de 3 dígitos: "))

resto = v % 100
c = v // 100
d = resto // 10
u = resto % 10
inv = c + (d * 10) + (u * 100)

s =  v + inv

print(f"A soma entre {v} e seu inverso, {inv}, é igual a {s}.")