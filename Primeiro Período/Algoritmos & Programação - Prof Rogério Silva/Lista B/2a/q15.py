# 15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
# Escreva na tela qual dos professores tem salário total maior.

def vsal(hp1, v1, hp2, v2):
    
    t_hp1, t_hp2 = type(hp1) == int, type(hp2) == int
    t_v1, t_v2 = type(v1) in (int, float), type(v2) in (int, float) 

    if t_hp1 and t_v1 and t_hp2 and t_v2:
        sal1 = hp1 * v1
        sal2 = hp2 * v2
        if sal1 > sal2:
            return 1
        elif sal1 == sal2:
            return "Ambos ganham o mesmo tanto."
        else:
            return 2
    
    return "Parâmetros/tipos errados, seu bananão."

def main():
    try:
        horas1, val1 = int(input("Digite as horas de aula do(a) primeiro(a) professor(a): ")), float(input("Digite quanto ele(a) ganha por hora: "))
        horas2, val2 = int(input("Digite as horas de aula do(a) segundo(a) professor(a): ")), float(input("Digite quanto ele(a) ganha por hora: "))

        res = vsal(horas1, val1, horas2, val2)

        if type(res) == int:
            print(f"O salário do(a) {res}° professor(a) é maior")
        else:
            print(res)
    except ValueError:
        print("Só são permitidos números inteiros/decimais seu bananão")

if __name__ == "__main__":
    main()
    