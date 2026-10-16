"""Passo 5: nova modalidade adicionada sem alterar a classe Pedido."""

from typing import TYPE_CHECKING

from estrategia_frete import EstrategiaFrete

if TYPE_CHECKING:
    from pedido import Pedido


class FreteDrone(EstrategiaFrete):
    """Implementa o novo requisito de taxa fixa de R$ 25,00."""

    def calcular(self, pedido: "Pedido") -> float:
        # A regra está inteiramente nesta nova classe.
        return 25.0
