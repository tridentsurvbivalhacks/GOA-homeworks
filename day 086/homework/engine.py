class Player:
    def __init__(self,health,damage) -> None:
        self.health = 100
        self.damage = damage

    def attack(self,enemy):
        enemy.health -= self.damage

    def walk(self):
        print("Player is walking")
class Enemy(Player):
    def __init__(self, health,damage) -> None:
        super().__init__(health,damage)

    def enemywalk(self):
        print("Enemy is walking stealthily")



#შექმენით utils ფოლდერი. შექმენით utils.py ფაილი იქ, და გადაიტანეთ print ფუნქციები
# controller.py-დან utils.py-ში როგორც ფუნქციები.
