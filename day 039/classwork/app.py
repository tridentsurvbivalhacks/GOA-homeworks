# def repeat_str(s,n):
#     for i in range(n):
#         return s
# print(repeat_str("hello", 3))
# n = 5
# s = "hello"
# for i in range(n):
#     s = s + s[i]
# print(s)
def remove_char(s):#function to remove first and last character
    return s[1:-1] #1 is first and -1 is last so we used slicing to type this so it could return the characters after the first character and before the last character and we only used start and stop (start:stop:step)
print(remove_char("sandro"))


# def square_sum(numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i*i
#     return sum
# print(square_sum([1, 2, 2]))
# numbers = [1, 2, 3]
# sum = 0
# for i in numbers:
#     sum = sum + i*i
# print(sum)

def find_smallest_int(arr):
    smallest = [0]
    for i in arr: #cycle through every number in this list
        if smallest > i : #check the conditions
            smallest = i #update the variable if the condition is true
    return smallest #return the updated value
print(find_smallest_int([[34, -345, -1, 100]]))#give the value to the parameter and print out the function