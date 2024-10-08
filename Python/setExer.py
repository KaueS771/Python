lista_de_lista_de_inteiros = [
    [1, 2, 3,3,5,6,7,3,2],
    [4, 52,4,5,7,2,1,3,5],
    [6, 7, 8, 9,3,2,5,6,2],
    [10,10,2,4,7,5,4,2,1,4]
]

def encontrar_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        
        numeros_checados.add(numero)

    return primeiro_duplicado
    
for lista in lista_de_lista_de_inteiros:
    print(
        lista,
        encontrar_duplicado(lista)
    )
