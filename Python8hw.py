# a = lambda x,y: x + y
# num1 = int(input('Введите первое число:'))
# num2 = int(input('Введите второе  число:'))
# result = a(num1,num2)
# print(f'Сумма чисел {num1} и {num2}  равна {result}')

# school managment


class_list = {'рамазан': 17, 'артур': 17}
class_marks = {'рамазан': {'Предметы': {'алгебра': 5}},
               'артур': {'Предметы': {'биология': 5}}}

def add_students():
    add_student = input("Добавить ученика в список: ")
    if add_student.lower() in {i.lower() for i in class_list}:
        print('Такой ученик существует')
    else:
        add_age = int(input('Введи возраст: '))
        class_list[add_student] = add_age
        print(f'{add_student} - {add_age} лет успешно добавлен/a')

def remove_students():
    remove_student = input('Удалить ученика из списка: ')
    if remove_student.lower() not in {i.lower() for i in class_list}:
        print("Такого ученика не существует")
    else:
        class_list.pop(remove_student.lower())
        print(f'{remove_student} успешно удален/а')

def show_students():
    print('Список учеников:', class_list)

def show_marks():
    print('Список итоговых оценок:', class_marks)

def subjects():
    existing_name = input('Имя ученика: ')
    if existing_name.lower() not in {i.lower() for i in class_list}:
        print('Такого ученика не существует')
        return

    subject_name = input('Введите предмет для выставления итоговой оценки:\n'
                         'Алгебра\n'
                         'Биология\n'
                         'Английский: ').lower()

    if subject_name not in ['алгебра', 'биология', 'английский']:
        print('не тот предмет')
        return

    subject_mark = int(input('Оценка: '))
    if subject_mark < 1 or subject_mark > 5:
        print(f'Введите оценку от 1 до 5, а не {subject_mark}')
        return

    for student in class_marks:
        if student.lower() == existing_name.lower():
            class_marks[student]['Предметы'][subject_name] = subject_mark
while True:
    menu = int(input('\nВведите номер действия\n'
                     '1-Добавить\n'
                     '2-Удалить\n'
                     '3-Поставить итоговую оценку\n'
                     '4-Показать список учеников\n'
                     '5-Показать список итоговых оценок\n'
                     '6-Выйти: '))

    if menu == 1:
        add_students()
    elif menu == 2:
        remove_students()
    elif menu == 3:
        subjects()
    elif menu == 4:
        show_students()
    elif menu == 5:
        show_marks()
    elif menu == 6:
        print('Вы успешно вышли!')
        break
    else:
        print('Вы ввели неправильный номер действия')