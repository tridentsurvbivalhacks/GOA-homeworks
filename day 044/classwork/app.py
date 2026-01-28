def abbrev_name(name):
    initial = name[0].upper() + "."
    for i in range(len(name)):
        if name[i] == " ":
            initial += name[i+1].upper()
    return initial
print(abbrev_name("Sam Harris"))

# def find_average(numbers):
#     average = 0
#     if numbers == []:
#             return 0
#     for i in numbers:
#         average += i
#     average = average / len(numbers)
#     return average
# print(find_average([5,5,8,1,6,8,10053,694]))

# def dna_to_rna(dna):
#     rna = ""
#     for i in dna:
#         if i == "T":
#             rna += "U"
#         else:
#             rna += i
#     return rna
# print(dna_to_rna("TTTTTGCA")) 

# def remove_exclamation_marks(s):
#     res = ""
#     for i in s:
#         res += i
#         if i == "!":
#             res 
#     return res
# print(remove_exclamation_marks("mfdd!njcw!n dwa!"))

# def rps(p1, p2):
#     #rock beats scissors
#     if p1 == "rock" and p2 == "scissors":
#         return "Player 1 won!"
#     elif p1 == "scissors" and p2 == "rock":
#         return "Player 2 won!"
#     #scissors beat paper
#     elif p1 == "scissors" and p2 == "paper":
#         return  "Player 1 won!"
#     elif p1 == "paper" and p2 == "scissors":
#         return "Player 2 won!"
#     #Paper beats rock
#     elif p1 == "paper" and p2 == "rock":
#         return "Player 1 won!"
#     elif p1 == "rock" and p2 == "paper":
#         return "Player 2 won!"
def points(games):
    total = 0
    for i in games:
        if i[0] > i[2]:
            total += 3
        elif i[0] < i[2]:
            total += 0
        elif i[0] == i[2]:
            total += 1
    return total
print(points(["3:1", "2:2","0:1"])) 