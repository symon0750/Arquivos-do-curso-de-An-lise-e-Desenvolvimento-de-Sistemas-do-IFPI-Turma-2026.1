# 19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
# (IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso
# (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).


def valida(msg, mi, mx):
    while True:
        try:
            val = float(input(msg))
            
            if msg == "Altura: " and 0.022 <= val <= 2.72:
                return val
            elif msg == "Peso: " and 0.212 <= val <= 635:
                return val
            else:
                print("Digite valores válidos (humanamente possíveis, seu bananão)")
        
        except ValueError:
            print("Parâmetros ou tipos errados, bananão.") 


def calc(p, a):

    imc = p / a**2

    if imc < 25:
        return f"Seu peso está normal"
    elif 25 <= imc <= 30:
        return f"Você está obeso."
    else:
        return f"Seu imc indica que você está com obesidade mórbida"
    

def main():
    while True:
        peso = valida("Peso: ", 0.212, 635)
        altura = valida("Altura: ", 0.22, 2.72)

        res = calc(peso, altura)

        print(res)

        continuar = str(input("Deseja calcular mais um IMC? (s/n)\n").strip().lower())

        if continuar != 's':
            print("Cabô.\nAté a próxima.")
            break

if __name__ == "__main__":
    main()