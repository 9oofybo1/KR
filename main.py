from operator import itemgetter
import logging

logging.basicConfig(filename='info.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def out():
    print(f'''
--<=====>--<ТЕЛЕПЕРЕДАЧИ>--<=====>--
Доступные опции:
    1. Вывести список телепередач
    2. Добавить новую телепередачу в список
    3. Поиск по названию телепередачи
    4. Выйти''')
    logging.info('Пользователь получил на вывод основные опции')

def inp():
    ch = input('Введите номер выбранной опции (от 1 до 4) - ')
    try:
        choose = int(ch)
    except ValueError:
        print(f'''
Номер введен некорректно, введите число от 1 до 4!
        ''')
        logging.error(f'Пользователь ввел "{ch}" - данные не числового формата.')

        inp()
        return

    if choose not in[1, 2, 3, 4]:
        print(f'''
Номер введен некорректно, введите число от 1 до 4!
        ''')
        logging.info(f'Пользователь ввел число - {choose}, такой опции не предусмотрено.')

        inp()
        return

    logging.info(f'Пользователь выбрал опцию под номером {choose}')
    return choose

def main():
    while True:
        out()
        choose = inp()

        if choose == 1:
            file_r = open('data.txt', 'r', encoding='utf-8')
            file = list()
            for x in file_r.readlines():
                file.append(x.split(', '))

            print(f'''  
    Выберите действие:
        1. Сортировать список по рейтингу телепередач
        2. Сортировать по дате добавления в список
        3. Сортировать по длительности
        4. Выбрать другое действие''')
            logging.info('Пользователь получил на вывод опции вывода списка телепередач')

            choose1 = inp()
            logging.info(f'Пользователь выбрал опцию {choose1}')

            if choose1 == 1:
                sorted(file, key=itemgetter(2))
                file.sort(key=lambda x: x[2], reverse=True)
            elif choose1 == 3:
                sorted(file, key=itemgetter(1))
                file.sort(key=lambda x: x[1])
            elif choose1 == 4:
                continue

            print(f'''            
--<=====>--<СПИСОК ТЕЛЕПЕРЕДАЧ>--<=====>--''')
            for x in file:
                print(f'{file.index(x) + 1}. {x[0]}, длительность в минутах- {x[1]}, рейтинг - {x[2][:-1]}')

            logging.info('Пользователь получил на вывод список телепередач')

        if choose == 2:
            print(f'''            
--<=====>--<ДОБАВЛЕНИЕ ПЕРЕДАЧИ В СПИСОК>--<=====>--
''')

            file_r = open('data.txt', 'r', encoding='utf-8')
            name = input('Введите название передачи - ')

            flag = False
            for x in file_r.readlines():
                x = x.split(', ')
                if name in x:
                    print('Такая телепередача уже есть в списке!')
                    logging.info(f'Пользователь ввел название телепередачи - {name}, такая передача уже есть в списке')
                    flag = True
                    break

            if flag:
                continue

            while True:
                dll = input('Введите длительность в минутах - ')
                ratee = input('Введите рейтинг передачи - ').replace(',', '.')

                try:
                    dl = int(dll)
                    rate = float(ratee)
                except ValueError:
                    print('Данные введены неккоректно, рейтинг и длительность должны быть числового формата!')
                    logging.error(f'Пользователь ввел данные - "{dll}", "{ratee}" некорректного формата.')

                    continue

                if 0 <= rate <= 10 and 1 <= dl <= 600:
                    break
                elif rate < 0 or rate > 10:
                    print('Рейтинг должен быть от 0 до 10, попробуйте ввести еще раз')
                    logging.info(f'Пользователь ввел число - "{rate}", не входящее в диапазон рейтинга от 0 до 10')

                    continue
                else:
                    print('Длительность должна быть не менее 1 минуты, и не более 600 минут, попробуйте ввести еще раз')
                    logging.info(f'Пользователь ввел число - "{dl}", не входящее в диапазон длительности от 1 до 600 минут')

                    continue

            file_a = open('data.txt', 'a', encoding='utf-8')
            file_a.write(f'{name}, {dl}, {rate}')

            print(f'Вы добавили в список телепередачу: {name}, {dl}, {rate}')
            logging.info(f'Пользователь добавил в список телепередачу: {name}, {dl}, {rate}')

        if choose == 3:
            print(f'''            
--<=====>--<ПОИСК ПЕРЕДАЧИ ПО НАЗВАНИЮ>--<=====>--
            ''')

            file_r = open('data.txt', 'r', encoding='utf-8')
            name = input('Введите название передачи - ')
            logging.info(f'Пользователь начал поиск телепередачи по названию - {name}')

            flag = False
            for x in file_r.readlines():
                x = x.split(', ')
                if name in x:
                    print(f'Найдена телепередача: {x[0]}, {x[1]}, {x[2]}')
                    logging.info(f'Найдена телепередача: {x[0]}, {x[1]}, {x[2]}')
                    
                    flag = True
                    break

            if flag:
                continue
            else:
                print(f'Телепередачи "{name}" нет в списке!')
                logging.info(f'Телепередачи "{name}" нет в списке!')


        if choose == 4:
            print(f'''
До свидания!''')
            logging.info('Программа завершила выполнение.')
            
            break

main()
