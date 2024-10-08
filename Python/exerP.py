perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',  
    },
]
qtd_acertos = 0

# Iterando sobre cada pergunta no dicionário
for indice, pergunta in enumerate(perguntas):
    print(f"Pergunta {indice}: {pergunta['Pergunta']}")

    # Iterando sobre as opções de cada pergunta
    for idx, opcao in enumerate(pergunta['Opções']):
        print(f"{idx}: {opcao}")

    # Solicitando a resposta do usuário
    entrada = input('Escolha uma Opção: ')

    # Verificando se a resposta está correta
    if entrada == pergunta['Resposta']:
        qtd_acertos +=1
        print('** Acertou **')
    else:
        print('XX Errou XX')

print('Voce acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
        
    
