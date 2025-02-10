from typing import List

class Orders:
    def combine_orders(self, requests: List[int], n_max: int) -> int:
        """
        Método deve combinar as viagens dos malotes limitado ao valor 'n_max' e 2 pedidos por vez

        :param requests: requests dos valores dos pedidos de dinheiro
        :param n_max: valor maximo que pode ser agrupado por remessa
        :return: Retorna o número de viagens que precisam ser realizadas

        """
        excedentes = 0
        requests.sort(reverse=True)

        # Check valor malote excedente
        for i in range(len(requests)):
            if requests[i] > n_max:
                print(
                    f"ATENÇÃO: A requisição de valor {requests[i]} excede o limite do malote ! \nPor segurança a mesma não será agrupada."
                )
                excedentes += 1

        for i in range(excedentes):
            requests.pop(0)

        # Combine requests
        combine_orders = []
        i = 0
        while i < len(requests):
            encontrou_par = False
            for j in range(i + 1, len(requests)):
                if requests[i] + requests[j] <= 100:
                    combine_orders.append((requests[i], requests[j]))
                    requests.pop(j)
                    encontrou_par = True
                    break
            if not encontrou_par:
                combine_orders.append((requests[i],))
            i += 1

        print(f"Agrupamento: {combine_orders}")

        return len(combine_orders)
