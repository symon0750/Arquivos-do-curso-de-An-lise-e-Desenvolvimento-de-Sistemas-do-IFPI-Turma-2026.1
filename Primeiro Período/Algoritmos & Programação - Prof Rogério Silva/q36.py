# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

a = int(input("Digite uma idade em anos: "))
m = int(input("Digite os meses: "))
d = int(input("Digite os dias: "))

i = d + (m *30) + (a * 365)

print(f"Essa idade é igual à {i} dias")