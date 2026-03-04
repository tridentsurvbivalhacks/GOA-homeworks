a = [x * 10 for x in range(5, 9)]
print(a)


def even_odd(n):
    if n % 2 == 0:
        return "Even"


print("map", list(map(lambda n: n if n % 2 == 0 else None, [1, 2, 3, 4, 5])))
print("filter", list(filter(lambda n: n if n % 2 == 0 else None, [1, 2, 3, 4, 5])))
