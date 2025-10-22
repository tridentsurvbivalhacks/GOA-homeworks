#1) მომხმარებელს შემოატანინეთ ერთი რიცხვი და შექმენი ფუნქცია რომელიც შეამოწმებს არის თუ არა რიცხვი ლუწი ან კენტი
def func(num):
    if num % 2 == 0:
        return "Even"
    else: 
        return "Odd"
print(func(6))
# 2) მომხმარებელს შემოატანინეთ ერთი რიცხვი და შექმენი ფუნქცია რომლითაც გაიგებ არის თუ არა ეს რიცხვი დადებითი თუ უარყოფითი
# this
def func1(num1):
    if num1 > 0:
        return "es ricxvi aris dadebiti"
    elif num1 == 0:
        return "es ricxvi arc dadebitia arc uaryofiti"
    else:
        return "es ricxvi aris uaryofiti"
print(func1(-24))
#3) მომხარებელს შემოატანინეთ ორი რიცხვი და შექმენი ფუნქცია რომელიც შეადარებს რომელია უფრო დიდი
def func2(a, b):
    if a > b:
        return  str(a) + " aris ufro didi"
    else:
        return  str(b) + " aris ufro didi"
print(func2(50, 61)) 
# 4) დაწერე პროგრამა, რომელიც მომხმარებლისგან შეიტანს სტუდენტის მიღებულ ქულას (0-დან 100-მდე) და გამოიტანს შესაბამის ნიშანს დამოკიდებულს ქულაზე:
# ქულა        ნიშანი
# 90 – 100      A
# 80 – 89       B
# 70 – 79       C
# 60 – 69       D
# 0 – 59        F
def func3(num2):
    if num2 > 100:
        return "ar sheizleba 100ze meti"
    elif 100<=num2<=90:
        return f"Your score: {num2}, your grade: A"
    elif 89<=num2<=80:
        return f"Your score: {num2}, your grade: B"
    elif 70<=num2<=79:
        return f"Your score: {num2}, your grade: C"
    elif 60<=num2<=69:
        return f"Your score: {num2}, your grade: D"
    elif 0<=num2<=50:
        return "F"
    else:
        return "ricxvi ar chagiweriat"
print(func3(71))
# 5) მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში.
# თუ ტემპერატურა 0-ზე ნაკლებია დააბრუნეთ “Today is very cold! Wear warm clothes 💙”,
# თუ 0–30 შორისაა → დაპრინტეთ “Today is a really nice weather 🥰”,
# თუ 30-ზე მეტია → დაპრინტეთ “Today is very hot! Drink plenty of water 🔥”.
def func4(temperature):
    if temperature < 0:
        return "today is very cold wear warm clothes"
    elif temperature >= 0 and temperature <= 30:
        return "today is a really nice weather"
    elif temperature > 30:
        return "today is very hot! Drink plenty of water"
    else:
        return "you dont know the temperature?"
print(func4(23))