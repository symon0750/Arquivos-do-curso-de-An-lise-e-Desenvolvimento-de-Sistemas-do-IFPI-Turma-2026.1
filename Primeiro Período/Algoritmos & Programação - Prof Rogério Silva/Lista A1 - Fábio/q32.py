# Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.
v = int(input("Digite um valor de 3 dígitos: "))

resto = v % 100
c = v // 100
d = resto // 10
u = resto % 10
inv = c + (d * 10) + (u * 100)

dif =  v - inv

print(f"A diferença entre {v} e seu inverso, {inv}, é igual a {dif}.")