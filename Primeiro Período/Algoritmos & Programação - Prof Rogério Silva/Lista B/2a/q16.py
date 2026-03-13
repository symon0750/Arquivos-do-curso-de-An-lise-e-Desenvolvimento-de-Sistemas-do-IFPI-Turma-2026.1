# 16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
# ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
# final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
# escreva “Reprovado”.

def media(n1, n2):

    md = (n1 + n2)/2
    return "Aprovado" if md >= 7 else md


def exame(m, n_ex):

    mdfinal = (m + n_ex) / 2
    return "Aprovado." if mdfinal >= 5 else "Reprovado."


def ntvalida(n):
    return type(n) in (int, float) and 0 <= n <= 10


def main():
    try:
        nota1, nota2 = float(input("Digite a 1° nota: ")), float(input("Digite a 2° nota: "))
        
        if ntvalida(nota1) and ntvalida(nota2):
            res1 = media(nota1, nota2)
            if type(res1) == str:
                print(f"O Aluno está... {res1}!!!!!!!!!!!!!!!!!!\n(não fez mais que sua obrigação ¯|_(ツ)_|¯)")
            else:
                try:
                    nt_ex = float(input("Digite a nota do exame: "))
                    if ntvalida(nt_ex):
                        med_f = exame(res1, nt_ex)
                        print(f"O aluno está {med_f}.")
                    else:
                        print("Digite a nota corretamente, bananão.")
                except:
                    print("Digita a nota, bananão.")
        else:
            print("Digite as notas corretamente, bananão.")            
 
    except ValueError:
        print("Digita a nota, bananão.")

if __name__ == "__main__":
    main()
