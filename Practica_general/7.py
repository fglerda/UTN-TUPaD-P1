num1 = 3
num2 = 7
num3 = 4

if num2 % 2 == 0:
    x = num2 * 2
else:
    x = 3 * num2
if x % 2 == 0:
    t = x + num3
else:
    t = x - num3

if t > 10:
    resultado_final = t * num1
else:
    resultado_final = t + num1
print(f"Resultado final: {resultado_final}")
