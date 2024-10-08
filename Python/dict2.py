

pessoa = {
    'nome': 'Kaue',
    'sobrenome': 'Henrique',
}
print(len(pessoa))#le as quantidade de chaves
print(pessoa.keys())#retorna as chaves
print(pessoa.values())#retorna valor

print(pessoa.items())#retorna chave + valor
pessoa.setdefault('idade', None)#adiciona valor caso a chave não exista 

pessoa2 = pessoa.copy()#retorna uma copia rasa (Shallow Copy)
pessoa2 = copy.deepcopy(pessoa)#copia profunda (uma copia que será distinta da outra no local de memoria)

pessoa2['nome'] = 'tay'

print(pessoa.get('nome', 'Não Existe'))#pega o nome no dict

nome = pessoa.pop('nome') #remove o elemento selecionado
print(nome)


# ultima_chave = pessoa.popitem()#remove a ultima chave do dict
# print(ultima_chave)

# pessoa.update({ atualiza e cria valores inexistentes no dict
#     'nome': 'novo valor',
#     'idade': 19,
# })
# pessoa.update(nome='KAUE', idade=20)
# print(pessoa)
# tupla = ('nome', 'lionel'),('idade', 34), ('titulos', 'Copa do Mundo')
# pessoa.update(tupla)
print(pessoa)
# print(pessoa2)

