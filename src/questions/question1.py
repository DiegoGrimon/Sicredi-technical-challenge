class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return f"id={self.id}, debt={self.debt}"


class Contracts:
    def get_top_N_open_contracts(
        self,
        open_contracts: list[Contract],
        renegotiated_contracts: list[int],
        top_n: int,
    ) -> list[int]:
        """
        Gera a lista dos "top_n" devedores sem contrato renegociado

        :param open_contracts: Lista dos contratos abertos e seus débitos
        :param renegotiated_contracts: Lista dos contratos renegociados
        :param top_n: Top "N" registros que devem ser retornados pela função em ordem decrescente
        :return: Lista dos list_top_debtors

        """

        list_not_renegotiated_contracts = [
            cont for cont in open_contracts if cont.id not in renegotiated_contracts
        ]

        list_not_renegotiated_contracts.sort(key=lambda x: x.debt, reverse=True)

        list_top_debtors = [cont.id for cont in list_not_renegotiated_contracts][:top_n]

        return list_top_debtors
