# Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. 
# Ex.: número = 9534 ; soma = 9+5+3+4 = 21.


n = int(input("Digite um número de até quatro algarismos: "))
um = (n // 1000)

r1 = n % 1000
c = (r1 // 100)

r2 = r1 % 100
d = (r2 // 10) 

r3 = (r2 % 10)
u = r3 

s = um + c+ d + u
print(f"A soma dos algarismos do número {n} é = {s}.")