#1
class Dog:
    def __init__(self,name="cuga",age = 2):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"name:{self.name} age:{self.age}"
    def greeting(self):
        return "gamarjoba"
x = Dog()
print(x)
#2

class Characteristics:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    
    def take_damage(self, amount):
        self.health -= amount

class warrior(Characteristics):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
    
    def __str__(self):
        return f"Health: {self.health}, Damage: {self.damage}, Speed: {self.speed}"
w = warrior(100,20,70)
w.take_damage(50)
print(w)
w.take_damage(20)
print(w)