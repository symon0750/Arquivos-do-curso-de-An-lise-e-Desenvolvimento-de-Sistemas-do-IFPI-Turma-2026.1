# 18. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 
# 1 – Adição  
# 2 – Subtração
# 3 – Multiplicação 
# 4 – Divisão). 
# Calcule e escreva o resultado dessa operaçãosobre os dois valores lido

def validaop(msg):

    while True:
        try:
            op = int(input(msg))
            if 1 <= op <= 4:
                return op 
        except ValueError:
            print("Parâmetros errados, bananão.")

def validaN(msg):

    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Parâmetros errados, bananão.")

def calcula(op, v1, v2):

    if op == 1:
        return f"A soma dos números {v1:.2f} + {v2:.2f} é {(v1+v2):.2f}."
    elif op == 2:
        return f"A subtração dos números {v1:.2f} - {v2:.2f} é {(v1-v2):.2f}."
    elif op == 3:
        return f"A multiplicação dos números {v1:.2f} x {v2:.2f} é {(v1*v2):.2f}."
    else:
        return f"A divisão dos números {v1:.2f} + {v2:.2f} é {(v1/v2):.2f}." if v2 != 0 else "O valor 2 é 0."


def main():
    
    while True:
        op = validaop("Digite uma opção de 1~4: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n")
        v1 = validaN("Digite o 1° número: ")
        v2 = validaN("Digite o 2° número: ")

        res = calcula(op, v1, v2)
        print(res)

        continuar = str(input("Deseja realizar mais uma operação? (s/n): ").lower().strip())

        if continuar != 's':
            print("Cabô. Até a próxima.")
            break
    
if __name__ == "__main__":
    main()

    
