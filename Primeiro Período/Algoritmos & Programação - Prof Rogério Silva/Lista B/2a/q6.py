'''
Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva 
se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180º). 
Se formam, verifique  se  formam  um  triângulo  acutângulo  (3  ângulos  <  90º),  
retângulo  (1  ângulo  =  90º)
ou obtusângulo (1 ângulo > 90º). 
Não existe ângulo com tamanho 0º (zero grau).
'''


def tipotriangulo(a1:float, a2:float, a3:float):

    res = f""

    if a1 + a2 + a3 == float(180.0):

        if a1 < float(90.0) and a2 < float(90.0) and a3 < float(90.0):
            res = f"É um triângulo Acutângulo"
        elif a1 == float(90) or a2 == float(90) or a3 == float(90):
            res = f"É um triângulo Retângulo"
        elif a1 > float(90.0) and a2 > float(90.0) and a3 > float(90.0):
            res = f"É um triângulo Obtusângulo"

    elif a1 == float(0) or a2 == float(0) or a3 == float(0):
        res = f"Não existe triângulo com ângulo de 0°, seu bananão."

    else:
        res = f"Digite valores que deem 180°, seu bananão"

    return res

def main():
    n1 = float(input("Digite o 1° número: "))
    n2 = float(input("Digite o 2° número: "))
    n3 = float(input("Digite o 3° número: "))

    result = tipotriangulo(n1, n2, n3)

    print(result)

if __name__ == "__main__":
    main()
