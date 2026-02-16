# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
# distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor
# seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e
# escreva o custo ao consumidor.

cf = float(input("Digite o custo de fábrica do carro: "))

cc = cf + (cf * 0.28) + (cf * 0.45)

print(f"O custo final é de {cc:.2f} R$.")