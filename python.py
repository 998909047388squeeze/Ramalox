# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         return f"{self.name} is barking."
#
# # Создание экземпляров класса
# dog1 = Dog("Rex", 2)
# dog2 = Dog("Buddy", 3)
#
# print(dog1.name)
# print(dog2.age)
# print(dog1.bark())
#
# class Animal:
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def speak(self):
# #         pass
#
#

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"
#
#
# dog = Dog("Rex")
# cat = Cat("Whiskers")
#
# print(dog.speak())
# print(cat.speak())



#2 задание
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"
#
#
# person1 = Person("Albert", 18)
# person2 = Person("Rama", 15)
# person3 = Person("Artur", 17)
#
#
# people = [person1, person2, person3]
#
#
# for person in people:
#     print(person)





# 4 доп Задача
# class Car:
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#     def start_car(self):
#         print('Автомобиль заведен')
#     def stop_car(self):
#         print('Автомобиль заглушен')
#     def year_car(self):
#         print(f'Год выпуска: {self.year}')
#     def type_car(self):
#         print(f'Тип машины: {self.type}')
#     def color_car(self):
#         print(f'Цвет машины: {self.color}')
#
# user1 = Car('Cерый', 'SUV', 2020)
# user1.start_car()
# user1.stop_car()
# user1.year_car()
# user1.type_car()
# user1.color_car()
#
# #3доп задача
# class Math:
#     def __init__(self, first_number, second_number):
#         self.a = first_number
#         self.b = second_number
#     def addition(self):
#         final_answer = self.a + self.b
#         print(f'{self.a} + {self.b} = {final_answer}')
#     def multiplication(self):
#         final_answer = self.a * self.b
#         print(f'{self.a} * {self.b} = {final_answer}')
#     def division(self):
#         if self.a != 0 and self.b != 0:
#             final_answer = self.a / self.b
#             print(f'{self.a} / {self.b} = {final_answer}')
#         else:
#             print('На 0 делить нельзя')
#     def substraction(self):
#         final_answer = self.a - self.b
#         print(f'{self.a} - {self.b} = {final_answer}')
#
# user1 = Math(2, 1)
#
# user1.addition()
# user1.multiplication()
# user1.division()
# user1.substraction()