def davigolias(n1, n2):

    res = ""

    if n1 == n2:
        res = "Os números são iguais."
    elif n1 > n2:
        res = f"O número {n1} é o maior e o {n2} é menor."
    else:
        res = f"O número {n2} é maior e o {n1} é menor."

    return res


def main():
    num1 = float(input("Digite o 1° número: "))
    num2 = float(input("Digite o 2° número: "))

    result = davigolias(num1, num2)

    print(result)


if __name__ == "__main__":
    main()