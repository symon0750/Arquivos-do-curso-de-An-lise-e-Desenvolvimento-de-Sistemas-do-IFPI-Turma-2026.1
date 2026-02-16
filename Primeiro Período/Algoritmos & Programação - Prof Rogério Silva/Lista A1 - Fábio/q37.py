# Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

d = int(input("Dgite uma idade em dias: "))

a = d // 365

r1 = d % 365
m = r1 // 30

d2 = r1 % 30

print(f"Essa idade corresponde à {a} anos, {m} meses e {d2} dias.")