# #инкапсуляци

# class BankAccount:
#     __def_pass = "admin"
#     def __init__(self, user, balance, password):
#         self.user = user
#         self._balance = balance #защищенный атрибут
#         self.__password = password #приватный атрибут

#     def get_user(user):
#         return print(f"self.user")
    
#     def __generate_defoult_pass(self):
#         self.__password = self.__def_pass
    
#     def reset_pass(self):
#         self.__generate_defoult_pass()
#         return print("pass reset!!!")
    
# john  = BankAccount("John", 1000, 1234)

# print (john._BankAccount__password)
# john.reset_pass()
# print (john._BankAccount__password)

# print (dir(john))
from abc import ABC, abstractmethod

#абстракный кдасс
class Animal(ABC):
    @abstractmethod
    def step(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, nik):
       self.nik = nik
    
    def step(self):
        pass

    def make_sound(self):
        pass

    
sharik = Dog("Sharik")

