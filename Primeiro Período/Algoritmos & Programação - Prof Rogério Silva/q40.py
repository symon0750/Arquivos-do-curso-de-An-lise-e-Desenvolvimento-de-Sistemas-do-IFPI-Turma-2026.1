# Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele
# fuma, o nº de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

n_anos = int(input("Digite o número de anos que fuma: "))
cg_dia = int(input("Digite o número de cigarros fumados por dia: "))
v_cart = float(input("Digite o valor de uma carteira de cigarros: "))

qt_carteira_dia = cg_dia // 20
cg_fora_carteira = cg_dia % 20

val_carteiras_dia = qt_carteira_dia * 5
val_cg_fora = cg_fora_carteira * (5/20)
v_gasto_dia = val_cg_fora + val_carteiras_dia

val_ano = v_gasto_dia * 365

val_total = val_ano * n_anos

print(f"O fumante em questão gastou cerca de {val_total:.2f} R$ ao longo de {n_anos} anos.")