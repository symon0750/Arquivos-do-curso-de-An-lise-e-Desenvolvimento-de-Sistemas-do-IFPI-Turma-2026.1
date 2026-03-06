'''
Leia  3  (três)  números  (cada  número  corresponde  a  um  lado  do  triângulo),  verifique  e  escreva  se  os  3 
(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se 
formam,  verifique  se  formam  um  triângulo  equilátero  (3  lados  iguais),  isósceles  (2  lados  iguais)  ou 
escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero). 
'''

def tipotriangulo(l1:float, l2:float, l3:float):
    
    res = f""

    if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l2 + l1):
        if (l1 == l2) and (l2 == l3):
            res = f"O triângulo é equilátero"
        elif (l1 == l2) or (l1 == l3 ) or (l3 == l2):
            res = f"O triângulo é isósceles"
        elif (l1 != l2) and (l2 != l3):
            res = f"O triângulo é escaleno"

    elif l1 == float(0) or l2 == float(0) or l3 == float(0):
        res = f"Não existe triângulo com lado de valor 0, seu bananão."
        
    else:
        res = f"Digite valores que deem que um triângulo, seu bananão"

    return res

def main():
    n1 = float(input("Digite o 1° número: "))
    n2 = float(input("Digite o 2° número: "))
    n3 = float(input("Digite o 3° número: "))

    result = tipotriangulo(n1, n2, n3)

    print(result)

if __name__ == "__main__":
    main()
