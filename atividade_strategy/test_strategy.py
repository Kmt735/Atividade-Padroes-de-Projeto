"""Verificações automatizadas: python -m unittest -v

Os testes conferem as regras preservadas, os novos requisitos e o uso de
uma estratégia inédita sem qualquer alteração em Pedido.
"""

import unittest

from estrategia_frete import EstrategiaFrete
from frete_drone import FreteDrone
from frete_retirada_local import FreteRetiradaLocal
from fretes import FreteMotoboy, FretePac, FreteSedex, FreteTransportadora
from pedido import Pedido


class TestStrategy(unittest.TestCase):
    def test_regras_originais_em_diferentes_pesos(self):
        # Valores esperados calculados a partir das regras originais.
        casos = [
            (2.5, FreteSedex(), 13.75),
            (2.5, FretePac(), 7.50),
            (2.5, FreteTransportadora(), 27.50),
            (2.5, FreteMotoboy(), 15.00),
            (10.0, FreteSedex(), 25.00),
            (10.0, FretePac(), 15.00),
            (10.0, FreteTransportadora(), 50.00),
            (10.0, FreteMotoboy(), 15.00),
        ]
        for peso, estrategia, esperado in casos:
            with self.subTest(peso=peso, estrategia=type(estrategia).__name__):
                pedido = Pedido(peso)
                pedido.set_estrategia(estrategia)
                self.assertAlmostEqual(pedido.calcularFrete(), esperado)

    def test_drone_tem_taxa_fixa(self):
        for peso in (0.5, 2.5, 10.0):
            with self.subTest(peso=peso):
                pedido = Pedido(peso)
                pedido.set_estrategia(FreteDrone())
                self.assertEqual(pedido.calcularFrete(), 25.0)

    def test_retirada_local_gratuita(self):
        pedido = Pedido(2.5)
        pedido.set_estrategia(FreteRetiradaLocal())
        self.assertEqual(pedido.calcularFrete(), 0.0)

    def test_troca_de_estrategia_no_mesmo_pedido(self):
        pedido = Pedido(2.5)
        pedido.set_estrategia(FreteSedex())
        self.assertEqual(pedido.calcularFrete(), 13.75)
        pedido.set_estrategia(FreteDrone())
        self.assertEqual(pedido.calcularFrete(), 25.0)
        self.assertEqual(pedido.peso_kg, 2.5)

    def test_pedido_sem_estrategia(self):
        with self.assertRaisesRegex(ValueError, "Defina uma estratégia"):
            Pedido(2.5).calcularFrete()

    def test_contrato_nao_pode_ser_instanciado(self):
        with self.assertRaises(TypeError):
            EstrategiaFrete()

    def test_extensao_sem_modificar_pedido(self):
        # Esta classe só existe no teste. Pedido não a importa e não sabe
        # que ela existe, mas consegue utilizá-la pelo contrato comum.
        class FretePromocional(EstrategiaFrete):
            def calcular(self, pedido: Pedido) -> float:
                return 9.0

        pedido = Pedido(2.5)
        pedido.set_estrategia(FretePromocional())
        self.assertEqual(pedido.calcularFrete(), 9.0)


if __name__ == "__main__":
    unittest.main()
