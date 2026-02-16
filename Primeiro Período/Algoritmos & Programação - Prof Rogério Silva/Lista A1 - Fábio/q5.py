#q5

v = int(input("Digite um valor de 3 dígitos: "))

resto = v % 100

c = v // 100

d = resto // 10

u = resto % 10

soma = c + d + u
print(f"A soma dos algarismos da unidade({u}), dezena({d}) e centena({c}) é {soma}. ")