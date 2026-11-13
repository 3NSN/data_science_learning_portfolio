#объявляю переменные max_number = None и min_number = None
#запрашиваю ввод чисел от пользователя через input
#проверяю, ввел ли пользователь done и выхожу из программы break
#пробую перевести ввод в число float
#если это не число, вывожу ошибку и возвращаюсь в начало цикла
#если число, сравниваю с None (if None) и сравниваю число с самым большим max_number (if >max_number)
#если true записываю полученное число в max_number
#тут же сравниваю с None и с min_number (if < min_number)
#если меньше, то записываю это число в мин_намбер
#за пределами цикла вывожу max_number и minnumber

max_number = None
min_number = None
while True:
    number = input('Enter number: ')
    if number == 'done':
        break
    try:
        number = float(number)
        if max_number is None or number > max_number:
            max_number = number
        if min_number is None or number < min_number:
            min_number = number
    except:
        print('Input error')
        continue
print(max_number, min_number)