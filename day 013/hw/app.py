"""
1)ახსენი ერთ წინადადაში რას აკეთებს for loop Python-ში
"""
#for loop არის ერთერთი ფუნქცია რომლითაც შეგვილია iteration გავაკეთოთ რამდენჯერაც გვინდა.
"""
2)მომხმარებელს შემოაყვანინე რიცხვი და დაბეჭდე, დადებითია თუ უარყოფითი.

"""

num = int(input("first question number : " ))
if num > 0:
    print("დადებითი რიცხვია")
else:
    print("უარყოფითი რიცხვია")
"""
3)მომხმარებელს შემოაყვანინე რიცხვი და დაბეჭდე კენტის შემთხვევაში კენტი ლეწის შემთხვევაში ლუწი
"""

num = int(input("second question number: " ))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


"""
4)მომხმარებელს შემოაყვანინე გამოცდის ქულა თუ მიიღო 100 დაბეჭდოს მალადეც თუ მიიღო 50 ნაკლები ვერ ჩააბარე 

"""
point = int(input("How many points did you get?:" ))
if point >= 100:
    print("მალადეც!")
else: 
    print("ვერ ჩააბარე.")

"""
5)სხვადასხვა მაგალითი მოიყვანეთ (მინიმუმ 5-5) ლუწების და კენტების (მოკლეთ იმუშავეთ ლუწებზე და კენტებზე)

"""
#1
num - 3
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#2
for i in range(10):
 if i % 2 == 0:
    print("Even"+ str(i))
 else:
    print("Odd" + str(i))
#3
num - int(input("number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
#4
num - 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")