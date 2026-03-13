# 17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
# escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
# são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
# divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
# escreva o quadrado dos números lidos.


def valida(msg):

    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Parâmetros errados, bananão")


def calculo(n1, n2):
    
    r = n1 % n2

    if r == 1:
        return f"A soma de (n1+n2+resto) é {n1+n2+r}."
    elif r == 2:
        lista = [f"{x} é {'Par' if x % 2 == 0 else 'Ímpar\n'}" for x in [n1,n2]]
        return " | ".join(lista)
    elif r == 3:
        return f"A soma dos valores lidos ({n1}-{n2}) multiplicado pelo primeiro é {(n1+n2) * n1 }."
    elif r == 4:
        return f"A soma dos valores lidos ({n1}-{n2}) dividido pelo segundo é {((n1 + n2) / n2):.2f}" if n2 != 0 else "O segundo número é 0."
    else:
        lista = [f"O quadrado de {n} é {n**2}" for n in [n1,n2]]
        return " | ".join(lista)

def main():
    while True:
        v1 = valida("Digite o 1° valor: ")
        v2 = valida("Digite o 2° valor: ")

        res = calculo(v1, v2)
        print(res)

        op = str(input("Deseja fazer mais um cálculo? (s/n): ").strip().lower())
        

        if op != 's':
            print("Cabô. Até a próxima.")
            break

if __name__=="__main__":
    main()

