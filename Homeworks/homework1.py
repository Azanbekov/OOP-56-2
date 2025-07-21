class Car:
    def __init__(self, brand, model, speed, fuel, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.fuel = fuel
        self.year = year
    def introduse(self):
        return print(f"машина {self.brand} {self.model} {self.year} года может разгонятся до {self.speed} ")

Mersedes_benz = Car("Mersedes_benz", "cls63", "350 km/h", "petrol", "2020")
BMW = Car("BMW", "M5", "330km/h", "diesel", "2019" )
Mersedes_benz.introduse()
BMW.introduse()
print(Mersedes_benz.brand)
print(f"{BMW.brand} медленне чем {Mersedes_benz.brand}")
