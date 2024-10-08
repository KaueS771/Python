contador = 0

while contador <= 50:
    contador += 1
    
    
    if contador % 2 == 0:
        print('esse numero é par', contador)
        continue
    
    print(contador)
    
    if contador == 40:
        break   
    
    
print('acabou')
    
    