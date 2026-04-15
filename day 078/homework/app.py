# lomialika = lambda x,*args,**kwargs:f"{kwargs['name2']} aris {x} wlis da {args[1]}"
# y = lomialika(13,"kargi biwia","cudi biwia",name1="sandro",name2="gio",name3="lomi")
# print(y)


#1) *args
#შექმენი ფუნქცია, რომელიც მიიღებს უსასრულო რაოდენობის რიცხვებს *args-ით და დააბრუნებს მათ ჯამს.
def func(*infinite):
    return sum(infinite)
x = func(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(x)

#2) **kwargs
# შექმენი ფუნქცია, რომელიც მიიღებს სტუდენტის მონაცემებს **kwargs-ით და დაბეჭდავს ლამაზად.
def student(**data):
    return f"name: {data["name"]} age: {data["age"]} color: {data["color"]}"
x = student(name = "sandro",age = "14",color = "black")
print(x)