# 12. Leia 1 (um) número inteiro e escreva se este número é par ou impar.

def vernum(n):

    t_n = type(n) == int

    if t_n:
        if n % 2 == 0:
            return "Par"
        else:
            return "Ímpar" 
    else:
        return "Parâmetros/tipos errados, seu bananão."

def main():
    try:
        valor = int(input("Digite um número: "))
        res = vernum(valor)
        print(f"Esse número é: {res}.")
    except ValueError:
        print("Só são permitidos números inteiros, seu bananão")

if __name__== "__main__":
    main()