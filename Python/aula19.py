class Carro:
    def __init__(self,nome,marca,ano,cor):
        self.nome = nome
        self.marca = marca 
        self.ano = ano
        self.cor = cor
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
        
c1 = Carro('Palio','Fiat','2010','Vermelho')
print(c1.nome)
c1.acelerar()
c2 = Carro('M3','BMW','2019','Azul')
print(c2.nome)
c2.acelerar(  )


