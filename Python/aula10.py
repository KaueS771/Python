entrada = input('[E]ntrar [S]air:')
senha_digitada =input('Senha:')

senha_permitida = '123456'
#and = checar mais de uma expressao
if (entrada =='E' or 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
#Avaliação de Curto Circuito AND
print(True and False and True) # False
print(True and True and True) # True  

#Avaliação de Curto Circuito OR
senha = input('Senha ') or 'Sem senha'
print(True or False or 0 or 'abc')

 
    