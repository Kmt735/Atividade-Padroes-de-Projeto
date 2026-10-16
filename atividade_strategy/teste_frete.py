"""Passo 4: cliente que escolhe e injeta cada estratégia no pedido.

Execute na pasta deste arquivo: python teste_frete.py
Não há dependências externas: basta ter Python 3 instalado.
"""

from frete_drone import FreteDrone
from frete_retirada_local import FreteRetiradaLocal
from fretes import FreteMotoboy, FretePac, FreteSedex, FreteTransportadora
from pedido import Pedido


def main() -> None:
    """Demonstra as modalidades e a substituição do algoritmo em execução."""
    print("Cálculo de frete com Strategy")
    pedido = Pedido(peso_kg=2.5)

    # A seleção fica no cliente. A lista associa um rótulo de exibição a
    # cada objeto, sem transferir para Pedido a escolha da modalidade.
    modalidades = [
        ("SEDEX", FreteSedex()),
        ("PAC", FretePac()),
        ("TRANSPORTADORA", FreteTransportadora()),
        ("MOTOBOY", FreteMotoboy()),
        ("DRONE", FreteDrone()),
        ("RETIRADA_LOCAL", FreteRetiradaLocal()),
    ]

    print("Pedido com 2,5 kg:")
    for nome, estrategia in modalidades:
        # O mesmo pedido recebe algoritmos diferentes por composição.
        pedido.set_estrategia(estrategia)
        valor = pedido.calcularFrete()
        valor_formatado = f"{valor:.2f}".replace(".", ",")
        print(f"  {nome}: R$ {valor_formatado}")

    # No cliente original, pedido2 era criado, mas o cálculo usava pedido.
    # Aqui o PAC é corretamente calculado sobre o segundo pedido, de 10 kg.
    pedido2 = Pedido(peso_kg=10.0)
    pedido2.set_estrategia(FretePac())
    valor_formatado = f"{pedido2.calcularFrete():.2f}".replace(".", ",")
    print(f"Pedido com 10 kg - PAC: R$ {valor_formatado}")


if __name__ == "__main__":
    # Impede que a demonstração rode apenas por importar este módulo.
    main()
