# data ={'name':['jordan','Pavel'],'age':(12,21),'job':'programmers'}
# print(data['name'][0],data['job'][-1])

# instruktor ={'name': 'jordan', 'age': 21, 'job': 'programmer'}
#
# if 21 in instruktor:
#     print('Да есть ')
# else:
#     print('Не понимаю')

# users = {}
#
# users['name'], users ['age'] ='Jordan',21
# print(users)

# users = {}
#
# users['name'], users ['age'] ='Jordan',21
# users.update(job='junior')
# print(users)

# cafees = {'Evos':{'Gorod':'Tashkent','Filialov':'Много','Otkritie':2007}}
#
# cafees['Evos']['кухня'] = 'Fast food'
# print(cafees)

# nums ={1,2,2,3,4,5}
# print(nums)
#
# my = ['2', '33','33',2,'Tgbot']
# my2 = set(my)
#
# print(my2)

# inst = dict(name='Jordan', age=32,job='python programmer')
#
# for k,v in inst.items():
#     print(k,v)

# all_products = {'Весь склад':{}}
# cart = {}
# while True:
#     admin = input('Что хотите сделать? ')
#     if admin.lower() == 'добавить':
#         all_products_name = input('Название продукта ')
#         products_count = int(input('Количество продуктов'))
#         all_products['Весь склад'][all_products_name] = products_count
#     elif admin.lower() == 'продукты':
#         print(all_products)
#     elif admin == 'Добавить в корзину':
#         products_name = input('Название продукта: ')
#         if products_name in all_products['Весь склад']:
#             products_count= int(input('кол-во продукта: '))
#             if products_count <= all_products['Весь склад'][products_name]:
#                 all_products['Весь склад'][products_name] -= products_count
#                 cart[products_name] = products_count
#         elif admin == 'выход':
#             print('Не понимаю вас, попробуйте снова')

s