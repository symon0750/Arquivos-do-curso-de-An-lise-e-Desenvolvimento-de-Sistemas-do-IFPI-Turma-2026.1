def crescente(n1: float, n2: float, n3: float):
    res = ""

    if n1 < n2 and n1 < n3:
        if n2 < n3:
            res = f"{n1}, {n2}, {n3}"
        else:
            res = f"{n1}, {n3}, {n2}"
    elif n2 < n1 and n2 < n3:
        if n1 < n3:
            res = f"{n2}, {n1}, {n3}"
        else:
            res = f"{n2}, {n3}, {n1}"
    else:
        if n1 < n2:
            res = f"{n3}, {n1}, {n2}"
        else:
            res = f"{n3}, {n2}, {n1}"

    return res


def main():
    num1 = float(input("Digite o 1° número: "))
    num2 = float(input("Digite o 2° número: "))
    num3 = float(input("Digite o 3° número: "))

    result = crescente(num1, num2, num3)

    print(f"Os números em ordem crescente são: {result}")


if __name__ == "__main__":
    main()