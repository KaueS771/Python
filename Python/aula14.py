nome = input('Digite seu nome:')
idade = input('Digite sua idade:')

if nome and idade:
    print(f'Seu nome é {nome}') 
    print(f'Seu nome ao invertido é: {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome  NÂO contém espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira Letra do seu nome é: {nome[0]}')
    print(f'A ultima Letra do seu nome é: {nome[3]}')
else:
    print('Desculpe, você deixou campos vazios. ')

