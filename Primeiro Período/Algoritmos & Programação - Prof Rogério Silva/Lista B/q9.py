'''
9. Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.
'''
def eh_primo_recursivo(n: int, divisor=None):
    
    if n > 0 and n <=100:

        if divisor is None:
            divisor = int(n**0.5)

        if n <= 1: 
            return False
        if n == 2: 
            return True
        if n % 2 == 0: 
            return False
        if divisor < 2: 
            return True 

        if n % divisor == 0:
            return False
    
        return eh_primo_recursivo(n, divisor - 1)
    
    else:
        res = ""
        res = "É entre 0 e 100, seu bananão."
        return res
def main():
    num = int(input("Digite um número entre 0 e 100: "))
    result = eh_primo_recursivo(num)
    print(f"É primo: {result}")
if __name__ == "__main__":
    main()

