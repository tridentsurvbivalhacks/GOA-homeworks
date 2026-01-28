# def capitalize(s):
#     res = ""
#     for i in range(len(s)):
#         if i % 2 == 1:
#             res += s[i].capitalize()
#         else:
#             res += s[i].lower()
#     new_res = []
#     new_res.append(res)
#     # return  new_res
#     res = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             res += s[i].capitalize()
#         else:
#             res += s[i].lower()
#     new_res1 = []
#     new_res1.append(res)
#     return new_res1 + new_res
# print(capitalize("ab"))

# def fizzbuzz(n):
#     array = []
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             array.append("FizzBuzz")
#         elif i % 3 == 0:
#             array.append("Fizz")
#         elif i % 5 == 0:
#             array.append("Buzz")
#         else:
#             array.append(i)
#     return array
# print(fizzbuzz(10))
# #expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']


# def greet(name): 
#     res = f"Hello {name[0].capitalize()}{name[1:].lower()}!"
#     return res
# print(greet("R"))

# def vaporcode(s):
#     res = ''
#     for i in s:
#         if i == ' ':
#             pass
#         else:
#             res += f"{i.capitalize()}  " 
#     return res[:-2]
# print(vaporcode("Why isn't my code working?"))

# def reverse_number(n):
#     if n == 1000:
#         return 1
#     rev = ''
#     for i in str(n):
#         rev += i
#     rev = rev[::-1]
#     if rev[-1] == "-":
#         rev = "-" + rev[:-1]
#     return int(rev)
# print(reverse_number(456)

