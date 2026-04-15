# 1) დაწერეთ ფუნქცია apply_operation(numbers, operation) numbers — რიცხვების სია, operation — ფუნქცია, ფუნქციამ უნდა
# დააბრუნოს ახალი სია, სადაც თითოეულ ელემენტზე გამოყენებულია operation.
operation_square = lambda list:[i**2 for i in list]


def apply_operation(numbers,operation):
    return operation(numbers)
print(apply_operation([1,2,3,4],operation_square))
