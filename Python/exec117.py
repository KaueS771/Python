# def duplican(numero):
#     return numero * 2
# def triplicam(numero):
#     return numero * 3
# def quadriplicam( numero):
#     return numero * 4

# n1 = duplican(2)
# nm = triplicam(2)
# nq = quadriplicam(2)

# print(n1)
# print(nm)
# print(nq)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))
