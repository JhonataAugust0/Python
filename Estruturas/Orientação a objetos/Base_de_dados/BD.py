from random import randint

class BD:
    def __init__(self ):
        self._dados = {}

    @property
    def dados(self):
        return self._dados

    def inserir_clientes(self, nome, id ):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})
        
    def listar_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(f"\n{id}:  {nome}")

    def apagar_clientes(self, id):
        del self._dados['clientes'][id]


bd1 = BD()
bd2 = BD()
bd1.inserir_clientes(77, 'Mário')
bd2.inserir_clientes(25, 'Júlia')
print(bd1.dados)
print(bd2.dados)
