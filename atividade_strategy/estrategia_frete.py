"""Passo 1: contrato comum aos algoritmos de cálculo de frete."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Importação apenas para as anotações de tipo.
    # circular em tempo de execução: Pedido também importa EstrategiaFrete.
    from pedido import Pedido


class EstrategiaFrete(ABC):
    """Strategy: define a única operação exigida das estratégias concretas.

    A classe abstrata representa um contrato e não pode ser instanciada.
    Cada subclasse deve fornecer sua própria implementação de calcular().
    """

    @abstractmethod
    def calcular(self, pedido: "Pedido") -> float:
        """Recebe o pedido e retorna o custo do frete em reais."""
        pass
