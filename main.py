#отступы - хорошо
age = int(input('Ваш возраст? '))
if age < 18:
    print('Доступ закрыт')
elif age == 23:
    print('Доступ абсолютно запрещен')
else:
    print('Доступ разрешен')