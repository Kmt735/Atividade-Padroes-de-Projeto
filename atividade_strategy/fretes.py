"""Passo 2: estratégias com as quatro regras do projeto original."""

from typing import TYPE_CHECKING

from estrategia_frete import EstrategiaFrete

if TYPE_CHECKING:
    from pedido import Pedido


class FreteSedex(EstrategiaFrete):
    """SEDEX: taxa inicial de R$ 10,00 e R$ 1,50 por quilograma."""

    def calcular(self, pedido: "Pedido") -> float:
        # O peso é consultado pela propriedade pública do pedido.
        return 10.0 + pedido.peso_kg * 1.5


class FretePac(EstrategiaFrete):
    """PAC: taxa inicial de R$ 5,00 e R$ 1,00 por quilograma."""

    def calcular(self, pedido: "Pedido") -> float:
        return 5.0 + pedido.peso_kg * 1.0


class FreteTransportadora(EstrategiaFrete):
    """Transportadora: R$ 20,00 mais R$ 3,00 por quilograma."""

    def calcular(self, pedido: "Pedido") -> float:
        return 20.0 + pedido.peso_kg * 3.0


class FreteMotoboy(EstrategiaFrete):
    """Motoboy: taxa fixa de R$ 15,00, independentemente do peso."""

    def calcular(self, pedido: "Pedido") -> float:
        # Matendo o parâmetro para respeitar o contrato.
        return 15.0
