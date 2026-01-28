def matrix(array):
    count = -1
    for list in array:
        count += 1
        if list[count] < 0:
            list[count] = 0
        else:
            list[count] = 1
    return array
print(matrix([
  [-1,  4, -5, -9,  3 ],
  [ 6, -4, -7,  4, -5 ],
  [ 3,  5,  0, -9, -1 ],
  [ 1,  5, -7, -8, -9 ],
  [-3,  2,  1, -5,  6 ]
]))