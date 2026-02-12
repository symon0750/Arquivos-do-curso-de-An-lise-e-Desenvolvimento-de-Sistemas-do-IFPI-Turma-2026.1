# Leia 2 (duas) frações (numerador e denominador), 
# calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

nf1 = int(input("Digite o númerador da 1° fração: "))
df1 = int(input("Digite o denominador da 1° fração: "))

nf2 = int(input("Digite o númerador da 2° fração: "))
df2 = int(input("Digite o denominador da 2° fração: "))

nf = (nf1 * df2) + (nf2 * df1)
df = (df1 * df2)

print(f"A soma dessas duas frações é {nf}/{df}.")