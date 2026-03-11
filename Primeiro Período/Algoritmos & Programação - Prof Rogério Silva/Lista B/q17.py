# 17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
# escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
# são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
# divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
# escreva o quadrado dos números lidos.

def valida(n):

    return True if type(n) == int else False


def calculo(n1, n2):
    
    op = n1 % n2

    if op == 1:
        return "O resto é 1 e a soma é", n1 + n2 + 1
    if op == 2:
        return "Os números são pares" if (n1%2 == 0 and n2 % 2== 0) else "Os números são ímpares"     
    if op == 3:
        return (n1 + n2) * n1
    if  op == 4:
        return ((n1 + n2) / n2) if n2 != (0) else "O resto é 4. Mas o 2° número é 0."
    else:
        return n1**2, n2**2


def main():
    try:
        v1 = int(input("Digite o 1° valor: "))
        v2 = int(input("Digite o 2° valor: "))
        if valida(v1) and valida(v2):
            res = calculo(v1, v2)
            if type(res) == tuple:
                sentença, soma = res
            if type(res) == int:
                print(f"A soma do 1° e do 2° multiplicada pelo 1° é {res}")
            else:
                print(res)
    except:
        print("Parâmetros/tipos errados, bananão.")

if __name__=="__main__":
    main()


# usar try except
# configurar os retorno e clocar try except



# isso aqui foi o que aprendi
# isso aqui foi o código
# agora quero melhorar meu código
# depois quero aprender a usar loops