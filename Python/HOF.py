# def saudacao(msg, nome):
#     return f'{msg}, {nome}'


# def executa(funcao, *args):
#     return funcao(*args)

# v = executa(saudacao, 'Bom dia', 'Kaue')
# print(v)

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')

print(s1('Kaue'))
print(s2('kaue'))