class produto():
    # atributos - estado da memória do objeto
    #pid = 0
    #descricao = ''
    #valor = 0.0
    
    # métodos - comportamento do objeto
    # método especial - construtor
    # chamado quando criamos um objeto
    def __init__(self, pi, pd, pv = 0.0):
        self.pid = pi
        self.descricao = pd
        self.valor = pv if pv >= 0 else 0.0
        self.qtd = 0
        
    def set_valor(self, pv):
        if pv >= 0.0:
            self.valor = pv
        else:
            self.valor = 0.0
    
    # exemplo nao usando o self, mas preciso da referencia
    # explicita de qualquer forma
    def set_descricao(self, ref_produto, pd):
        ref_produto.descricao = pd
        
    def set_id(self, pi):
        self.pid = pi
        
    def as_tuple(self):
        return (self.pid, self.descricao, self.valor)
    
    def venda(self):
        if (self.qtd > 0):
            self.qtd = self.qtd - 1
            return self.qtd
        else:
            print('Em falta')
            return -1
            
    def compra(self, qtd_compra):
        self.qtd = self.qtd + qtd_compra
        return self.qtd
        
    def __str__(self):
    # retorna a string que será exibida quando chamado print() para o objeto
        return str(self.as_tuple())
        
        