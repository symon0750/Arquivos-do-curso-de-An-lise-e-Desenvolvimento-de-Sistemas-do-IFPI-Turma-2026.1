#11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

v = int(input("Digite um valor de 3 dígitos: "))

resto = v % 100
c = v // 100
d = resto // 10
u = resto % 10
inv = c + (d * 10) + (u * 100)

print(f"O inverso de {v} é {inv}")