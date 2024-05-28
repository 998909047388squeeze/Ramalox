def add_client(clients):
    print("Занятые комнаты:", list(clients.values()))
    name = input("Введите имя клиента: ")
    if name in clients:
        print("Клиент с таким именем уже существует!")
        return
    room_number = input("Введите номер комнаты для клиента: ")
    print(f"Клиент {name} добавлен в комнату {room_number}.")


def remove_client(clients):
    name = input("Введите имя клиента для удаления: ")
    if name in clients:
        del clients[name]
        print(f"Клиент {name} был удален.")
    else:
        print("Клиент с таким именем не найден!")

def view_occupied_rooms(clients):
    if clients:
        print("Занятые номера:")
        list(clients.values())
    else:
        print("Нет занятых номеров.")


# Основной цикл программы
clients = {}
while True:
    print("\nМеню:")
    print("1. Добавить клиента")
    print("2. Удалить клиента")
    print("3. Увидеть занятые номера")
    print("4. Выйти")

    choice = input("Выберите действие (1-4): ")

    if choice == '1':
        add_client(clients)
    elif choice == '2':
        remove_client(clients)
    elif choice == '3':
        view_occupied_rooms(clients)
    elif choice == '4':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор, попробуйте снова.")

