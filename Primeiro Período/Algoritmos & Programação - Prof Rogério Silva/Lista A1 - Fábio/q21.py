#21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).
f = float(input("Digite uma temperatura em graus fahrenheit (°F): "))
c = (5 * f - 160) / 9 

print(f"A temperatura {f} °F é equivalente à {c:.2f}°C.")