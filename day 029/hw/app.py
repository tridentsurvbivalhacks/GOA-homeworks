#1) შექმენი ფუნქცნია lion() სადაც  5 ელემენტიანი მასივი რომელიშ გამოიყენებთ .index() მეთოდს
def lion():
    return [1, 2, 3, 3, 4, 5, 5]
lion()
print(lion().index(3))
# 2) შექმენი ფუნქცნია lion2() სადაც შექმენი 5 ელემენტიანი მასივი [1,1,1,1,1,1,1,2] რომელიშ გამოიყენებთ .index() მეთოდს და მიწვდებით ბოლო ელემენტს მხოლოდ index() !!!
def lion2():
    #       0  1  2  3  4  5  6  7  8  index
    return [1, 1, 2, 2, 3, 3, 4, 4, 5]
lion2()
print(lion2().index(5))
#3) შექმენი ფუნქცნია lion3() სადაც მისალმების ფუნქცია იქნება და თქვენ სახელს თუ ჩაწერთ გამოგიგდებთ თქვენს სახელს მაგალითად + "მე ვარ დავით ლომი" შედეგს <3 
def lion3():
    return str(input("enter your name: "))
print(f"me var {lion3()} lomi")
# 4) შექმენი ფუნქცნია lion4() სადაც შევქმნით ცარიელ მასივს და for loop ის გამოყენეით + .appnd() შევიტანთ მხოლოდ კენტ რიცხვებei 
def lion4(): # create function
    empty = [] # create empty massive
    for i in range(50): #cycle in range 50
     if i % 2 != 0: #check the conditions
        empty.append(i) #add elements to the empty massive with the help of condition
    return empty
print(lion()) #printed the whole function


#5) შექმენი ფუნქცნია lion5() სადაც მომხმარებელს შეეკითხებით სანამ პაროლს არ გამოიცნობს მანამდე დაუწეროს "პაროლი არასოწორია" მინიშნება while loop ი გამოიყენეთ
def lion5():
    password = "sandro123"
    enter_password = (input("enter your password: "))
    while enter_password != password:
        enter_password = input("enter password again: ")
    print("correct")
lion5()
    

#6) კომენტარების სახით ახსენით რა არის array და def
#array aris igive masivi da igivenaerad ezaxian arrays listis magivrad
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# "def" aris igive funqciis sheqmna romelic gamoiyeneba funcqciashi da mas sheizleba qondes sxvadasxva raodenobis parametrebi
def lomi(a):   #def create function called lomi() with 1 parameter
    return a             #single parameter function
print(lomi("hello world"))

def lomi1(a, b):
    return a + b         #2 parameter function
#parameter     a             b
print(lomi1("sandro", " miqelashvili"))
#7) შექმენით array სადაც შეინახავთ მრავალ მონაცემს და გამოიტანეთ ტერმინალში რამდენჯერ გაქვთ რაიმე თქვენ მიერ არჩეული მონაცემი
array = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8, 9, 10]
print(array.count(5))
# 8) შექმენით ფუნქცია რომელიც გაამრავლებს ორ მონაცემს
def lion6(a, b):
    return a * b
print(lion6(9, 6))
#9)მოცემულია სია animals = ["Lion", "Tiger", "Frog", "Panda", "Deer", "Elephant", "Fox"].
# დაბეჭდე ყოველი მეორე და მესამე ელემენტები გამოიყენეთ indexing (მინუს ინდექსებითაც)
animals = ["Lion", "Tiger", "Frog", "Panda", "Deer", "Elephant", "Fox"]
print(animals[::2])
print(animals[::3])
print(animals[::-2])
print(animals[::-3])