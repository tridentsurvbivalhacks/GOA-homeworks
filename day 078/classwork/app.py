lomialika = lambda x,*args,**kwargs:f"{kwargs['name2']} aris {x} wlis da {args[1]}"
y = lomialika(13,"kargi biwia","cudi biwia",name1="sandro",name2="gio",name3="lomi")
print(y)


class Animal:
    def __init__(self,name,age,jeison_born,color):
        self.name = name
        self.age = age
        self.jeison_born = jeison_born
        self.color = color
info1 = Animal("alika",83,False,"yellow")
info2 = Animal("lomi",14,True,"green")
print(info2.name,info2.age,info2.color)
print(info1.name,info1.age,info1.jeison_born,info1.color)
