# class Human():
#     is_human = True

#     def __init__(self, name, surname, age):  #constructor
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}")

#     @classmethod
#     def is_human(cls, fullname, age):
#         name, surname = fullname.split()
#         cls.name = name
#         cls.surname = surname
#         cls.age = age
#         return f"Name: {cls.name}\nSurname: {cls.surname}\nAge: {cls.age}"

#     @staticmethod
#     def check_age(age):
#         if age > 18:
#             return True
#         else:
#             return False


# p1 = Human("John", "Doe", 30)
# # p1.display()

# new_obj = Human.is_human("John Doe2", 25)
# # print(new_obj)


# print(Human.check_age(20))


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        ...


class Cat(Animal):
    def move(self):
        print("Cat is moving")


p2 = Cat()
p2.move()
