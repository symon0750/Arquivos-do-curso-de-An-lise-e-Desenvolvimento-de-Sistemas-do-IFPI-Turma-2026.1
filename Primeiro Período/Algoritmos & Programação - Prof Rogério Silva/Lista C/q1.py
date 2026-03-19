# 1. Leia N e escreva todos os números inteiros de 1 a N.

import numpy as np

def valida(msg):

    while True:
        try:
            n = float(input(msg))

            return n

        except ValueError:
            print("Digite números, bananão.")


def imprimir(n):

    gerador = np.arange(n)
    # lista = [x for x in gerador]

    return "-".join([f"{n:0f}" for n in gerador])


def main():

    while True:
        val = valida("Digite um número: ")

        res = imprimir(val)
        print(res)

        cont = str("Quer continuar? (s/n) ").strip().lower()

        if cont != "s":
            print("Cabô")
            break 
        
if __name__ == "__main__":
    main()