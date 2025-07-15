#Инкапсуляция
class Student: 
    def __init__(self, name, grade, password):
        self.name = name            
        self._grade = grade         
        self.__password = password  

    def change_password(self, new_pass):
        self.__password = new_pass

    def get_info(self):
       print(f"Имя: {self.name}, Оценка: {self._grade}")

student = Student("Эржан", 56, "123456789")
student.get_info() 
student.change_password("112233445566")



from abc import ABC, abstractmethod

# Абстрактный класс
class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def move(self):
        print("Машина едет по дороге.")

    def stop(self):
        print("Машина остановилась.")
        
class Bike(Vehicle):

    def move(self):
        print("Велосипед движется по тропинке.")

    def stop(self):
        print("Велосипед остановился.")


car = Car()
bike = Bike()

print("мерседес:")
car.move()
car.stop()

print("\nШосссейный велосипед:")
bike.move()
bike.stop()
