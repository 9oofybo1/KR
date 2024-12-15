# Исполнитель
Потапкин Максим

Фт-230008
# Курсовая работа - Обработка массива данных. Телепередачи
## Постановка задачи
Разработать программу по обработке заданного множества данных.
Множество данных представляет собой массив структур. Для всех вариантов
необходимо обеспечить реализацию следующих функций:
1. вывод информации из текстового файла в массив структур;
2. добавление новых элементов в конец массива;
3. просмотр всех элементов массива;
4. поиск элементов в массиве структур по заданному текстовому полю;
5. сортировка массива по числовому полю;
6. сохранение массива структур в текстовый файл.

# Среда разработки
Язык программирования: Python.

Среда разработки: PyCharm.

# Инструкция по работе
При запуске программа предлагает пользователю несколько опций:
1. Вывести список телепередач
     Пользователь выбирает сортировку списка, по рейтингу, по дате добавления, по длительности передачи, после чего программа выводит список телепередач из текстового файла, полученного на вход;
2. Добавить новую телепередачу в список
     Пользователь вводит данные о телепередаче, которую хочет добавить в список, после чего передача сохраняется в текстовом файле;
3. Поиск по названию телепередачи
     Пользватель вводит название телепередачи, если передача с таким названием есть в списке, программа выводит данные о ней, если нет, то сообщает об этом пользователю;
4. Выйти
     Программа заканчивает работу, выводя пользователю сообщение - "До свидания".
   
В программе реализована обработка ошибок ввода данных числового формата, допустим, в случае если пользователь вводит длительность передачи не в числовом формате, программа сообщает о некорректности введенных данных и предоставляет новую попытку ввода.
