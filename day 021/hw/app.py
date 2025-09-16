# 1) დღევანდელი მასალა ახსენით კომენტარებით (ლისტები, სლაისინგი , ა.შ)

list = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
#listebi aris rogorc cvladebi magram listebi shedgeba bevri mnishvnelobisgan da kide is rom atvla iwyeba 0 idan da bolo ricxvi shegvilia gamoviyenot -1 bolos wina kide -2 bolos mesame kide -3 da ase shemdeg
#ogond eseni ukve gamogvadgeba slice bshi
print("from 0 to end")
print(list[0::]) #index 0 idan iwyeba da mtavrdeba dasasrulamde
print("from start to end")
print(list[::])  #iwyeba sawyisidan mtavrdeba dasasrulamde
print("from start to index 3")
print(list[::3]) #iwyeba sawyisidan mtavrdeba 3 indexamde anu 4
print("from end to start (reverse list)")
print(list[::-1])#iwyeba bolodan da mtavrdeba dasawyisshi amas qvia (revers list)
#da es yvelaferi ketdeba slicebit
#(list[start:end:step])
#step aris ramdeni gamotovebit daprintos slice ma magalitad
print("STEP")
print(list[0:9:2])
#tu listi shedgeba 8 elementisgan da "end" shi davuwert 9s im merve elementsac chatvlis da gamova 1, 3, 5, 7, 9 da ara 1, 3, 5, 7

# 2) შექმენით სია და შეიტანეთ ასოები, slicing-ის გამოყენებით გამოიტანეთ: პირველი 5 ასო, ბოლო 3 ასო, უკუღმა და მე-2 დან მე-6 ამდე
#              0    1    2    3    4    5    6    7    8
array_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I",]
print("first 5 letters")
print(array_list[0:5])  #pirveli 5 aso
    #array_list[start:end:step]
print("last 3 letters")
print(array_list[:5:-1]) #bolo 3 aso
#tu listi shedgeba 8 elementisgan da "end" shi davuwert 9s im merve elementsac chatvlis
#da tu -1 gamoviyenet bolo elements agar chatvlis radgan -1 printavs bolo elementamde da ara bolo elementis chatvlit amitom davuwere 9
print("from index 2 to index 6 reversed")
print(array_list[:2:-1]) #2 idan 6 amde revers

# 3) შექმენით სია და შეიტანეთ ციფრები და slicing-ის გამოყენებით გამოიტანეთ: თითოეული მეორე ელემენტი და ბოლო ოთხი ელემენტი უკუღმა.
#              0  1  2  3  4  5  6  7  8 
array_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
print("all elements by 2 steps")
print(array_list1[::2])
#
print("last 4 elements reversed")
print(array_list1[0])

#4) text : "დილამშვიდობისა” და slicing-ის გამოყენებით ცალკე გამოიტანეთ "დილა" და ცალკე "მშვიდობისა"
text = "dilamshvidobisa"
print(text[0:4])
print(text[4::])
#5)sololearn 😎