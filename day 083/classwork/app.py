# 1) create Dog class with

# use Polimorphos and Encapuslation

# create one private method
# crete one public method

# create dog instance
# public name
# private age

class Dog:
    def __init__(self,name,age):#create dog instance
        self.name = name    #public name
        self.__age = age    #private age Encapuslation

    def info_printer(self):     #crete one public method
        return f"name:{self.name} age: {self.__age}" #Polimorphos
    def __fake_info_printer(self):  #create one private method EncapuslationS
        return f"name {self.name} age: {self.__age}"#Polimorphos

x = Dog("maxi",5)
print(x.info_printer())#Polimorphos
