# Iteravel -> str, range, etc (__iter__)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o proximo valor
#iter -> me entregue seu iterador

texto = 'Luiz'
iterador = iter(texto)
 
# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopAsyncIteration:
#         break
    
for letra in texto:
    print(letra)
        
