#დავალება 1: "Repeat-მანქანა" (Closure)დაწერე ფუნქცია make_repeater(n), რომელიც აბრუნებს ახალ ფუნქციას. ეს დაბრუნებული ფუნქცია უნდა იღებდეს ტექსტს და აბრუნებდეს 
# მას $n$-ჯერ გამეორებულს.მაგალითი: repeat5 = make_repeater(5) -> print(repeat5("გოა")) უნდა დაბეჭდოს "გოა" 5-ჯერ.

def make_repeater(n):
    def closurefunction(t):
        return t * n
    return closurefunction         #t * n ("გოა * 5")
print(make_repeater(5)("გოა"))

#დავალება 2: "საიდუმლო ბანკი" (Nonlocal & Closure)შექმენი ფუნქცია bank_account(initial_balance), რომელიც შიგნით ინახავს ბალანსს. მან უნდა 
# დააბრუნოს ფუნქცია withdraw(amount), რომელიც ყოველ გამოძახებაზე დააკლებს თანხას საწყის ბალანსს და დაბეჭდავს დარჩენილ ნაშთს. გამოიყენე nonlocal.


def bank_account(initial_balance):
    balance = initial_balance #sawyisi balansi
    def withdraw(amount):
        nonlocal balance
        balance -= amount
        return balance
    return withdraw
test = bank_account(1000)
print(test(500))#bank_account(1000)(500)
print(test(200))#bank_account(500)(200)
print(test(50))#bank_account(200)(50)

#დავალება 3: "Power Generator" (Currying)დაწერე ფუნქცია power_of(base), რომელიც აბრუნებს ფუნქციას. ეს მეორე ფუნქცია უნდა იღებდეს exponent-ს 
# (ხარისხს) და აბრუნებდეს $base^{exponent}$.მაგალითი: base_two = power_of(2) -> print(base_two(3)) (უნდა იყოს 8).


def power_of(base):
    def sorting(exponent):
        return base**exponent
    return sorting
base_two = power_of(2)
print(base_two(9))

#დავალება 4: "Global vs Local" (Debugging)სტუდენტს მიეცი ეს კოდი და სთხოვე, global ქივორდის გამოყენებით გაასწოროს ისე, რომ შეცდომის ნაცვლად დაიბეჭდოს 11:Pythonpoints = 10
points = 10
def add_point():
    global points
    points += 1 # აქ ერორია
    print(points)
add_point()

#დავალება 5: "Pure Math" (Pure Function)დაწერე Pure ფუნქცია calculate_rectangle_area(a, b), რომელიც ითვლის მართკუთხედის ფართობს. 
# სტუდენტმა უნდა დაამტკიცოს, რატომ არის ეს ფუნქცია "Pure" (არ ცვლის გარე ცვლადებს და ყოველთვის ერთსა და იმავე შედეგს იძლევა)

def calculate_rectangle_area(a, b):
    return a * b
#ფუნქცია არ ცვლის არაფერს თავის გარეთ. ყოველთვის ერთნაირია ერთი და იმავე a, b-სთვის და არ ეხება გარე რაგაცეებს.

#დავალება 6: "Logger Side-Effect" (Impure Function)შექმენი გლობალური მასივი logs = []. დაწერე Impure ფუნქცია add_log(message), 
#რომელიც არაფერს აბრუნებს (None), მაგრამ გადაცემულ შეტყობინებას ამატებს logs მასივში.

logs = []
def add_log(message):
    logs.append(message)
print(add_log("GOA"))
print(logs)


#დავალება 7: "Tax Calculator" (Currying)შექმენი კარიერებული ფუნქცია calculate_tax(tax_rate)(price).
# ჯერ შექმენი ცვლადი georgian_tax = calculate_tax(0.18).შემდეგ გამოიყენე ის სხვადასხვა ფასზე: georgian_tax(100), georgian_tax(250).

def calculate_tax(tax_rate):
    def test_f(price):
        return tax_rate * price
    return test_f
georgian_tax = calculate_tax(0.18)
print(georgian_tax(100))
print(georgian_tax(250))

#დავალება 8: "The Shadowing Challenge" (Scopes)დაწერე კოდი, სადაც ფუნქციის გარეთ არის name = "Global", 
# ფუნქციის შიგნით კი name = "Local". სტუდენტმა უნდა დაბეჭდოს ორივე მნიშვნელობა ისე, რომ ერთმანეთს ხელი არ შეუშალონ 
# (გამოიყენოს სკოუპების პრინციპი).

name = "global"
def a():
    name = "Local"  
    print(name)          #როდესაც ფუნქციის შიგნით იძახებ print(name)-ს პითონი ჯერ ეძებს ცვლადს ლოკალურ არეალში
print(name)
a()

#დავალება 9: "Prefixer" (Closure)დაწერე ფუნქცია make_prefix(prefix), რომელიც აბრუნებს ფუნქციას. დაბრუნებულმა ფუნქციამ ნებისმიერ გადაცემულ სახელს 
#წინ უნდა დაუწეროს ეს პრეფიქსი.მაგალითი: dr_prefix = make_prefix("Dr. ") -> print(dr_prefix("Davit")) (უნდა დაბეჭდოს: Dr. Davit).

def make_prefix(prefix):
    def applier(name):
        return f"{prefix}. {name[0].upper()}{name[1::]}"
    return applier
#Dr.
dr_prefix = make_prefix("Dr")
print(dr_prefix("davit"))
#Ms.
ms_prefic = make_prefix("Ms")
print(ms_prefic("barbare"))


#დავალება 10: "Filter & Lambda" (Built-in Scopes)მოცემულია მასივი: numbers = [1, 5, 8, 10, 15, 20].სტუდენტმა filter() ფუნქციისა და 
#lambda-ს (რომელიც თავისთავად Closure-ია) გამოყენებით უნდა დატოვოს მხოლოდ ის რიცხვები, რომლებიც 5-ზე უნაშთოდ იყოფა.
numbers = [1, 5, 8, 10, 15, 20]
print(list((filter(lambda n:n if n % 5 == 0 else None,numbers))))