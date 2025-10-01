# 1) შევქმნათ ლისტი სადაც შევინახავთ ტქვენი მშობლების სახელებს, და ბოლოში ჩაამატეთ თქვენი სახელიც
list = ["valeri mikelashvili", "nino managaze", "nana dolize", "davit mikelashvili"]
list.append("sandro mikelashvili")
print(list)

# 2) შექმენით რიცხვების სია. გადაუარეთ მას for ციკლითი. შეამოწმეთ თუ რიცხვი ლუწია დაბეჭდეთ "Number is even", სხვა შემთხვევაში "Number is Odd"
for i in range (20):
    if i % 2 == 0:
        print(i, "Number is even")
    else:
        print(i, "Number is odd")
# 3) შექმენით სიტყვების სია 10 ელემენტისგან. გადაუარეთ for ციკლით ამ სიას ისე, რომ დაბეჭდოთ ყოველი მე-2 ელემენტი(დაგჭირდებათ slicing-ი)
#             0          1        2       3         4      5      6      7       8        9     
array = [ "markdown", "markup", "c++", "golang", "html", "css", "c#", "rust" , "ruby", "python"]
print(len(array))
print(array[::2])
# 4) შექმენით ცვლადი, სადაც შეინახავთ სიტყვას. გადაუარეთ მას for ციკლით, დაბეჭდეთ მისი თითოეული სიმბოლო და გვერდით მიუწერეთ მისი რიგის ნომერი string-ში(ანუ მერამდენე სიმბოლოა)

# მაგალითად: academy = "GOA"
# "G-1"
# "O-2"
# "A-3"

# გატესტეთ ეს დავალება სხვადასხვა სიტყვებზე და ნახეთ შედეგი
mentor = "davit grzelishvili"
for i in range(len(mentor)):
    print(mentor[i], - (i), "symbol")
# 5) მოიძიეთ, როგორ შეიძლება სიის შემოტრიალება, შემდეგ შექმენით სია და დაბეჭდეთ ის შემოტრიალებულად. მაგალითად: [1,2] -> [2,1]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("----------------------normal printed array list of 10 nembers------------------------")
print(array[::])
print("----------------------reverse printed array list of 10 nembers-----------------------")
print(array[::-1])