'''
10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida
'''

def data(diat, mesat, anoat):

    res = False

    if len(str(diat)) <= 2 and len(str(mesat)) <= 2 and diat > 0 and diat <= 31 and mesat > 0 and mesat <=12 and isinstance(diat, int) and isinstance(mesat, int) and isinstance(anoat, int):
        res = True
    else:
        res = False
    
    return res

def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    result = data(dia, mes, ano)
    
    print(f"A validez da data é: {result}")
    
if __name__ == "__main__":
    main()

#???