# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 - value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '/':
#         return value1 / value2
# print(basic_op('/',49,7))

# def area_or_perimeter(l , w):
#     if l == w:
#         return w * l
#     elif w != l:
#         return w*2 + l*2

def points(games):
    sum = 0
    team1 = games[0]
    team2 = games[2]
    for i in games:
        if team1 > team2 :
            sum += 3
        elif team1 < team2:
            sum += 0
        elif team1 == team2:
            sum += 1
    return sum
print(points(["3:1", "2:2","0:1"]))
