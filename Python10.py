# def x (values):
#     values[0] = 1
# v = [1,2,3,4]
# x(v)
# print(v)

# class Noname:
#     def __init__(self,name):
#         self.name = name
#
#     def punkt(self,word):
#         return f'Слово: {word}, {self.name}'
#
# c = Noname('Oleg')
# b = Noname('Ivan')
# print(c.punkt('privet'))



# class Car:
#     def __init__(self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# class Super(Car):
#     def __init(self,sponsor,model,color,year):
#         super(). __init__(self,model,color,year)
#         self,sponsor = sponsor


#@classmethod

# class MyClass:
#     @classmethod
#     def class_info(spam):
#         print('Hello')
#
# MyClass.class_info()
# class Rectangle:
#     def __init__(self,width,height):
#         self.width =width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
# rectangle = Rectangle( 5,6 )
# print(rectangle.area)

# class Worker:
#     def __init__(self, name, position):
#         self.__name = name
#         self.__position = position
#
#     def get_name(self):
#         return self.__name
#
#     def get_position(self):
#         return self.__position
#
#     def __str__(self):
#         return f"Worker(Name: {self.__name}, Position: {self.__position})"
#
#
# class TrackedWorker(Worker):
#     def __init__(self, name, position):
#         super().__init__(name, position)
#
#     def __str__(self):
#         return f"TrackedWorker(Name: {self.get_name()}, Position: {self.get_position()})"
#
#
# worker1 = TrackedWorker("John", "Programmer")
# worker2 = TrackedWorker("Baris", "Manager")
#
#
# print(worker1)
# print(worker2)