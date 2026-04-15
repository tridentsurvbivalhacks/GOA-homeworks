#1) დაწერეთ ფუნქცია apply_operation(numbers, operation) numbers — რიცხვების სია, operation — ფუნქცია,
def apply_operation(numbers,operation):
    return operation(numbers)

# def cube(list):
#     return [i**3 for i in list]

cube = lambda list:[i**3 for i in list]
x = apply_operation([1,2,3,4],cube)
print(x)


#2) დაწერეთ ფუნქცია my_map(func, lst) რომელიც იმუშავებს როგორც map.
def my_map(func,list):
    return func(list)

# def mapping(array):
#         return filter(lambda n: n if n % 2 == 0 else None, array)

mapping = lambda array:list(map(lambda n: n if n % 2 == 0 else None, array))
x = my_map(mapping,[2,4,5,6,7,8])
print(x)


#3) დაწერეთ ფუნქცია my_filter(func, lst) რომელიც აბრუნებს მხოლოდ იმ ელემენტებს, რომლებზეც func აბრუნებს True.
cube_eeo = lambda arr: [i for i in arr if i**3 % 2 == 0]

def my_filter(func, lst):
    return func(lst)

o = my_filter(cube_eeo, [6, 7, 8, 9, 1, 2, 3, 4, 5])
print(o)
#4) დაწერეთ ფუნქცია make_multiplier(n) ფუნქციამ უნდა დააბრუნოს ახალი ფუნქცია, რომელიც რიცხვს ამრავლებს n-ზე.
def make_multiplier(n):
    # def insertion(number):
    #     return number * n
    insertion = lambda number:number*n
    return insertion
print(make_multiplier(5)(10))

#5) დაწერეთ ფუნქცია repeat(func, n) რომელიც აბრუნებს ახალ ფუნქციას. ეს ახალი ფუნქცია როცა გამოიძახება,
# func შესრულდება n-ჯერ.
def simple_math(a,b):
    return a + b
def repeat(func,n):
    res = [i for i in range(n)]
    for i in res:
        res[i] = func
    return res
print(repeat(simple_math(2,3),3))
