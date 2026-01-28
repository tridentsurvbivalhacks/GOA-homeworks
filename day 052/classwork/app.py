# def number(bus_stops):
#     res = []
#     for i in bus_stops:
#         res.append(i[0] - i[1]) 
#     res2 = 0
#     for i in res:
#         res2 += i
#     return res2
# print(number([[10,0],[3,5],[5,8]]))



def sequence_sum(begin_number, end_number, step):
    res = []
    for i in range(begin_number,end_number + 1,step):
        res.append(i)
    sum = 0
    for i in res:
        sum += i
    return sum
print(sequence_sum(2,6,2))

