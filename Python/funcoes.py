# def soma (a,b):
#     return a + b

# n1 = 2
# n2 = 2
# resultado = soma(n1, n2)
# print(resultado)

# def calcular_soma(numeros):
#     soma = 0
#     for numero in numeros:
#         soma += numeros
#     return soma

# lista_numeros = [1,2,3,4,5,6,7,8,9]
# resultado = calcular_soma(lista_numeros)

# print(f'a soma dos valores é {resultado}')

# def soma(n1,n2):
#     print(n1 + n2)
    
# soma(5,10)


# def soma(x, y):
#     return x + y

# soma1 = soma(4,3)
# soma2 = soma(4,6)
# print(soma1 + soma2)

def soma(*args):
    total = 0
    for numero in args:
        print('Total',total, numero)
        total = total + numero
        print('Total', total)
    print(total)
    

soma = (1,2,3,4,5,6,7)