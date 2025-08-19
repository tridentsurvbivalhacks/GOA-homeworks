"""
1) ინდენტაცია საჭიროა თუ არა და რატომ for loop ის დროს, მოიყვანეთ მაგალითები და ახსენით კომენტარით


"""

for i in range(3):
    print("sandro") # იდენტაცია 
print("gorila") # იდენტაციის დაცვის გარეშე
#თუ იდენტაციას არ დაიცავ ფუნქცია იმუშავებს for loop-ის გარეთ და 3-ჯერ gorila-ს დაპრინტვის მაგივრად რამდენჯერას დაპრინტეთ იმდენჯერ დაპრინტავს ანუ (1)
#და თუ დაიცავთ იდენტაციას for loop ში ჩაჯდება "print("gorila")" და sandro=ს და gorila-ს დაპრინტავს რამდენიც მიუთითეთ range-ში ანუ (3)
for i in range(3):                                                                        #sandro                
    print("sandro")                                                                       #gorila
    print("gorila")                                                                       #sandro                                                                                                         #gorila 
#                                                                                         #gorila
#                                                                                         #sandro
#                                                                                          #gorila
"""
2) for loop-ის მეშვეობით გამოიტანეთ რიცხვი 4, 7-ჯერ.

"""
for i in range(7):
    print(4)

"""
3) for loop-ის მეშვეობით გამოიტანეთ "I love cats" 8-ჯერ.

"""
for i in range(8):
    print("i love cats")

"""
4) Input()-ის გამოყენებით მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ for loop-ით კი დაპრინტეთ ("hello" + მომხმარებლის სახელი) 5 ჯერ.

"""
name = input("რა გქვია?: ")
for i in range(5):
    print("hello " + (name))

"""
5) შევასწოროთ შეცდომები:

for i in range5
print("i")

"""
for i in range(5):
    print(i)
    