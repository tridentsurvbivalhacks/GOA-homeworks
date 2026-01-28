# def count_by(x, n):
#     """
#     Return a sequence of numbers counting by `x` `n` times.
#     """
#     array = []
#     for i in range(x * n + 1):
#         array.append(i)
#     return array[x::x]
# print(count_by(3,5))

# def type_validation(variable, _type):
#     return _type in str(type(variable))
# print(type_validation(43, "int"))

# def two_decimal_places(number):
#     return round(number,2)
# print(two_decimal_places(5.5589))

def descending_order(num):
    res = ""
    num = str(num) #"145263"
    for i in num:
        if i > num:
            res += i
    return res
print(descending_order(145263))