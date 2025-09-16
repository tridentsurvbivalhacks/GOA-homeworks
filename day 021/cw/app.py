array = ["ak47", 5, False, True, 2, "sandro", 4, "maxi", "davit", 21]
print(len (array))

for i in range (len(array)):
   print(i)

#              0  1  2  3  4  5  6  7  8  9
slice_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


print(slice_array[::]) #array
print(slice_array[::-1]) #reverse array
print(slice_array[9:0:-1])


#---------------------------------------------------------PRACTICE------------------------------------------------------------------------#
password = 923
guess = int(input("Enter the password: "))
while password != guess:
   guess = int(input("Incorrect try again: "))
print("You're Correct")