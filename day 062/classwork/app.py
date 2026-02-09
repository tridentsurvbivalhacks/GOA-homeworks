# list = [
#     {
#         "name":"sandro",
#     },
#     {
#         "name":"zviadi",
#     },
    
#     {
#         "name":"davit",
#     },
    
#     {
#         "name":"mp5",
#     }
# ]
# for i in list:
#     print(i["name"])


#--------------------------------------PRACTICE----------------------------------------
#The Evens Multiplier
def multiply_evens(numbers):
    res = [i * 100 for i in numbers if i % 2 == 0]
    return res
print(multiply_evens([1,2,3,4,5,6]))

