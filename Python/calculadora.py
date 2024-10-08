
while True:
    n1 = input('Digite um numero n1:')
    n2 = input('Digite um numero n2:')
    operador = input('Digite um operador (+-/*):')
    
    numeros_validos = None
    n1_float = 0
    n2_float = 0
    
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:#Is = forem
        print('Um ou ambos os numeros digitados são invalidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador invalido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando sua conta, Confira o resultado abaixo: ')
    if operador == '+':
        soma = n1_float + n2_float
        print(f'a soma entre {n1_float} + {n2_float} é {soma}')
        
    elif operador == '-':
        subtracao = n1_float - n2_float
        print(f'a subtração entre {n1_float} - {n2_float} é {subtracao}')
        
    elif operador == '/':
        divisao = n1_float / n2_float
        print(f'a divisão entre {n1_float} / {n2_float} é {divisao}')
        
    elif operador == '*':
        multiplicacao = n1_float * n2_float
        print(f'a multiplicação entre {n1_float} * {n2_float} é {multiplicacao:.2f}')
        
    else:
        print('Nunca deveria chegar aqui. ')
    
    sair = input('Quer sair? [s]im:').lower().startswith('s')
    #lower - coloca as letras em minusculo
    #startwith - pega a primeira letra
    if sair is True:
        break
    print(sair)
        