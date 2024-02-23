def calculate_change(nominals: list[int], amount: int) -> list[int]:
    for nominal in nominals:
        if amount == nominal:
            return [nominal]


nominals = [1, 2, 5, 10, 20, 50]
amount = 74
expected_solution = [2,2,20,50]

result = calculate_change(nominals, amount)

assert result==expected_solution, f'got: {result}, expected: {expected_solution}'



