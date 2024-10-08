#SET
# Seus valores serão sempre unicos
# Não aceitam valores mutaveis
# não tem Index
# não garantem ordem
# são iteraveis (for, in, not in)
#elimina naturalmente valores repetidos


# s1 = set('Kaue')
# s2 = set()
# s1 = {'Kaue', 1,2,3,4}
# s1 = {1,2,2,3,3,3}
# l1 = [1,2,3,4,5,6,7,8,9,1,5,8,6,4]
# t2 = (1,1,1,1,1,1,1,2,2,3)
# s1 = set(l1)
# l2 = list(s1)#arruma a lista original por conta do set
# s2 = set(t2)
# print(s1)
# print(l2)
# print(s2)

# s1 = set()
# s1.add('Kaue')#add
# s1.add(1)
# s1.add('Ola mundo')
# print(s1 )
# s1.update(('Ola mundo',1,2,3,4))#update
# s1.clear()#clear limpa o set
# s1.discard('Ola mundo')# discard elimina o valor por referencia entre (   )
# print(s1)


#Operadores úteis:
# união (|) união (union) - Une
# intersecção (&) - Itens presentes em ambos
# diferença (-) Itens presentes apenas no set da esquerda 
#diferença simetrica (^) - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)