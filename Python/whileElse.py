string = str(input('Digite um nome'))

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == ' ':
        break 
    
    print(letra)
    i += 1
else:
    print('não achei espaço na string')
print('Fora do laço')
    