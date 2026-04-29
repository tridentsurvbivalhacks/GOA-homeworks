# 1) ახსენით რა არის OOP

# 2) ახსენით რა არის Polimorphos, Encapuslation, instance

# 3) ახსენით რას შვება private method და public method 

# 4) ახსენით self. რას შვება და საერთოდ რატომ ვწერთ მას 


#-----------------------------------------------------------------------------------------------

#1.OOP aris object oriented programireba romelic aris obieqtze orientirebuli classebis gamoyenebit instance Encapsulation da ase shemdeg


#2 polimorphos - methodebi,funcqciebi romelic gamoiyeneba pythonshi
#Encapsulation - private method romlitac shegizlia private objectebi,funcqciebi da cvladebi sheqmna 
#instance - aris Classebshi initializeba romelic xdeba def __init__ am dros shen inicializebs uketeb parametrebs da obieqtebs
#mokled ro tqvat instance aris object sheqmnili classis gan romelsac qmni def __init__-it

#3 public methodebi arian sul danaxuli classis garet mara private methodebi ar arian
#anu es imas nishnavs rom private methodebs im classis garet romelshic sheqmeni ver gamoiyeneb
#public method iwereba magalitad self_age = age
#private method ki iwereba self_age = __age amas ro wer shen amas(__) xdi private


#4 self aris mimtitebeli konkretul obieqtze romlis gareshedac sheuzlebelia classebis instancis gamoyeneba


# 5) შექმენით ნებისმიერი კლასი გამოიყენეთ Polimorphos, Encapuslation, private method , public method, any instances

class Characteristics():
    def __init__(self,health,damage,speed,toughness):
        self.health = health #public method
        self.damage = damage #public method
        self.speed = speed #public method
        self.__toughness = toughness #Encapuslation
    



    def __take_damage_double(self, amount): #private method
        self.health = self.health - amount * 2


    def take_damage(self,amount):#Polimorphos
        self.health -= amount

  
boss = Characteristics(100,500,60,0.9)
print(f"boss-health {boss.health}")