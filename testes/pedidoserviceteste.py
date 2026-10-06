from src.models.desconto import *
from src.models.pedido import Pedido
from src.services.pedido_services import PedidoService


if __name__ == "__main__":
    pedido = [Pedido("Leonardo", DescontoVip()), Pedido("Nog", DescontoPremium()), Pedido("José", DescontoNormal())]
    for p in pedido:
        p.valor_original=120
    
    pedido_service = PedidoService()
    for p in range(len(pedido)):
        pedido_service.adicionar_pedido(pedido[p])

    pedido_service.processar_pedidos()



 