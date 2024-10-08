import os 
lista = []

while True:
    entrada = input('Selecione uma opção\n [i]nserir [a]pagar [l]istar [s]air:')
    
    # Verifica se a entrada é um único caractere e se é uma das opções válidas
    if len(entrada) != 1 or entrada not in 'ials':
        print('Opção inválida! Por favor, selecione [i]nserir, [a]pagar, [l]istar ou [s]air.')
        continue

    if entrada == 'i':
        print('='*20)
        valor = input('Item para inserir: ')
        print('='*20)
        lista.append(valor)
        print(lista)
        
    elif entrada == 'a':
        if lista:
            print('lista de itens')
            print('='*20)
            for indice, item in enumerate(lista):
                print(f'{indice} {item}')
            print('='*20)
            indice_str = input('qual indice voce deseja apagar:')
            
            try:
                indice = int(indice_str)
                del lista[indice]
            except ValueError:
                print('Por favor digite número int.')
            except IndexError:
                print('Indice não existe na lista')
            except Exception:
                print('Erro desconhecido')
                
    elif entrada == 'l':
        
        if len(lista) == 0:
            print('Nada a listar')
        
        print('Itens no Carrinho')
        print('='*20)
        
        indices = range(len(lista))
        for indice in indices:
            print(indice, lista[indice ])
        print('='*20)
        
    elif entrada == 's':
        print('='*20)
        print('Saindo do Programa...')
        print('='*20)
        break

print('Programa encerrado.')
        