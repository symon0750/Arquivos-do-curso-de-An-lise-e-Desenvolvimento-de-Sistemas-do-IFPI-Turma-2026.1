def maior(maior1, maior2, maior3):
    if maior1 > maior2 and maior1 > maior3:
        return maior1
    elif maior2 > maior1 and maior2 > maior3:
        return maior2
    else:
        return maior3


def main():
    n1 = float(input("numero 1: "))
    n2 = float(input("numero 2: "))
    n3 = float(input("numero 3: "))

    result = maior(n1, n2, n3)

    print(f"O numero maior entre os 3 é: {result}")


if __name__ == "__main__":
    main()
