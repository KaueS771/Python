# Função para calcular a área do triângulo retângulo
def area_triangulo_retangulo(base, altura):
    return (base * altura) / 2

# Função para calcular a área do círculo
def area_circulo(raio):
    pi = 3.14159
    return pi * raio ** 2

# Função para calcular a área do trapézio
def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

# Função para calcular a área do quadrado
def area_quadrado(lado):
    return lado ** 2

# Função para calcular a área do retângulo
def area_retangulo(lado1, lado2):
    return lado1 * lado2

# Leitura dos valores A, B e C
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# Calculando e mostrando as áreas formatadas
print(f"TRIANGULO: {area_triangulo_retangulo(A, C):.3f}")
print(f"CIRCULO: {area_circulo(C):.3f}")
print(f"TRAPEZIO: {area_trapezio(A, B, C):.3f}")
print(f"QUADRADO: {area_quadrado(B):.3f}")
print(f"RETANGULO: {area_retangulo(A, B):.3f}")
