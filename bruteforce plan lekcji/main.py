def calculate_change(nominals: list[int], amount: int) -> list[int]:
    for nominal in nominals:

        if amount == nominal:
            return [nominal]
        while expected_solution != amount:
            pass


# nominals = [1, 2, 5, 10, 20, 50]
# amount = 51
# expected_solution = [1,50]

# result = calculate_change(nominals, amount)

# assert result == expected_solution, f"got: {result}, expected: {expected_solution}"

# print(result)


def f1(nominals):  # tu generujemy kombinacje jednoelementowe
    result = []
    for nominal in nominals:
        result.append([nominal])

    return result


def f1git(nominals):
    return [[nominal1] for nominal1 in nominals]


def f2(nominals):  # tu generujemy kombinacje 2elementowe
    result = []
    for nominal1 in nominals:
        for nominal2 in nominals:
            result.append([nominal1, nominal2])

    return result


def f2git(nominals):
    return [[nominal1, nominal2] for nominal1 in nominals for nominal2 in nominals]


result = f2git([0, 1, 2, 3, 4, 5, 6, 7, 98])

print(result)
