#rsplit = pega o argumento apos o caracter escolhido(.)
#split = pega o argumento antes do caracter escolhido(.)

filename, ext = "my_photo.orig.png".rsplit(".", 1)
print(filename, "is a", ext, "file.")

