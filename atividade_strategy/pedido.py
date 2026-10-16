"""Passo 3: Pedido é o contexto do padrão Strategy."""

from typing import Optional

from estrategia_frete import EstrategiaFrete


class Pedido:
    """Mantém o peso e delega o frete à estratégia escolhida pelo cliente.

    A classe conhece somente EstrategiaFrete. Não importa classes concretas
    e não seleciona modalidades com if/elif ou match/case.
    """

    def __init__(self, peso_kg: float):
        self._peso_kg = peso_kg
        # O prefixo duplo torna o atributo privado por name mangling.
        # None indica que o cliente ainda não selecionou uma estratégia.
        self.__estrategia: Optional[EstrategiaFrete] = None

    @property
    def peso_kg(self) -> float:
        """Disponibiliza o peso para as estratégias, sem setter público."""
        return self._peso_kg

    def set_estrategia(self, estrategia: EstrategiaFrete) -> None:
        """Injeta ou substitui o algoritmo sem recriar o pedido."""
        self.__estrategia = estrategia

    def calcularFrete(self) -> float:
        """Delega o cálculo; não recebe parâmetros além do self implícito.

        O método antigo calcular_frete(tipo_servico) foi removido.
        O nome calcularFrete segue literalmente o enunciado do PDF.
        """
        if self.__estrategia is None:
            # Isso verifica a configuração, sem escolher uma modalidade.
            # Falhar explicitamente evita confundir falta de estratégia
            # com um frete que seja realmente gratuito.
            raise ValueError("Defina uma estratégia antes de calcular o frete.")

        # Polimorfismo: a mesma chamada executa a implementação do objeto
        # recebido pelo setter. Pedido não precisa conhecer a fórmula.
        return self.__estrategia.calcular(self)
