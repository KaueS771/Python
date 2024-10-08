
numero = input('Digite um numero inteiro:')
numero_str = int(numero)
if numero.isdigit():
    if numero_str % 2 == 0:
        print('é Par')
    else:
        print('é Impar')
else:    
    print('Voce não digitou um numero inteiro')

 
 
  
hora  = input('Usuario que hora são ?')

try:
    hora_int = int(hora)
    
    if hora_int >= 0 and hora_int < 12:
        print('Bom dia')
    
    elif hora_int >= 11 and hora_int < 17:
        print('Boa tarde')
    
    elif hora_int >= 17 and hora_int < 23:
        print('Boa Noite')
except:
    print('Hora Invalida')
 


nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome == 5 or 6:
        print('Seu nome é Normal')
    elif tamanho_nome > 6:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
 