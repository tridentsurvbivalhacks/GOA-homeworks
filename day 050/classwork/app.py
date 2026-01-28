# def min_max(lst):
#   min = lst[0]
#   max = lst[0]
#   for i in lst:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
#   return [min, max]
# print(min_max([1,2,3,4,5]))

def remove_smallest(numbers):
    if numbers == []:
        return []
    
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    array = numbers.copy()
    for i in range(len(array)):
        if array[i]
print(remove_smallest([1, 2, 3, 1, 1]))


# def number(lines):
#     if lines == []:
#         return []
#     res = []
#     count = 0
#     for i in range(0,len(lines)):
#         count += 1
#         res.append(f"{count}: {lines[i]}")
#     return res
# print(number(["a","b","c"]))