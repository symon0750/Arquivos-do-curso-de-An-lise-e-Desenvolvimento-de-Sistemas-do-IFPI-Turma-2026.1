#20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)
c = float(input("Digite uma temperatura em graus celsius (°C): "))
f = (9 * c + 160) / 5 

print(f"A temperatura {c} °C é equivalente à {f:.2f}°F.")