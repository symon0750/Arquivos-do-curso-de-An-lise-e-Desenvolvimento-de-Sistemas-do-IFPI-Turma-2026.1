# 20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
# quarto) em que o ângulo se localiza.


import re


def valida(msg):

    while True:
        try:
            a = float(input(msg))

            if 0 <= a <= 360:
                return a
            
            print("O valot deve estar, obrigatoriamente, entre 0° e 360°, bananão.")
        except ValueError:
            print("Digite números, bananão.")


def qd(a):


    qds = {1: "No primeiro", 2: "No segundo", 3: "No terceiro", 4: "No quarto"}

    if a in [0, 90, 180, 270, 360]:
        return "Sobre o eixo do"
    elif a < 90:
        res = qds[1] 
    elif a < 180:
        res = qds[2]
    elif a < 270:
        res = qds[3]  
    else:
        res = qds[4]
    
    return res

def main():
    while True:
        ang = valida("Digite o ângulo: ")

        res = qd(ang)
        print(f"O angulo está: {res} quadrante.")

        cont = str(input("Deseja realizar mais uma operação? (s/n) ").lower().strip())

        if cont != 's':
            print("Cabô")
            break

if __name__ == "__main__":
    main()

    