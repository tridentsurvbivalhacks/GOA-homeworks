# მათემატიკური ოპერატორი:
# შექმენი ფუნქცია apply_op(a, b, func), რომელიც მიიღებს ორ რიცხვს და ერთ
# ფუნქციას. ფუნქციამ უნდა გამოიყენოს გადაწოდებული func ამ ორ რიცხვზე
# (მაგალითად, მიმატება ან გამრავლება).|

# first class function
def func(a, b):
    return a * b


# high order function
def apply_op(a, b, func):
    return func(a, b)


# store the function in a variable called "c"
# c = func
# y = apply_op(5, 4, x)
# print(y)
print(apply_op(5, 4, func))


# დაწერე ფუნქცია make_greeter(greeting), რომელიც დააბრუნებს ახალ ფუნქციას. ეს ახალი ფუნქცია კი
# მიიღებს სახელს და დაბეჭდავს მისალმებას.
# მაგალითად: say_hi = make_greeter("გამარჯობა") -> say_hi("დავით") დაბეჭდავს "გამარჯობა დავით".



def make_greeter(greeting,name): #higher order function  requieres to have 1 parameter function(greeting) and 1 parameter(name)
    return greeting(name)

#this first class function desides what to do with the second parameter(name)
def greeting(name):
    return f"gamarjoba {name}"

#we store the higher order function in a variable and give parameters 1:function 2:"sandro"
#greeting("sandro")
#what does greeting func do? it returns "gamarjoba + {name}" what is name?:"sandro"
#so final result is "gamarjoba sandro"
x1 = make_greeter(greeting,"sandro")
print(x1)


#მარტივი ფილტრი:
#შექმენი ფუნქცია my_filter(list, predicate), სადაც predicate არის ფუნქცია, რომელიც აბრუნებს True-ს ან False-ს.
#my_filter-მა უნდა დააბრუნოს სიაში მხოლოდ ის ელემენტები, რომლებზეც predicate ჭეშმარიტია.
predicate = lambda arr:True if len(arr) > 10 else False

def my_filter(arr, predicate):
    return predicate(arr)

x2 = my_filter(["sandro","daviti","giorgi","erekle","lado"],predicate)
print(x2)


#ტექსტის ტრანსფორმაცია:
#შექმენი ფუნქცია process_string(text, action), სადაც action იქნება ფუნქცია
#(მაგალითად, .upper(), .lower() ან ტექსტის შებრუნება).
action = lambda text:text.replace(text.split()[0],text.split()[1])

def process_string(text,action):#
    return action(text)         #
x3 = process_string("goa kaia",action)
print(x3)

#ფუნქციების სია:
#შექმენი ფუნქციების სია [square, cube, double]. დაწერე ციკლი,
#რომელიც ერთ კონკრეტულ რიცხვს (x = 5) გაატარებს სამივე ფუნქციაში და დაბეჭდავს შედეგებს.
square = lambda x:x**2
cube = lambda x:x**3
double = lambda x:x*2
res = [func(5) for func in [square, cube, double]]
print(res)


#Logger-ის იმიტაცია:
#დაწერე HOF სახელად safe_execute(func, x), რომელიც ცდის ფუნქციის შესრულებას.
#თუ ფუნქცია შეცდომას არ დააბრუნებს, დაბეჭდოს "Success", წინააღმდეგ შემთხვევაში – "Error".

def safe_execute(func, x):
    try:
        func(x)
        print("Success")
    except:
        print("Error")
def test_func(n):
    return 10 / n
print(safe_execute(test_func, 5))


#Multiplier Factory:
#დაწერე ფუნქცია multiplier(n), რომელიც აბრუნებს ფუნქციას,
#რომელიც თავის მხრივ მიღებულ არგუმენტს ამრავლებს n-ზე.
#გამოყენება: double = multiplier(2), double(10) -> 20.

def multiplier(n):
    def double(x):
        return x * n
    return double
print(double(10))


#List Mapper:
#დაწერე შენი საკუთარი my_map(func, items) ფუნქცია, რომელიც გადაუვლის სიას და თითოეულ ელემენტს შეუცვლის მნიშვნელობას გადაწოდებული ფუნქციის მიხედვით.
def evenorodd(items):
    res = []
    for i in items:
        res.append("Even" if i % 2 == 0 else "Odd")
    return res
def my_map(func,items):
    return func(items)
x = my_map(evenorodd, [5,68,74,1,3,7])
print(x)


#Conditional Wrapper:
# შექმენი ფუნქცია run_if_positive(func, value), რომელიც შეასრულებს გადაწოდებულ ფუნქციას მხოლოდ იმ შემთხვევაში, თუ value > 0.


def run_if_positive(func, value):
    try:
        func(value8
    excep:
        "value is less then 0"
