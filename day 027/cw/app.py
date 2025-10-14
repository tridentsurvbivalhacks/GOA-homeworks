list = []
for i in range (50):
   if i % 2 != 0:
    list.append(i)
print(list)

#3) შექმენი ფუნქცნია lion3() სადაც მისალმების ფუნქცია იქნება და თქვენ სახელს თუ ჩაწერთ გამოგიგდებთ თქვენს სახელს მაგალითად + "მე ვარ დავით ლომი" შედეგს <3 
def lion3():
    return str(input("enter your name: "))
print(f"me var {lion3()} lomi")