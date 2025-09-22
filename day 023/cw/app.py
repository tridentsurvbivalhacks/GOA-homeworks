a = "lom ki ara lekvi kide!"
print(len(a))

# 1) მოცემული ინფორმაციის მიხედვით გამოიყენეთ for loop და თითო ელემენტს მიწვედით ინდექსით ხოლო პრინტით კი გამოიტანეთ ტერმინალში <3

for i in range(len(a)):
    print(a[i])

# 2)
# მოცემული კოდში შევქმანთ ახალი new_a ში შევინახოთ იგივე წინანადადება რაც გვქონდა a ში ოღონდ " " / სფეისების გარეშე
a = "lom ki ara lekvi kide!"
print(len(a))
new_a = ""
## ამ ხაზის ქვემოთ შეცვალეთ კოდი მხოლოდ <3

for i in range(len(a)):
    if a[i] != " ":
     new_a += a[i]
print(new_a)
print(a)

#===============================================PRACTICE====================================#
b = "sandro aris 14 wlis teenager"
new_b = ""
print(len(b))

for i in range(len(b)):
   if b[i] != " ":
    new_b += b[i]
print(new_b)