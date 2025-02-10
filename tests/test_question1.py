import unittest
from src.questions.question1 import Contract, Contracts

class Question1Tests(unittest.TestCase):
    def test_default(self):
        """
        Teste Default do Readme.md.
        :return:
        """
        contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5),
        ]
        renegotiated = [3]
        top_n = 3

        actual_open_contracts = Contracts().get_top_N_open_contracts(
            contracts, renegotiated, top_n
        )

        expected_open_contracts = [5, 4, 2]
        self.assertEqual(expected_open_contracts, actual_open_contracts)

    def test_get_5_top_n_contracts(self):
        """
        Teste para obter os 5 list_top_debtors
        :return:
        """
        contracts = [
            Contract(1, 100),
            Contract(2, 200),
            Contract(3, 300),
            Contract(4, 400),
            Contract(5, 500),
            Contract(6, 600),
            Contract(7, 700),
            Contract(8, 800),
            Contract(9, 900),
            Contract(10, 1000),

        ]
        renegotiated = [9, 7, 6]
        top_n = 5

        list_top_debtors = Contracts().get_top_N_open_contracts(
            contracts, renegotiated, top_n
        )

        expected_list_top_debtors = [10, 8, 5, 4, 3]
        self.assertEqual(expected_list_top_debtors, list_top_debtors)


if __name__ == "__main__":
    unittest.main()
