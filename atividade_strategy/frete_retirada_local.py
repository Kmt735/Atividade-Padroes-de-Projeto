"""Modalidade gratuita mencionada no cenário da atividade."""

from typing import TYPE_CHECKING

from estrategia_frete import EstrategiaFrete

if TYPE_CHECKING:
    from pedido import Pedido


class FreteRetiradaLocal(EstrategiaFrete):
    """O cliente retira o produto na loja e não paga frete."""

    def calcular(self, pedido: "Pedido") -> float:
        return 0.0
