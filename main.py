import random

def is_valid(number, right_range=100):
    if number.isdigit() and 1<= int(number) <= right_range:
        return True
    else: return False

def quess_the_number():
    right_range = input('Введите от 1 до скольки __ загадать число ?')
    if right_range.strip().isdigit() == False:
        print('Введите целое число больше 1 ')
    else:
        right_range = int(right_range)
        num = random.randint(1, right_range)
        print(num)
        print('Добро пожаловать в числовую угадайку')
        counter = 0
        flag = True
        while True:
            quess = input('Введите число:')
            counter += 1
            if is_valid(quess, right_range) == False:
                print(f'Введите целое число от 1 до {right_range}!')
                continue
            else: quess = int(quess)
            if quess < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')

            elif quess > num:
                print('Ваше число больше загаданного, попробуйте еще разок')

            else:
                print('-'*50)
                print(f'Вы угадали с {counter} попытки, поздравляем!')

                while True:
                    if flag == True:
                        regame = input('Хотите сиграть еще разок ? (да/нет)')
                        if regame.lower().strip() == 'да':
                            return True
                        elif regame.lower().strip() == 'нет':
                            return False

                        else: print('Введите да или нет ')
                    elif flag == False:
                        continue





while True:
    again = quess_the_number()
    if again == True:
        again = quess_the_number()
    elif again == False:
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')