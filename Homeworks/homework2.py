class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print("Transport is moving")



class Car(Transport):
    def __init__(self, name, speed, fuel):
        super().__init__(name, speed)
        self.fuel = fuel

    def move(self):
        super().move()
        print("Car is driving")



class Plane(Transport):
    def __init__(self, name, speed, wings):
        super().__init__(name, speed)
        self.wings = wings

    def move(self):
        super().move()
        print("Plane is flying")



class Boat(Transport):
    def __init__(self, name, speed, sail):
        super().__init__(name, speed)
        self.sail = sail

    def move(self):
        super().move()
        print("Boat is sailing")



if __name__ == "__main__":
    car = Car("Toyota", 120, "Gasoline")
    plane = Plane("Boeing", 900, 2)
    boat = Boat("Sailboat", 40, "Large sail")

    car.move()
    plane.move()
    boat.move()
