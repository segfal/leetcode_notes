
def climb(n : int) -> int:
    if n < 3:
        return n

    first_case = 1
    second_case = 2
    res = 0
    for i in range(3, n+1):
        res = first_case + second_case
        first_case = second_case
        second_case = res
    return res

print(climb(32))def climb(n : int) -> int:
    if n < 3:
        return n

    first_case = 1
    second_case = 2
    res = 0
    for i in range(3, n+1):
        res = first_case + second_case
        first_case = second_case
        second_case = res
    return res

print(climb(32))
