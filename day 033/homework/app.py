#1) ახსენი  რას ნიშნავს “default value” ფუნქციის პარამეტრებში.
def func(a):
    return f"ra ggqvia?  {a}"
print(func("sandro")) #sandro aris a parametris value 
#default value nishnavs igive chveulebriv values
def func(a, b):
    return f"ra aris sheni saxeli da gvari?:  {a}"
print(func("sandro", "miqelashvili"))
#2) ახსენით return ის მნიშვნელობა.
#return function-ში გვიბრუნებს მაგ ფუნქციაში დაწერილ კოდებს ან რაც ჩვენ გვინდა გამოვიტანოტ return ასრულებს იგივე პრინტის ფუნქციას მაგრამ მას ტერმინალში არ გამოაქ
#4)  შექმენით ფუნქცია სახელწოდებით multiply, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ პასუხად უნდა დააბრუნოს ამ რიცხვების ნამრავლი.
def multiply(a, b):
    return a * b
print(multiply(5,9))
#5) შექმენით ფუნქცია სახელწოდებით divide, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ პასუხად უნდა დააბრუნოს ამ რიცხვების განაყოფი.
def divide1(c, d):
    return c / d
print(divide1(45, 9))
#second variant
def divide2(e, f):
    return e // f
print(divide2(45, 9))