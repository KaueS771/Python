# a = [1,2,4,5]
# b =[]
# for i in a:
#     if i > 4:
#         b.append(i)
        
# print(b)

# a =  [2,3,4,5]
# b = [i for i in a if i > 4]
# print(b)    

# a = [3,4,5]
# a = [ i + 3 for i in a]
# print(a)

# a = map(lambda i: i + 3, a)
# print(a)

a = ["icky", "icky", "icky", "p-tang"]
for i, item in enumerate(a):
    print("{i}: {item}".format(i=i, item=item))