# 14. Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

def maiormd(n1, n2, n3, n4, n5):

    t_n1 = type(n1) == int
    t_n2 = type(n2) == int
    t_n3 = type(n3) == int
    t_n4 = type(n4) == int
    t_n5 = type(n5) == int

    if t_n1 and t_n2 and t_n3 and t_n4 and t_n5:
        
        nums = []
        md = (n1 + n2 + n3 + n4 + n5)/5

        if n1 > md:
            nums.append(n1)
        if n2 > md:
            nums.append(n2)
        if n3 > md:
            nums.append(n3)
        if n4 > md:
            nums.append(n4)
        if n5 > md:
            nums.append(n5)

        return nums
    
    return "Parâmetros/tipos errados, bananão."


def main():
    try:
        num1, num2, num3, num4, num5 = int(input("Digite o 1° valor: ")), int(input("Digite o 2° valor: ")), int(input("Digite o 3° valor: ")), int(input("Digite o 4° valor: ")), int(input("Digite o 5° valor: "))
        res = maiormd(num1, num2, num3, num4, num5)
        
        if type(res) == list:
            virgulanums = ", ".join(map(str, res))
            print(f"Os números maiore que a média são {virgulanums}.")
        else:
            print(f"Ih... bananão: {res}")
    except ValueError:
        print("Só são permitidos números inteiros, bananão")

if __name__ == "__main__":
    main()

