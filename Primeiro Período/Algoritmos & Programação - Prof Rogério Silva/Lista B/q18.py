# 18. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 
# 1 – Adição  
# 2 – Subtração
# 3 – Multiplicação 
# 4 – Divisão). 
# Calcule e escreva o resultado dessa operaçãosobre os dois valores lido

def valida(msg, mi=None, mx=None):

    while True:
        try:
            val = float(input(msg))
            if mi is not None and mx is not None:
                if mi <= val <= mx:
                    return val
                else:
                    print("Digite valores nos intervalos especificados.")
            else:
                return val
        except ValueError:
            print("Parâmetros errados, bananão.")

def calcula(op, v1, v2):

    operacoes = {1: "+", 2: "-", 3: " x ", 4: " / "}
    simbolo = operacoes[op]

    if op == 1:
        res = v1 + v2
    elif op == 2:
        res = v1 - v2
    elif op == 3:
        res = v1 * v2    
    elif op == 4:
        if v2 != 0:
            res = v1 / v2
        else:
            return "Erro, divisão por 0."
    
    return f"Operação: {v1} {simbolo} {v2} = {res:.2f}"


def main():
    
    while True:
        op = valida("Digite uma opção de 1~4: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n", 1, 4)
        v1 = valida("Digite o 1° número: ")
        v2 = valida("Digite o 2° número: ")

        res = calcula(op, v1, v2)
        print(res)

        continuar = str(input("Deseja realizar mais uma operação? (s/n): ").lower().strip())

        if continuar != 's':
            print("Cabô. Até a próxima.")
            break
    
if __name__ == "__main__":
    main()

    
