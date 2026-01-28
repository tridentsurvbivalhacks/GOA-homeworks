# def reverse_words(text):
#     result = ""
#     word = ""
#     for char in text:
#         if char == " ":
#             result += word[::-1] + " "
#             word = ""
#         else:
#             word += char

#     result += word[::-1]
#     return result
# print(reverse_words('Thisisanexample!'))
# print(reverse_words('Thisisanexample!'))

# def divisors(n):
#     res = 0
#     if n % 1 or 2 or 3 or 4 == 0:
#         res += 1
#     return res
# print(divisors(4))

# def sort_by_length(arr):
#     min = arr[1]
#     max = arr[1]
#     for i in arr:
#         if len(i) > len(max):
#             max = i
#         elif len(i) < len(min):
#             min = i 
#     arr1 = [min,max]    
#     return arr1

# print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))