# 1) კომენტარის სახით ახსენით რა არის Polymorphism, Encapsulation, instance
#polimorphos - methodebi,funcqciebi romelic gamoiyeneba pythonshi
#Encapsulation - private method romlitac shegizlia private objectebi,funcqciebi da cvladebi sheqmna
#instance - aris Classebshi initializeba romelic xdeba def __init__ am dros shen inicializebs uketeb parametrebs da obieqtebs
#mokled ro tqvat instance aris object sheqmnili classis gan romelsac qmni def __init__-it

#2) შექმენით კლასი Car, რომელსაც ექნება:
   # brand
   # year
   # დააწერეთ მეთოდი info(), რომელიც დააბრუნებს:
   # "This car is BMW from 2020"

class Car:
    def __init__(self,brand,year) -> None:
        self.brand = brand
        self.year = year

    def info(self):
        return f"This car is {self.brand} from {self.year}"

car1 = Car("BMW","2020")
print(car1.info())


# 3)შექმენით კლასი Vehicle:
#   name, speed
#   მეთოდი:
#   move() → "The vehicle is moving"
#   შემდეგ შექმენით კლასი Bike, რომელიც იღებს Vehicle-ს
#   და გადააკეთეთ move():
#   "The bike is moving fast"

class Vehicle:
    def __init__(self,name,speed) -> None:
        self.name = name
        self.speed = speed

    def move(self):
        return "The vehicle is moving"

class Bike(Vehicle):
    def __init__(self, name, speed) -> None:
        super().__init__(name, speed)

    def move(self):
        return f"the {self.name} is moving {self.speed}"

bike1 = Bike("bike","slow")
print(bike1.move())


# 4)შექმენი 2 კლასი:
#   Bird
#   Fish
#   ორივეს ჰქონდეს მეთოდი move()
#   მაგრამ:
#   Bird → "Flying"
#   Fish → "Swimming"
#   შექმენი ობიექტები და გამოიძახე ორივეზე move()

class Bird:
    def __init__(self,name) -> None:
        self.name = name

    def move(self):
        return f"{self.name}(bird) is Flying"

class Fish:
    def __init__(self,name) -> None:
        self.name = name

    def move(self):
        return f"{self.name}(fish) is Swimming"

fish1 = Fish("bobi")
print(fish1.move())
bird1 = Bird("laura")
print(bird1.move())
