from random import randint

class Pessoa:
    ano_atual = 2020
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.falar == True: 
            print(f'{self.nome} já está falando.\n')  
        else: pass 
    
    def comer(self, alimento):
        if self.comendo == True:
            print(f'{self.nome} já está comendo.\n')
        else:
            self.comendo = True
            print(f'{self.nome} está comendo {alimento}.\n')

    def pararComer(self):
        if self.comendo == True:
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo.\n')
    
    @classmethod
    def por_ano_nascimento(cls, nome, nascimento):
        ano_atual = 2020
        idade = cls.ano_atual - nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        return randint(100, 12000)



p1 = Pessoa('Luiz', 28, False, False)

p1.comer('maçã')
p1.pararComer()
p1.comer('pedra')
p1 = Pessoa.por_ano_nascimento('Luiz', 1897)