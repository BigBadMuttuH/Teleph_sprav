from add_delete_read_func import read_phone_book
# Импортировал только чтение, так как у нас нет
from import_export import impexp_file


def menu():
    def menu_interface():
        list_menu = ['1. Посмотреть весь список целиком', '2. Найти контакт по ФИО', '3. Найти контакт по номеру',
                     '4. Импотрт из файла', '5. Экспорт в файл', '6. Выход']
        len_id_menu = len(list_menu[0])
        for i in list_menu:
            if len_id_menu < len(i):
                len_id_menu = len(i)
        len_id_menu += 9
        print('\t Меню телефонного справочника \t')
        print('=' * len_id_menu)
        for i in list_menu:
            print(f'+  {i}')
        print('=' * len_id_menu)
        print('')
        return list_menu

    res = 0
    id_menu = 0
    while res != 9:
        l_menu = menu_interface()
        count_of_points_menu = len(l_menu)  # Пусть количество пунктов будет в отдельной переменной.
        id_menu = input(f'Выберите пункт меню (1-{count_of_points_menu}): ')
        if id_menu.isdigit():  # Проверка на цифры
            if int(id_menu) > 0 and int(id_menu) < count_of_points_menu + 1: res = -1  # Проверка на диапазон пунктов
            match id_menu:
                case '1':
                    print('+++++++++++++++++++++++++')
                    print('Просмотр списка контактов')
                    print('+++++++++++++++++++++++++')
                    read_phone_book()
                case '2':
                    print('++++++++++++++++++++')
                    print('Найти контакт по ФИО')
                    print('++++++++++++++++++++')
                # В общем репозитории не найдена нужная функция.
                case '3':
                    print('+++++++++++++++++++++++')
                    print('Найти контакт по номеру')
                    print('+++++++++++++++++++++++')
                case '4':
                    print('++++++++++++++++')
                    print('Импотрт из файла')
                    print('++++++++++++++++')
                    impexp_file()

                case '5':
                    print('++++++++++++++')
                    print('Экспорт в файл')
                    print('++++++++++++++')
                    impexp_file()

                case '6':
                    break
    # Раз у нас в этом файле вызываются функции, то думаю, что и id_menu не надо возвращать.
    # return id_menu
