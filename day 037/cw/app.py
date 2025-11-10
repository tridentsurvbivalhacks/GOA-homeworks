#1
def func1(a):
    return a ** 2
print(func1(5))
print(func1(-5))
print(func1(10))
print(func1(100))
print(func1(7))

#2

def positive_sum(arr):
    arr = [1, -4, 7, 12]
    sum = 0
    for i in range(len(arr)):  # i = 0|1  sum = 1
        if arr[i] > 0:         # i = 1|-4 sum = 1
            sum += arr[i]      # i = 2|7  sum = 1+7 = 8
    return sum
print(positive_sum)  # i = 3|12 sum = 8 + 12 = 20

#----------------------------------------------------------------------------------------------------------------------------#
def positive_sum(arr):
    arr = [1, -4, 7, 12]
    if arr < 0:
        return arr