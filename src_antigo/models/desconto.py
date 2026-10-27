from abc import ABC, abstractmethod

class IDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1
    
class DescontoPremium(IDesconto):
    def calcular(self, valor):
        return valor * 0.2
    
class DescontoVip(IDesconto):
    def calcular(self, valor):
        return valor * 0.3