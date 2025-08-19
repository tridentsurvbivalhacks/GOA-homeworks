"""
დავალება 1: ასაკის შემოწმება
მიზანი: შეამოწმეთ მომხმარებლის ასაკი და დაადგინეთ, შეუძლია თუ არა მას მანქანის მართვა.
"""


age_input = int(input("age?: "))

if age_input >= 18:
    print(" shegilia manqanis tareba!")
else: 
    print(" ar shegilia manqanis tareba!")


"""
 დავალება 2: თერმომეტრის თბილ/ცივ მდგომარეობაში გადატანა
მიზანი: შეამოწმეთ ჰაერის ტემპერატურა და დაადგინეთ, არის თუ არა ცივი თუ თბილი ამინდი.
"""


temp = 38

if temp > 9:
    print(" es aris tbili temperatura")
else: 
    print(" es aris civi temperatura")


"""
✅ დავალება 3: საკუჭნაოში ნივთის რაოდენობა
მიზანი: შეამოწმეთ თუ საკუჭნაოში არსებობს საკმარისი რაოდენობა კონკრეტული ნივთის (მაგ. პურის) და მიიღეთ გადაწყვეტილება, უნდა შეიძინოთ თუ არა.
"""

to_buy_puri = 3


if to_buy_puri >= 4:
    print("unda sheizino")
else:
    print(" ar unda sheizino")

"""
დავალება 4: გაყიდვა და ფასდაკლება
მიზანი: შეამოწმეთ, თუ მომხმარებელს აქვს საკმარისი თანხა ნივთის შესაძენად და განახორციელეთ ფასდაკლება.
"""

balance = 30
benzini = 50
#fasdakleba
benzini = benzini // 2
if balance >= benzini:
    print(" enough balance")

elif balance >= benzini:
    print(" enough ballance")

else: 
    print(" not enough balance")

"""
 დავალება 5: დაწერე გამოთვლა
მიზანი: შეამოწმეთ, არის თუ არა რიცხვი კენტი თუ კი ერთმნიშვნელოვანი.
"""

num = 2
if num % 2 == 0:
    print(" Even")
else:
    print(" Odd")