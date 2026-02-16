#27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde. 

s = int(input("Digite uma quantidade de segundos: "))
h = s // 3600 
r = s % 3600
m = r // 60
sc = r % 60

print(f"{s} equivale a {h} horas, {m} minutos e {sc} segundos.")