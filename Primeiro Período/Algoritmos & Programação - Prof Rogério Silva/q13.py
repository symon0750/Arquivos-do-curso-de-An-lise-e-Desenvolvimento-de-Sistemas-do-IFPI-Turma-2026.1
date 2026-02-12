# 13. Leia um valor em real (R$), calcule e escreva 70% deste valor.

v = float(input("Digite um valor em real (R$): "))
nv = v * 0.7

print(f"70% de {v} é {nv:.2f} R$")