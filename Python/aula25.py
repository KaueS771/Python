
valor = float(input(""))


imposto = 0.0

if valor <= 2000.00:
    print("Isento")
else:
    if valor <= 3000.00:
        imposto += (valor - 2000.00) * 0.08
    elif valor <= 4500.00:
        imposto += (3000.00 - 2000.00) * 0.08
        imposto += (valor - 3000.00) * 0.18
    else:
        imposto += (3000.00 - 2000.00) * 0.08
        imposto += (4500.00 - 3000.00) * 0.18
        imposto += (valor - 4500.00) * 0.28
    print(f"R$ {imposto:.2f}")
