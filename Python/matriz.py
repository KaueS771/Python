linhas= 3
colunas = 3

matriz = []

for i in range(linhas):
    linhas = []
    for j in range(colunas):
        valor = int(input("valor a matriz"))
        linhas.append(valor)
    matriz.append(linhas)
    

for linhas in matriz:
    print(linhas)