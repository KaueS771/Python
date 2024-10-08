numero_str = input('Vou dobrar o numero que digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')

except:
    print('Voce nao digitou nenhum numero!')



#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro do {numero_str} é {numero_float * 2:.2f}')
#else:
#    print('Voce nao digitou nenhum numero!')