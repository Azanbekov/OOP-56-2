class Hero:
#конструктор класса
    def __init__(self, name, hp,lvl):
         self.name = name
         self.lvl = lvl
         self.hp = hp
#метод класса
    def introduse(self):
         return print(f"привет меня зовут{self.name}")

kirito = Hero("Kirito", "100", "1000")
kirito.introduse()