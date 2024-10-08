pessoa = {
    'nome': 'Kaue',
    'sobrenome':'Henrique',
    'idade': 19,
    'altura': 1.75,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
    
}
# pessoa1 = dict(nome='Henrique')
del pessoa['altura']

print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print()


if pessoa.get('altura') is None:
    print('Não existe')
else:
    print(pessoa['altura'])


for chave in pessoa:
    print(f'{chave} : {pessoa[chave]}')