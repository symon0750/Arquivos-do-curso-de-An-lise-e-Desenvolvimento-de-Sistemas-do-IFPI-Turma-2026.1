# 13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes

def davigolias(n1, n2, n3, n4, n5):
    
    t_n1 = type(n1) == int
    t_n2 = type(n2) == int
    t_n3 = type(n3) == int
    t_n4 = type(n4) == int
    t_n5 = type(n5) == int
    
    if t_n1 and t_n2 and t_n3 and t_n4 and t_n5: # verifica os tipos e se tem realmente algum valor (se não tá vazio) 
        
        nums = sorted((n1, n2, n3, n4, n5)) #ordena a lista 
        if len(nums) == len(set(nums)):
            return nums[-1], nums[0] # maior, menor 
    
    return "Parâmetros/tipos errados, seu bananão."

def main():
    try:
        num1, num2, num3, num4, num5 = int(input("Digite o 1° valor: ")), int(input("Digite o 2° valor: ")), int(input("Digite o 3° valor: ")), int(input("Digite o 4° valor: ")), int(input("Digite o 5° valor: "))
        
        res = davigolias(num1, num2, num3, num4, num5)
        if type(res) == tuple:
            maior, menor = res
            print(f"O maior número é {maior}, e o menor é {menor}")
        else:
            print(res)
    except ValueError:
        print("Só são permitidos números inteiros seu bananão")

if __name__ == "__main__":
    main()