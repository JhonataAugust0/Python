class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('Garrafa', 'R$15')
print(p1.nome, p1.preco)
        
