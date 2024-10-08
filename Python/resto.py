#desempacotamento 
# nome1, *resto = ['Kaue','Henrique', 'Santos']
# print(nome1, resto)



# #tuplas 
# nomes = 'Kaue', 'Henrique', 'Santos' 
# nome1 = tuple(nomes)#convertendo lista em tupla
# print(nomes)
# nomes = list(nomes)
# print(nomes) 

numeros = [1,2,3,4,5,6,7,8,7,10]
numeros2 = [1,6,8,5,3,4,9,2,41,10]
lista_nomes = ['kaue', 'henrique', 'santos']
# numeros.reverse() tras a lista reverça 
# numeros_uns = numeros.count(7)# conta as repetiçoes de um determinado numero ()
numeros2.sort()#ordena a lista de ordem crescente
numeros2.sort(reverse=True)#Ordena a lista de forma decrescente
lista_nomes.sort(key=len)# pega a quantidade de caracteres e organiza em ordem crescente
print(lista_nomes)
print(numeros2)