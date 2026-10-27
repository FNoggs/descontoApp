from src.models.desconto import IDesconto  

# Classe Contexto
class Pedido:
    def __init__(self, cliente, desconto: IDesconto):

        self.cliente = cliente
        self.Idesconto = desconto
        self.valor_original = 0.0 

    def valor_final(self, valor: float) -> float:
        self.valor_original = valor
        return valor - self.Idesconto.calcular(valor)