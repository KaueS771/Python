# a, *rest = [1,2,3]
# # a = 1, rest = [2,3]
# print(a, rest)

# a, *middle, c = [1,2,3,4]
# print(f"a= {a}, middle= {middle}, c= {c}")

filename = 'foobar.txt'
basename, __, ext = filename.rpartition('.')
print(basename)

