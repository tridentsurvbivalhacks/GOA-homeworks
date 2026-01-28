# def maskify(cc):  
#     if len(cc) <= 4:
#         return cc
#     return ("#" * (len(cc) - 4) + cc[-4:])
# print(maskify("skippy"))

# def accum(st):
#     res = ""
#     count = 0
#     for i in range(len(st)):
#         count = i
#         res += st[i].capitalize() + st[i].lower() * count + "-"
#     return res[:-1]
# print(accum("abcd"))


def is_anagram(test, original):
    if len(test) != len(original):
        False
    original = original.lower()
    test = test.lower()
    count = 0
    for i in test:
        if i in original:
            count += 1
    return count == len(test)
    
