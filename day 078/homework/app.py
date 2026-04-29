# lomialika = lambda x,*args,**kwargs:f"{kwargs['name2']} aris {x} wlis da {args[1]}"
# y = lomialika(13,"kargi biwia","cudi biwia",name1="sandro",name2="gio",name3="lomi")
# print(y)


#1) *args
#შექმენი ფუნქცია, რომელიც მიიღებს უსასრულო რაოდენობის რიცხვებს *args-ით და დააბრუნებს მათ ჯამს.
def func(*infinite):
    return sum(infinite)
y = func(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(y)

#2) **kwargs
# შექმენი ფუნქცია, რომელიც მიიღებს სტუდენტის მონაცემებს **kwargs-ით და დაბეჭდავს ლამაზად.
def student(**data):
    return f"name: {data["name"]} age: {data["age"]} color: {data["color"]}"
z = student(name = "sandro",age = "14",color = "black")
print(z)

#3) კლასი + init
# შექმენი კლასი Car, რომელსაც ექნება:
# brand
# model
# year
# ინიციალიზაცია გაუკეთე.
class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        return f"brand: {self.brand}. model: {self.model}. year: {self.year}"

e = Car("lamborghini","Revuelto",2023)
print(e.info())


#დაამატე მეთოდი info(), რომელიც დაბეჭდავს მანქანის ინფორმაციას.


# 4) args + კლასი
# შექმენი კლასი Calculator, რომელსაც ექნება მეთოდი და რომელიც აბრუნებს ყველა გადაცემული რიცხვის ჯამს.

class Calculator():
    def __init__(self,*numbers):
        self.numbers = numbers
    def returner(self):
        return sum(self.numbers)

r = Calculator(2,3,4,5,7)
print(r.returner())

# 5) kwargs + OOP
# შექმენი კლასი User, რომელიც მიიღებს **kwargs-ს __init__-ში.
# მოთხოვნები:
# ყველა გადაცემული key/value შეინახოს ობიექტში
# დაამატე მეთოდი get_info(), რომელიც აბრუნებს ყველაფერს dictionary-ად

class User():
    def __init__(self,**user_information):
        self.user_info = user_information

    def get_info(self):
        return self.user_info

g = User(name="dato", age=20, city="tbilisi")
print(g.get_info())
