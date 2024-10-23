def countdown():
    while True:
        try:
            x = int(input('Введи целое, положительное число '))
            if x > 0:
                break
            else:
                print('Это не положительное', '\n')
        except ValueError:(
            print('Это не число', '\n'))
    while x >= 0:
        print(x)
        x -= 1


countdown()
