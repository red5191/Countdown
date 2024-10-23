print('Начинаем обратный отсчет!')


def countdown():
    while True:
        try:
            x = int(input('Введи целое, положительное число '))
            while True:
                if x > 0:
                    print(x)
                    x = (x - 1)
                elif x < 0:
                    print('Это не положительное', '\n')
                    x = int(input('Введи целое, положительное число '))
                else:
                    print(f'{x} Отсчет закончен', '\n')
                    break
            break
        except ValueError:
            print('Это не число', '\n')


countdown()


def repeater():
    while True:
        answer = (input('Ещё разок? (да/нет) ')).lower()
        correct = ['да', 'нет']
        while answer not in correct:
            print('Это да или нет?', '\n')
            answer = (input('Ещё разок? (да/нет) ')).lower()
        if answer == 'да':
            countdown()
        else:
            print('Ну и ладно')
            break


repeater()
