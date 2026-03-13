def dif(n):

    res = ""
    qt = len(str(n))

    if qt == 2:
        d = n // 10
        u = n % 10

        if d == u:
            res = "Os números são iguais."
        else:
            res = "Os números são diferentes"
    else:
        res = "Digite um número de dois dígitos."

    return res


def main():

    num = int(input("Digite um número de dois dígitos: "))

    result = dif(num)

    print(result)


if __name__ == "__main__":
    main()
