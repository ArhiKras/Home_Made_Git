class Warrior():
    def __init__(self, name, power, endurance, hair_color): # в данном функция является методом, т.к. находится внутри класса
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
        
    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2
        
    def eat(self):
        print(f"{self.name} сел кушать")
        self.powre += 1
        
    def hit(self):
        print(f"{self.name} нанес удар")
        self.endurance -= 3
        
    def walk(self):
        print(f"{self.name} ходьба")
        self.endurance -= 1
        
    def info(self):
        print(f"имя воина: {self.name}")
        print(f"цвет волос: {self.hair_color}")
        print(f"сила воина: {self.power}")
        print(f"выносливость воина: {self.endurance}")