def countdown():
    try:
        x = int(input('Введи целое, положительное число '))
        while True:
            if x > 0:
                break
            else:
                print('Это не положительное', '\n')
                x = int(input('Введи целое, положительное число '))
    except ValueError:
        print('Это не число', '\n')
    while x >= 0:
        print(x)
        x -= 1


countdown()
