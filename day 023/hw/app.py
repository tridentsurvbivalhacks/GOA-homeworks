#1) გადავხედოთ ლისტებს და საერთოდ განვლილ მასალას

#2) ვინც არ დაასრულეთ საკლასო დავალება, აუცილებლად დაასრულეთ ბოლომდე და თავიდან უყურეთ ჩანაწერს

a = "lom ki ara lekvi kide!"
print(len(a))
new_a = ""

for i in range(len(a)):
    if a[i] != " ":
     new_a += a[i]
print(new_a)
print(a)
# 3) კომენტარების სახით ახსენით როგორ მუშაობს for ციკლი list ებთან
# pirveli vqmnit 5 elementian lists igive arrays 
#           0         1      2       3       4
array = ["sandro", "davit", "gio", "ilia", "mate"]
print(len(array)) #amit gavigebt ramdeni elementia namdvilad am listshi
for i in range(len(array)): #amas ro davwert range shi range sheinaxavs array listis elementebis raodenobas anu iqneba range(5)
 print(i) #amit dava cyclebt range shi chaweril raodenobas anu 5 cifrs
 print(array[i]) #amit dava cyclebt listis shignit yvela elements

#4) for ციკლის მეშვეობით გამოიტანეთ ყველა ლუწი რიცხვი 22-დან 104-მდე , და ყველა კენტი რიცხვი 204-დან 426 ამდე.
print("#-----------------------------------------------Even-----------------------------------")
for i in range(24,104):
 if i % 2 == 0:
   print(i)
print("#-----------------------------------------------Odd------------------------------------")
for i in range(204,426):
  if i % 2 != 0:
    print(i)

#5) მომხმარებელს შემოატანინეთ თავისი ასაკი, შეინახეთ იგი ცვლადში და შეამოწმეთ მეტია თუ არა იგი 18 თუ ნაკლებია უთხარით:  "ჯერ არ ხართ 18 წლის " თუ 18 ის არის ან მეტის უთხარით: "თქვენ გადაცდით ასაკის ზღვარს"
age = int(input("Sheiyvanet tqveni asaki: "))
print(age)
if int(age) < 18:
  print("ჯერ არ ხართ 18 წლის ")
elif age >= 18:
  print("თქვენ გადაცდით ასაკის ზღვარს")