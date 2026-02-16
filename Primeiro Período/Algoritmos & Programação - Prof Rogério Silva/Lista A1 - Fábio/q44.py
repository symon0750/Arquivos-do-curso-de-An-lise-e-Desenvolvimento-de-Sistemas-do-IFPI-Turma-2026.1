#  Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a
# quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada
# pelo usuário.

qtl = float(input("Digite a quantidade de latão que deseja: "))

c = qtl * 0.7
z = qtl * 0.3

print(f"Para obter {qtl:.2f} Kg de latão, são necessários {c:.2f} Kg de cobre e {z:.2f} kg de ferro.")