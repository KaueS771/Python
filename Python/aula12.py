#Operações in e not in 
# String são iteráveis
# 0 1 2 3 4 5
# o t á v i o
#-6-5-4-3-2-1

#nome = 'Otavio'
#print(nome[2])
#print(nome[-6])
#print('vio' in nome) em nome existe vio?Sim - true

nome = input('Digite um nome')

encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
