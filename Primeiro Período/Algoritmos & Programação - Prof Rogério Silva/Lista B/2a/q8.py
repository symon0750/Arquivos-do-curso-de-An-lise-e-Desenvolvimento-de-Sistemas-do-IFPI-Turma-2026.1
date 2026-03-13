'''
Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
sua idade exata (em anos).
'''

def idade(diat:int, mesat:int, anoat:int, dian:int, mesn:int, anon:int):

    idexata = int()

    if anoat >= anon and len(str(diat)) <= 2 and len(str(mesat)) <= 2 and diat > 0 and diat <= 31 and mesat > 0 and mesat <=12 and len(str(dian)) <= 2 and len(str(mesn)) <= 2 and dian > 0 and dian <= 31 and mesn > 0 and mesn <=12:
        anos = anoat - anon

        if mesat < mesn:
            idexata = anos -1
        elif mesat > mesn:
            idexata = anos
        elif mesat == mesn and diat < dian:
            idexata = anos
        elif mesat == mesn and diat >= dian:
            idexata = anos
    else:
        idexata = str(idexata)
        idexata = "Inválido, seu bananão."
    
    return idexata

def main():
    dia_atual = int(input("Digite o dia atual: "))
    mes_atual = int(input("Digite o mês atual: "))
    ano_atual = int(input("Digite o ano atual: "))
    
    dia_nasci = int(input("Digite o dia em que nasceu: "))
    mes_nasci = int(input("Digite o mês em que nasceu: "))
    ano_nasci = int(input("Digite o ano em que nasceu: "))
    
    res = idade(dia_atual, mes_atual, ano_atual, dia_nasci, mes_nasci, ano_nasci)
    
    print(f"Sua idade é: {res}")
    
if __name__ == "__main__":
    main()