# def diagonal_sum(array):
#     count = -1
#     res = 0
#     for subarray in array:
#         count += 1
#         res += subarray[count]
#     return res
# print(diagonal_sum([[3,8,2],[2,4,7],[9,1,1]]))

# def capitals_first(text):
#     for i in text:
        
#     words = text.split()      
#     upper = []                 
#     lower = []                
#     for word in words:
#         first_char = word[0]
#         if first_char == first_char.upper():
#             upper.append(word)
#         else:
#             lower.append(word)
#     return " ".join(upper + lower)
# print(capitals_first("123 You Me baby and' should equal 'You Me baby and"))



# def is_isogram(string):
#     string = string.lower()
#     letters = []
#     for i in string:
#         letters.append(i)
#     res = ""
#     for i in letters:
#         if letters.count(i) <= 1:
#             res += i
#     return res == string
# print(is_isogram("ZknwGvV"))


# def xo(s):
#     string = s.lower()
#     if string == "":
#         return True
#     x_count = 0
#     o_count = 0
#     for i in string:
#         if i == "x":
#             x_count += 1
#         elif i == "o":
#             o_count += 1
#     return x_count == o_count
# print(xo("zzoo"))

def remove_exclamation_marks(s):
    res = ""
    for i in s:
        if i != "!":
            res += i
    return res
print(remove_exclamation_marks("Oh, no!!!"))