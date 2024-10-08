nome = "Kaue"



novo_nome = ''
indice = 0
while indice < len(nome):
    print(nome[indice])
    letra = nome[indice]
    novo_nome += f'*{letra}'
    
    indice +=1
print(novo_nome)
    