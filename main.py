from src.questions.question1 import Contract, Contracts
from src.questions.question2 import Orders

if __name__ == "__main__":
    print("Question 1:")
    contracts = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5),
    ]
    renegotiated = [3]
    TOP_N = 3

    actual_open_contracts = Contracts().get_top_N_open_contracts(
        contracts, renegotiated, top_n=TOP_N
    )
    
    n_open_contracts = len(actual_open_contracts)

    if n_open_contracts:
        print(f'{"Existe apenas" if n_open_contracts == 1 else "Existem"} {n_open_contracts} {"devedor" if n_open_contracts == 1 else "devedores" } sem débitos renegociados! {f"(Solicitados: {TOP_N})" if n_open_contracts < TOP_N else ""}\nSão eles: {actual_open_contracts}')
    else:
        print(f"Não Há devedores sem débitos renegociados!")


    print("\nQuestion 2:")
    orders = [2,4,5,6,6]
    N_MAX = 100
    how_many = Orders().combine_orders(orders, n_max=N_MAX)

    print(f'{f"Serão necessárias {how_many} viagens" if how_many > 1 else f"Será necessária apenas {how_many} viagem"}')
