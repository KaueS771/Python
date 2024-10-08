import os
# #Listas em Python
# Tipo List - Mutavel
# Suporta varios valores de qualquer tipo
# Metodos úteis: append, insert, pop, del, clear, extend, +
# #


# string = 'ABCDE' # 5 caracteres (len)
# lista = []
# lista = [123, True, 'Kaue Henrique', 1.2, []]
# lista[2] = 'Rodrigo Faro'
# print(lista)
# print(lista[2], type(lista[2]))

# lista = [1,2,3]
# # soma = lista[1] + lista[2]
# # del lista[0] # deleta o valor do indice, e o python reorganiza  

# # print(lista)
# # print(soma)

# lista.append(50)
# print(lista)

lista_Par = []
lista_Impar = []
i = 0
for i in range(1,10):
    numero = int(input("Digite um numero para lista"))
    if numero % 2 == 0:
        lista_Par.append(numero)
        print(f' {numero} adicionado a lista Par:',lista_Par)
    else:
        lista_Impar.append(numero)
        print(lista_Impar)
        print(f' {numero} adicionado a lista Impar:',lista_Impar)
os.system('cls')
print('Lista Impar:',lista_Impar)
print('Lista Par',lista_Par)

    
# ultimo_valor = lista.pop()# remove o ultimo item da lista
# print(lista, 'Removido', ultimo_valor)