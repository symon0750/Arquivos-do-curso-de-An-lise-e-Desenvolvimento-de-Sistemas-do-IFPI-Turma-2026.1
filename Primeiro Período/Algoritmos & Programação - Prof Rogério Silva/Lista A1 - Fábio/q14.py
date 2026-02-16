# 14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

n1 = float(input("Digite a 1° nota: "))
p1 = float(input("Digite o 1° peso: "))
n2 = float(input("Digite a 2° nota: "))
p2 = float(input("Digite o 2° peso: "))
n3 = float(input("Digite a 3° nota: "))
p3 = float(input("Digite o 3° peso: "))

mp = float(((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3))

print(f"A média ponderada do aluno é {mp:.2f}")