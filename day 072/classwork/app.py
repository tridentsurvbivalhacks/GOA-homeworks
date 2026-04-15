# A factorial is the product of
# all positive integers less than or equal to a number. For example, 5! (read: "five factorial") is 5 * 4 * 3 * 2 * 1, which is 120.
def factorial(n):  # 5
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
