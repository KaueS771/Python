#Interpolação básica de strings
#s - string
#d e i - int
#f - float
#x e X - Hexadecimal (ABCDEF0123456789)

nome =  'Luiz' #s
preco = 1000.95897643 #f
variavel = '%s, o preço e R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (15,15))