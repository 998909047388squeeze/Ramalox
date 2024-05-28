# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
#
# class Cow(Animal):
#     def make_sound(self):
#         return "Moo!"
#
#
# dog = Dog()
# cat = Cat()
# cow = Cow()
#
#
# print("Dog:", dog.make_sound())
# print("Cat:", cat.make_sound())
# print("Cow:", cow.make_sound())


# class Vehicle:
#
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#     def display_info(self):
#         print(f"Марка: {self.brand}")
#         print(f"Год выпуска: {self.year}")
#
#
# class Car(Vehicle):
#
#     def __init__(self, brand, year, num_doors):
#         super().__init__(brand, year)
#         self.num_doors = num_doors
#
#     def display_info(self):
#         super().display_info()
#         print(f"Количество дверей: {self.num_doors}")
#
#
# class Motorcycle(Vehicle):
#
#     def __init__(self, brand, year, engine_size):
#         super().__init__(brand, year)
#         self.engine_size = engine_size
#
#     def display_info(self):
#         super().display_info()
#         print(f"Объем двигателя: {self.engine_size} куб. см")
#
#
# car = Car("Toyota", 2024, 5)
# motorcycle = Motorcycle("Harley-Davidson", 2022, 1800)
#
# print("Информация об автомобиле:")
# car.display_info()
# print("\nИнформация о мотоцикле:")
# motorcycle.display_info()