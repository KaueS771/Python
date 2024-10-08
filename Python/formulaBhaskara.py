import math
a = float(input("digite A"))
b = float(input("digite B"))
c = float(input("Digite C"))

delta = b**2 - 4*a*c

if delta < 0:
    print("Impossivel calcular")
elif delta == 0:
    print("Impossivel calcular")
else:
    R1 = (-b + math.sqrt(delta)) / (2*a)
    R2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"R1 = {R1:.4f} \nR2 = {R2:.4f}")