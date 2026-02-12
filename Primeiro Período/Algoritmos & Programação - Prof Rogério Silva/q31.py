# 31. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

nb = int(input("Digite um número binário de até quatro algarismos: "))
um = (nb // 1000) * (2**3)

r1 = nb % 1000
c = (r1 // 100) * (2**2)

r2 = r1 % 100
d = (r2 // 10) * (2**1)

r3 = (r2 % 10)
u = r3 * (2**0) 

s = um + c+ d + u
print(f"O número {nb} (binário) é equivalente, no sistema de númeração decimal, ao número {s}.")