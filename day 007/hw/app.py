#1: მათემატიკური კალკულატორი
#შექმენი პროგრამა, რომელიც:

#შეეკითეხბა მომხმარებელს ორ რიცხვს --- მინიშნება input()
#გამოთვლის ყველა ოპერაციას (+, -, *, /, //, **, %)
#დაბეჭდავს შედეგებს

x = int(45)
y = int(5)

input(45)
input(5)

print("substraction:", x - y )
print("addition:", x + y )
print("multiply:", x * y )
print("divide:", x // y )
print("float divide:", x / y)
print("sorting:", x ** y)
print("modulus:", x % y)

#2: ლუწი თუ კენტი რიცხვი if else ის გამოყენებით <3

num = 9

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# 3: ქულების სისტემა 📊
# შექმენი ქულების სისტემა:

# აქ სულ if ებით წერეთ :)))

# 90-100: "შესანიშნავი!"
# 80-89: "კარგი!"
# 70-79: "საშუალო"
# 60-69: "ცუდი"
# 0-59: "ძალიან ცუდი"

if 90 - 100: 
    print("შესანიშნავი!")
if 80-89:
    print("კარგი!")
if 70-79:
    print("საშუალო")
if 60-69:
    print("ცუდი")
if 0 - 59:
    print("ძალიან ცუდი")

# 4: მაგარი დავალება 👌
# შექმენით კოდი რომლის გაშვების შემთხევვაში გავარკვეკთ
# აქვს თუ არა ასაკი ვინმეს ატაროოს "ზილი" ან "იკარუსი"

gela = 13
grisha = 19

if grisha < 18:
   print("ატაროოს ძილი")
else:
    print("ატაროოს იაკრუსი")

#5: ამინდის პროგნოზი 🌦️🌅
# შექმენი პროგრამა, რომელიც რეკომენდაციას გაიღებს ჩაცმულობაზე:

# თუ ცხელა (>25°) და მზიანია → "მოკლე შარვალი და მაისური"
# თუ ცივა (<10°) ან წვიმს → "ქურთუკი და ქოლგა"
# სხვა შემთხვევაში → "ჩვეულებრივი ტანსაცმელი"

temperature = 28
is_sunny = True
is_raining = False

if temperature > 25 and is_sunny:
    recommendation1 = "მოკლე შარვალი და მაისური"
if temperature < 10 or is_raining:
    recommendation2 = "ქურთუკი და ქოლგა"
else:
    recommendation3 = "ჩვეულებრივი ტანსაცმელი"

print(recommendation1)

print(recommendation3)

