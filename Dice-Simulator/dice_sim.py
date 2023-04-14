import random

def roll():
    check = input('Wanna play?(Y/n): ')
    while check == 'Y':
        num = random.randint(1,6)
        print(f'Your number is: {num}\n\n')
        check = input('Play more?(Y/n)')
        # if not check:
        #     break

roll()