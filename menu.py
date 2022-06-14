from import_export import import_file
import add_delete_read_func


def menu():
    def menu_interface():
        list_menu = ['1. Показать телефонную книгу', '2. Найти контакт по ФИО', '3. Найти контакт по № телефона',
                     '4. Добавить контакт', '5. Редактировать контакт',
                     '6. Удалить контакт', '7. Импортировать контакт', '8. Экспортировать контакт', '9. Выход']
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
                    print('+++++++++++++++++++++++++++')
                    print('Показать телефонную книгу')
                    print('+++++++++++++++++++++++++++')

                case '2':
                    print('+++++++++++++++++++++++++++')
                    print('Найти контакт по ФИО')
                    print('+++++++++++++++++++++++++++')

                case '3':
                    print('+++++++++++++++++++++++++++')
                    print('Найти контакт по № телефона')
                    print('+++++++++++++++++++++++++++')

                case '4':
                    print('+++++++++++++++++++++++++++')
                    print('Добавить контакт')
                    print('+++++++++++++++++++++++++++')

                case '5':
                    print('+++++++++++++++++++++++++++')
                    print('Редактировать контакт')
                    print('+++++++++++++++++++++++++++')

                case '6':
                    print('+++++++++++++++++++++++++++')
                    print('Удалить контакт')
                    print('+++++++++++++++++++++++++++')

                case '7':
                    print('+++++++++++++++++++++++++++')
                    print('Импортировать контакт')
                    print('+++++++++++++++++++++++++++')

                case '8':
                    print('+++++++++++++++++++++++++++')
                    print('Экспортировать контакт')
                    print('+++++++++++++++++++++++++++')

                case '9': break
        else:
            print("Введите пожалуйста число (арабское), и нажмите клавишу 'Enter'!")
    return id_menu
