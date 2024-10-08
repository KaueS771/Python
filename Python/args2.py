def soma(*args): #args empacota o que eu enviar para a função
    total = 0
    for numero in args:
        total = total + numero
    return total

soma_6 = soma(1,2,3)
print(soma_6)

numeros = 1,2,3,4,5,6,7,8,9,10
print(numeros)
print(*numeros)# desempacotamento 
outra_soma = soma(*numeros) 

print(outra_soma)

print(sum(numeros))