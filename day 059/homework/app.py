def high_and_low(numbers):
    numbers2 = numbers.split()
    min = numbers2[0]
    max = numbers2[0]
    for i in numbers2:
        if int(i) > int(max):
            max = i
        elif int(i) < int(min):
            min = i
    return f"{max} {min}"     
print(high_and_low("5 1 3 5 6 7"))

