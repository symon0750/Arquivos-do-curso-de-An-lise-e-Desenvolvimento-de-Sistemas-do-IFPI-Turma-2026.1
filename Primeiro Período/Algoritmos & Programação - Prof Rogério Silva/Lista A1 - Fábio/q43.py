a = float(input("Digite o valor de 'a': "))
b = float(input("Digite o valor de 'b': "))
c = float(input("Digite o valor de 'c': "))
d = float(input("Digite o valor de 'd': "))
e = float(input("Digite o valor de 'e': "))
f = float(input("Digite o valor de 'f': "))

x = ( ( c * e) - ( b * f ) ) / ( ( c * e ) - ( b * d ))
y = ( ( a * f) - ( c * d ) ) / ( ( a * e ) - ( b * d ))

print(f"O valor de x é {x:.2f} e o valor de y é {y:.2f}")
