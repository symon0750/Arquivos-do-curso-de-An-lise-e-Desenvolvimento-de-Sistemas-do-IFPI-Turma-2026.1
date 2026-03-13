def verificar(n1, n2, n3):

    res = ""

    if n1 == n2 and n1 == n3:
        res = "Todos os números são iguais."
    elif n1 == n2 and n1 != n3:
        res = f"Somente o 1°({n1}) e o 2°({n2}) número são iguais."
    elif n1 == n3 and n1 != n2:
        res = f"Somente o 1°({n1}) e o 3°({n3}) número são iguais."
    elif n2 == n3 and n2 != n1:
        res = f"Somente o 2°({n2}) e o 3°({n3}) número são iguais."
    else:
        res = "Todos os números são diferentes"

    return res


def main():
    num1 = float(input("Digite o 1° número: "))
    num2 = float(input("Digite o 2° número: "))
    num3 = float(input("Digite o 3° número: "))

    result = verificar(num1, num2, num3)

    print(result)


if __name__ == "__main__":
    main()