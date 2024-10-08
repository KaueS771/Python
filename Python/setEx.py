letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())
    
    if 'k' in letras:
        print('Parabens voce achou a letra secreta')
        break
    
    print(letras)
    