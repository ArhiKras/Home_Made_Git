class Warrior():
    def __init__(self, name, power, endurance, hair_color): # в данном функция является методом, т.к. находится внутри класса
        self.name = name # атрибут
        self.power = power # атрибут
        self.endurance = endurance # атрибут
        self.hair_color = hair_color # атрибут
        
    def sleep(self): #метод
        print(f"{self.name} лег спать")
        self.endurance += 2
        
    def eat(self): #метод
        print(f"{self.name} сел кушать")
        self.power += 1
        
    def hit(self): #метод
        print(f"{self.name} нанес удар")
        self.endurance -= 3
        
    def walk(self): #метод
        print(f"{self.name} ходьба")
        self.endurance -= 1
        
    def info(self): #метод
        print(f"имя воина: {self.name}")
        print(f"цвет волос: {self.hair_color}")
        print(f"сила воина: {self.power}")
        print(f"выносливость воина: {self.endurance}")
        
war1 = Warrior("Иван", 76, 54, "Блондин") # создание объекта класса Warrior
war2 = Warrior("Олег", 45, 67, "Русый") # создание объекта класса Warrior

print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_color)

print(f"выносливость воина: {war2.endurance}")
war2.sleep()
print(f"выносливость воина повысилась: {war2.endurance}")

print(f"сила воина: {war2.endurance}")
war1.eat()
print(f"сила воина повысилась: {war2.endurance}")

war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.info()