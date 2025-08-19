#1) კომენტარებით ახსენით მათემატიკური ოპერატორები

# მათემატიკური ოპერატორები არიან 
# - (გამოკლება)
# + (მიმატება)
# *, ** (გამრავლება) --> * (ხარისხი) ---> **
# //, / (გაყოფა) ----> / გამოაქვს შედეგი float // ---> გამოაქვს შედეგი Int
# % (ნაშთი)
# მათემატიკური ობიექტებით შეგვილია გამოვითვალოთ სხვადა სხვა მაგალითები პრინტის სახით

#2) შექმენით ორი ცვლადი სადაც input ით კითხავთ მომხმარებელს რომ შეიყვანოს სხვადასხვა ციფრი და შეაჯამეთ ის

x = 94
y = 42


inputExample = input(" შეიყვანეთ" + " სხვადასხვა" + " ციფრი" " და" " შეაჯამეთ" " ის") 

print(x + y)

# 3) შექმენით ცვლადები და მათემატიკური ოპერატორების მეშვეობით გააკეთეთ მაგალითები

# 1 (გამოკლება)
 
subtract = 85 - 25
print(subtract)

addition = 54 + 35
print(addition)

multiply = 7 * 8
print(multiply)

quality = 2 ** 6
print(quality)

divide_1 = 83 / 5
print(divide_1)

divide_2 = 45 // 9
print(divide_2)

#46 % 5-ზე არ იყოფა ამიტომაც დაგვრჩება ნაშთი და დარჩენილი ნაშთს პროგრამა გამოიტანს ტერმინალში რადგან ყველაზე უახლოესი იყოფა 45
balance = 46 % 5
print(balance)


# 4 ამოცანა: ერთ ყუთში არის 4 ბურთი. თუ გვაქვს 3 ყუთი, რამდენი ბურთი გვაქვს სულ?


#ოცემულია
box1 = 4
box2 = 4
box3 = 4

# ამოხსნა პროგრამულად

# 1box = 4 balls
# 2box = 1box + 1box
print(box1 + box2)
box1_box2 = 8
# 3box = 2box + 1 box

print(box1_box2 + box3)

#5) გამოიყენეთ შედარების ოპერატორები (< . > , >=, <=, ==, =!) სხვადასხვა მაგალითში, მაგ. შეადარეთ თქვენი და თქვენი ოჯახის წევრების ასაკი

father = 45
mother = 42
brother = 11
me = 13 

#father
print(father > mother)
print(father < brother)
print(father > me)

#mother
print(mother < father)
print(mother > brother)
print(mother > me)

#brother
print(brother > father)
print(brother > mother)
print(brother < me)

#me
print(me < father)
print(me < mother)
print(me > brother)