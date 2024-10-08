import string
import os

palavra_Secreta = 'Futebol'
letras_acertadas = ''
numeros_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numeros_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada not in string.ascii_letters:
        print('Digite apenas letras.')
        continue
    
    if letra_digitada in palavra_Secreta:
        if letra_digitada not in letras_acertadas:
            letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_Secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(palavra_formada)
    
    if palavra_formada == palavra_Secreta:
        os.system('cls')
        print('Parabéns! Você adivinhou a palavra secreta!')
        print('A palavra secreta era:',palavra_Secreta)
        print('Numero de tentativas:', numeros_tentativas)
        break
