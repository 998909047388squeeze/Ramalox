# циклы
# name ="Pasha"
# for item in name:
#     print(item)

# my_list =(6,'a',2)
# for p in my_list:
#   print(p)
#
# print(f'Всего{len(my_list)})элементов')

# my_tuple = (6,'a',2)
# count = 0
# for i in range(1,16,2):
#     count = count +1
#     print(count)
# names =['Ivan','Pavel','jordan',5]
# for i in range (1,20):
#     if"Pavel" in names:
#         print('Pavel'' Есть в списке')
#     else:
#         print('Не понимаю о ком вы')

# spam =("Hello")
# while spam == "Hello":
#     print(spam)

# p = ['m','my',23]
# # i = 0
# # while i < len(p):
# #     print(p[i])
# #     i = i +  1

# names = ['Ivan','Pavel','Jordan']
# while True:
#     print('{}'.format(names[0::1]))
# Важно
# names = ["Inan","Oleg"]
# while True:
#     new = input('Кого добавили?:')
#     if new == "выход":
#         break
#     else:
#         names.append(new)
#         print(names)

# menu = input("Что хотите сделать? 1- добавить  имя  2- добавить номер  3- добавить услугу ")
# names = []
# contacts = []
# service = []
# while True:
#     new_name = input('Введите имя: ')
#     if new_name in names:
#         print("Имя успешно введено")
#     else:
#         names.append(new_name)
#
#     new_contact = input('Введите номер: ')
#     if new_contact in contacts:
#         print('Номер успешно введен')
#     else:
#         contacts.append(new_contact)
#     new_service = input('Введите сервис: ')
#
#     if new_service in service:
#         print('Сервис был введен')
#     else:
#         contacts.append(new_service)
#         print(names, contacts, service)

# def calculate_total_weight(suvenir_count, trinket_count):
#     suvenir_weight = suvenir_count * 75
#     trinket_weight = trinket_count * 112
#     total_weight = suvenir_weight + trinket_weight
#     return total_weight
#
# suvenir_count = int(input("Введите количество сувениров: "))
# trinket_count = int(input("Введите количество безделушек: "))
#
# total_weight = calculate_total_weight(suvenir_count, trinket_count)
# print("Общий вес посылки:",total_weight,"г")



# number = int(input("Введите любое число: "))
#
# print(f"Таблица умножения для числа {number}:")
# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")

# word = input("Введите слово: ").lower()
#
# if word == word[::-1]:
#     print("Это слово - палиндром.")
# else:
#     print("К сожалению это слово не является палиндромом.")

# mini_bottles = 0.10
# big_bottles = 0.25
#
# amount_minibottles = int(input('Введите количество бутылок объемом 1 литр или меньше: '))
# amount_bigbottles = int(input('Введите количество бутылок объемом больше 1 литра: '))
#
# total_amount = (mini_bottles * amount_minibottles) + (big_bottles * amount_bigbottles)
# print("Сумма, которую можно выручить: ${:.2f}".format(total_amount))

# numer = int(input('Введите натуральное положительное число: '))
# if numer <= 0:
#        print('Что то пошло не так')
# else:
#        total_sum = (numer) * (numer+ 1) // 2
#        print(f'Сумма натуральных чисел от 1 до {numer} = {total_sum} ')
