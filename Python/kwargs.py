a,b = 1, 2 
a,b = b,a
# print(a, b)

pessoa = {
    'nome': 'Kaue',
    'sobrenome': 'Henrique',
}

dados_pessoa = {
    'idade': 19,
    'altura':1.7,
}


pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÂO NOMEADOS:', args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)
    
mostro_argumentos_nomeados(**pessoas_completa)

# a, b = pessoa.values()
# a, b = pessoa.items() saida('nome', 'Kaue') ('sobrenome', 'Henrique')
# (a1,a2), (b1,b2) = pessoa.items()
# print(a1,a2)
# print(b1,b2)

# for chave, valor in pessoa.items():
#     print(valor)

