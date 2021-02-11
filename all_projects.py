#-------------------------------------------------#
#импорт библиотек
import time
import random2 as random
#-------------------------------------------------#
#все глобальные переменные
k = 0
password = 'sshh'
#-------------------------------------------------#
#помощь
def helps():
    print('Это помощник по боту. Тут будут ссылки на создателя и небольшая информация обо мне и о создателе:\n')
    print('Версия меня: 0.1.7\n')
    print('ссылки на создателя:\nВКонтакте: https://vk.com/darkangel58414\nGit-hub: https://github.com/droid-darkangel\nTelegram: @darkangel58414\n')
    print('Моя первая версия была написана спустя пол года, как мой создатель решил писать на Python\n')
    print('Удачи тебе в следующем запуске меня!')
    check = input('back или exit: ')
    if check == 'back':
        main_screen()
    if check == 'exit':
        exit()
#-------------------------------------------------#
#квадратные уравнения
def kvad_uravn():
    print('Тут вычисляются квадратные уравнения')
    print('Возможны большие числа после запятой, поэтому округляйте сами')
    a = float(input('Введите коэфицент a: '))
    b = float(input('Введите коэфицент b: '))
    c = float(input('Введите коэфицент c: '))
    D = float(b*b-4*a*c)

    def dis_bol_a(b, D):
        ax = float((-b-D**0.5)/(2*a))
        return ax
    def dis_bol_b(b, D):
        bx = float((-b+D**0.5)/(2*a))
        return bx
    def dis_rav(b):
        x = float((-b)/(2*a))
        return x

    if D > 0:
        ax = dis_bol_a(b, D)
        bx = dis_bol_b(b,D)
        print('x1 = ', ax)
        print('x2 = ', bx)
    if D == 0:
        x = dis_rav(b)
        print('x = ', x)
    if D < 0:
        print('Корней нет')
    choice = input('Ещё уравнение? да/нет: ')
    if choice == 'да':
        kvad_uravn()
    if choice == 'нет':
        main_screen()
#-------------------------------------------------#
#радиус и площадь
def radius_plochad():
    print('Тут вычисляется радиус и площадь окружности')
    print('Возможны большие числа после запятой, поэтому округляйте сами')
    while True:
        radius = int(input("Введите радиус: "))
        if radius >= 0:
            print("Длина окружности = ",  2  *  3.14  *  radius)
            print("Площадь = ", 3.14 * radius ** 2)
        else:
            print("Пожалуйста, введите положительное число")
        check = input('back или exit: ')
        if check == 'back':
            main_screen()
        if check == 'exit':
            main_screen()
            break
#-------------------------------------------------#
#корень из числа
def Koren():
    print('Вычисление корня из числа')
    print('Возможны большие числа после запятой, поэтому округляйте сами')
    n = float(input('Введите число: '))
    nk = float(n**0.5)
    print('Ваше число: ', nk)
    choice = input('ещё раз? да/нет: ')
    if choice == 'да':
        Koren()
    if choice == 'нет':
        main_screen()
#-------------------------------------------------#
#периметр и площадь
def perimetr_plochad():
    print('Тут вычисляется периметр и площадь прямоугольника')
    def plochad(x,y):
        return x*y
    def perimetr(x,y):
        return 2*(x+y)
    x = int(input('Введите длину первой стороны: '))
    y = int(input('Введите длину второй стороны: '))
    S = plochad(x,y)
    P = perimetr(x,y)
    print('Площадь равна: ',S)
    print('Периметр равен: ',P)
    check = input('back или exit: ')
    if check == 'back':
        main_screen()
    if check == 'exit':
        exit()
#-------------------------------------------------#
#игра blackjack
koloda = [6,7,8,9,10,2,3,4,11] * 4
random.shuffle(koloda)
def blackjack():
    print('Игра blackjack. Вам выпадает карта номиналом от 2 до 11. Вы должны набрать до 21 балла')
    count = 0
    botCount = 0
    while True:
        language = input('English или Русский язык или выйти? en/ru/exit\n')
        if language == 'en':
            count = 0
            botCount = 0
            while True:
                choice = input('Will you take a card? y/n\n')

                if choice == 'y':
                    current = koloda.pop()
                    print('You got a face value card %d' % current)
                    count += current

                    if count > 21:
                        print('Sorry, your score is over 21, you lost!')
                        print('Your score: %d points' % count)
                        break

                    elif count == 21:
                        print('Congratulations, you scored 21 points!')
                        print('Your opponent automatically lost!')
                        print('The game is over!')
                        break

                    else:
                        print('Your score: %d points' % count)

                elif choice == 'n' and count < 21:
                    botCount = random.randint(1, 21)
                    print('Game over, your have score: %d points!' % count)
                    print('Your opponent score: %d points' % botCount)
                    if count > botCount:
                        print('Your opponent lost!')
                    elif count < botCount:
                        print('Your opponent win!')
                    count = 0
                    botCount = 0
                    break

        if language == 'ru':
            count = 0
            botCount = 0
            while True:
                choice = input('Будете брать карту? да/нет\n')

                if choice == 'да':
                    current = koloda.pop()
                    print('Вам выпала карта номиналом: %d' % current)
                    count += current

                    if count > 21:
                        print('Извините, вы набрали больше 21 очка, вы проиграли!')
                        print('Ваш счёт: %d очков' % count)
                        break

                    elif count == 21:
                        print('Поздравляем, вы набрали 21 очко!')
                        print('Ваш противник автоматически проиграл!')
                        print('Игра окончена')
                        break

                    else:
                        print('Твой счёт: %d очков' % count)

                elif choice == 'нет' and count < 21:
                    botCount = random.randint(1, 21)
                    print('Игра окончена, ваш счёт: %d очков!' % count)
                    print('Счёт вашего противника: %d очков' % botCount)
                    if count > botCount:
                        print('Ваш противник проиграл вам')
                    elif count < botCount:
                        print('Ваш противник выиграл!')
                    count = 0
                    botCount = 0
                    break
        if language == 'exit':
            main_screen()
#-------------------------------------------------#
#шифр цезаря
def shifr():
    print('Шифр цезаря. Работает только на английском')
    print('Для того, что-бы выйти, перезапустите программуя')
    choise = input('начать или выйти: ')
    if choise == 'начать':
            def cipher(s,n):
                if s > 26:
                    s = s%26
                caesar=''
                for i in n:
                    if ord(i) >= ord('a') and ord(i)<=ord('z'):
                        if ord(i)+ s> ord('z'):
                            caesar = caesar+chr((ord(i)+s)-26)
                        else:
                            caesar = caesar+chr(ord(i)+s)
                    elif ord(i) >= ord('A') and ord(i)<=ord('Z'):
                        if ord(i)+s >> ord('Z'):
                            caesar = caesar + chr((ord(i)+s)-26)
                        else:
                            caesar = caesar + chr(ord(i)+s)
                    else:
                        caesar = caesar + i
                return caesar
            while True:
                def dec(s,n):
                    if s>>26:
                        s = s%26
                    caesar=""
                    for i in n:
                        if ord(i) >= ord('a') and ord(i) <= ord('z'):
                            if ord(i)-s<ord('a'):
                                caesar = caesar + chr((ord(i)-s)+26)
                            else:
                                caesar = caesar + chr(ord(i)-s)
                        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                            if ord(i)-s < ord('A'):
                                caesar = caesar + chr((ord(i)-s)+26)
                        else:
                            caesar = caesar + chr(ord(i)-s)
                    else:
                        caesar = caesar + i
                    return caesar
                s = input("Введите число здвига букв - ")
                n = input("Введите текст (на английском) - ")
                print (cipher(int(s),n))
    if choise == 'выйти':
        main_screen()
#-------------------------------------------------#
#выбор уравнений
def uravn():
    print('Выбор уравнений')
    print('доступно: радиус и площадь окружности/ периметр и площадь прямоугольника/ квадратные уравнения/ вычисление корня из числа/ выход из меню')
    seek_urav = input('выберите: R_S/P_S/KV/KOR/exit: ')
    if seek_urav == 'R_S':
        radius_plochad()
    if seek_urav == 'P_S':
        perimetr_plochad()
    if seek_urav == 'KV':
        kvad_uravn()
    if seek_urav == 'KOR':
        Koren()
    if seek_urav == 'exit':
        main_screen()
#-------------------------------------------------#
def games():
    print('Выбор игры')
    print('Доступно: blackjack')
    print('Пожалуйста, при выборе игры, пишите так как она написана')
    game = input('Выберите игру: ')
    if game == 'blackjack':
        blackjack()
#-------------------------------------------------#
#главный экран
def main_screen():
    print('Приветствую тебя! Я приложение со всеми созданными программами моего создателя, на 11.02.2021.')
    print('вот, что я умею: помощь/ игры/ шифр цезаря/ уравнения и математические задачи/ выход')
    seek = input('Выберите help/games/cipher/urav/exit: ')
    if seek == 'games':
        games()
    if seek == 'cipher':
        shifr()
    if seek == 'help':
        helps()
    if seek == 'urav':
        uravn()
    if seek == 'exit':
        exit()
#-------------------------------------------------#
#загрузочная анимация
def loading(x):
    for a in range(x+1, 1, -1):
        print('*'*a)
        time.sleep(0.45)
    main_screen()
#-------------------------------------------------#
#ввод пароля
while k<3:
    try:
        password1 = input("Введите пароль: ")
        if password1 == password:
            print("Добро пожаловать")
            x = random.randint(7, 20)
            loading(x)
            break
        if password1 != password:
            raise ValueError
    except ValueError:
        print("Доступ запрещен")
        k += 1
if k == 3:
    print('Закончились попытки ввода. Пожалуйста перезагрузите программу и попробуйте ещё раз')
    exit()
#-------------------------------------------------#