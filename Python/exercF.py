# def multi(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total


# multiplica = multi(1,2,3,4)
# print(multiplica)


def par_impar(x):
    if x % 2 == 0:
        return f'{x} é Par'
    return f'{x} é Impar'
    

print(par_impar(2)) 
