# [gift.js] Uma loja presenteia suas clientes com descontos
# (cashback) progressivos de acordo com suas compras. Desta
# forma, para compras mensais de até R$ 250 reais, é feita a
# conversão (geração) de cashback de 5%; Para compras acima de
# R$ 250 até R$ 500, 7% de cashback; De R$ 500 até R$ 750, 8%
# de cashback; E para compras acima de R$ 750 é aplicado
# primeiramente as regras anteriores até R$ 750 do valor em cada
# faixa, e 25% sobre o valor acima de R$ 750. Operações de
# cashbacks progressivos têm o objetivo de incentivar as suas
# clientes a comprarem mais e ao mesmo tempo serem
# compensadas por isso.

# a. Implemente um software para auxiliar no cálculo do
# cashback mensal de suas clientes (devem ser lidos N
# compras Nome Cliente e Valor Compras).

# b. Informe quanto foi o faturamento total (soma das vendas);
# Quanto foi distribuído em cashback; Qual o valor em reais e
# percentual investido em cashback pela loja; Maior, menor e
# valor médio pago em cashback.


def validar(label: str):
    ...


def calculos(values):
    
    operacoes = {
        "5%": lambda x: x + x*(0.05),
        "7%": lambda x: x + x*(0.07),
        "8%": lambda x: x + x*(0.08),
        "25%": lambda x: x + x*(0.25)
    }

    fat_total = [values(x) for x in values if x <= 250.0]
    


