
# 11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
# valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
# possíveis para a variável opção são 1, 2 e 3

def vernum(op, n1, n2, n3):

    t_op = type(op) == (int)
    t_n1 = (type(n1) in (int, float))
    t_n2 = (type(n2) in (int, float))
    t_n3 = (type(n3) in (int, float))
    
    if t_op and t_n1 and t_n2 and t_n3 and 1 <= op <= 3:
        return [n1, n2, n3][op - 1]
    
    return "Parâmetros/tipos errados, seu bananão."
    

def main():
    try:
        opc = int(input("Digite a opção(1~3): "))
        num1, num2, num3 = float(input("Digite o 1° valor: ")), float(input("Digite o 2° valor: ")), float(input("Digite o 3° valor: "))
        result = vernum(opc, num1, num2, num3)

        print(f"Para a opção escolhida, o número é {result}")
    except ValueError:
        print("Só são permitidos números seu bananão")

if __name__ == "__main__":
    main()