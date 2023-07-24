# Python é uma linguagem orientada a objetos, quase tudo nele é um objeto com suas propriedades, atributos e metodos
# A classe é o construtor de um objeto, é como se fosse a planta de uma casa ou uma planta de um projeto

class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel 


        self.ligado = False
        self.velocidade = 0 

    def ligar(self):
        if self.ligado:
            print("Carro já está ligado, nada acontece")
        else:
            print(f"{self.modelo} ligado")
            self.ligado = True

   

    def desligar(self):
        if self.ligado:
            print(f"{self.modelo} desligado")
            self.ligado = False
        else:
            print("Carro já está desligado")
            

    
    def acelerar(self):
        if self.ligado:
            self.velocidade += 1 
            print(f"{self.velocidade}km/h")
        else:
            print("O carro está desligado, você não pode acelerar ele")


    def frear (self):
        if self.ligado:
            self.velocidade -= 1 
            print(f"{self.velocidade}km/h")
        else:
            print("Não é possível frear, o carro está desligado")






