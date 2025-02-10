import unittest
from src.questions.question2 import Orders

class Question2Test(unittest.TestCase):
    def test_default(self):
        """
        Teste Default do Readme.md.
        """
        orders = [70, 30, 10]
        n_max = 100
        expected_travels = 2

        travels = Orders().combine_orders(orders, n_max)

        self.assertEqual(travels, expected_travels)


    def test_orders_greater_than_nmax(self):
        """
        Teste Order com um dos valores superior a n_max.
        O mesmo será ignorado da lista e as demais agrupados
        """
        orders = [120, 15, 50, 30, 90, 20, 40, 60, 20, 20]
        n_max = 100
        expected_travels = 5

        travels = Orders().combine_orders(orders, n_max)

        self.assertEqual(travels, expected_travels)


    def test_orders_equals_100(self):
        """
        Teste com uma Order de valor igual a n_max
        A mesma será enviada em um malote único
        """
        orders = [100, 60, 40, 70, 30, 10, 40, 60, 40]
        n_max = 100
        expected_travels = 5

        travels = Orders().combine_orders(orders, n_max)

        self.assertEqual(travels, expected_travels)


if __name__ == "__main__":
    unittest.main()
