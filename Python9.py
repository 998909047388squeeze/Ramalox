# class Car:
#     type = 'BMW'
#     color = 'white'
#     max_speed = 380

# class Car:
#     def __init__ (self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# gentra = Car('Ravon', 'Black',2024)
# print(gentra.year)


# class User:
#     def __init__ (self,username,text,likes):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
#     def add_comment(self):
#         print('Сколько раз Рама лох')
#
#
# username = User ('Ani', 'Davron',5734658)
# username.add_comment()
# print(username.likes)
#
# class Car:
#     def __init__(self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def stop(self):
#         print('Машина остановись')
#
#     def change_color(self,new_color):
#         self.color = new_color
#
# gentra = Car('Ravon','Black',2024)
#
# gentra.change_color('Yellow')
# print(gentra.color)

# class BankAccount:
#     def __init__(self,name,balance=0):
#         self.name = name
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance = self.balance + amount
#         print('Деньги успешно добавлены')
#     def cash(self,amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print('Деньги сняты')
#         else:
#             print('Недостаточно средств')
#     def my_balance(self):
#         print(f'Денег на балансе: {self.balance}')
#
# user1 = BankAccount("Rama")
# while True:
#     menu = input("Что хотите сделать?: \n"
#                  "1- Посмотреть баланс\n"
#                  "2- Пополнить счет\n"
#                  "3- Снять деньги\n"
#                  "Действие: " )
#     if menu == "1":
#         user1.my_balance()
#     elif menu == "2":
#         amount = float(input("Введите сумму:"))
#         user1.deposit(amount)
#     elif menu =="3":
#         amount =  float(input('Введите сумму для снятия '))
#         user1.cash(amount)
#     else:
#         print('Непонял')

# class User:
#     def __init__(self, name, email, age, phone_number):
#         self.name = name
#         self.email = email
#         self.age = age
#         self.phone_number = phone_number
#     def change_name(self, new_name):
#         self.name = new_name
#     def change_number(self, new_number):
#         self.phone_number = new_number
#     def change_email(self, new_email):
#         self.email = new_email
#
# user1 = User(name='Artur', email='bvsduv@gmail.com', age=29, phone_number='+998909393939',)
# print(vars(user1))