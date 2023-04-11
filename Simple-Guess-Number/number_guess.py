import random

def guess():
    number_to_guess = random.randint(1, 100)

    print("I have choosen a number in between 1 to 100, guess it mate!!!\n")
    while True:
        user_num = int(input("Guess the number: "))
        if user_num == number_to_guess:
            print("You guessed it correctly mate!! Congratulation!!")
            break
        else:
            if user_num < (number_to_guess//2):
                print("Your guess is less than my number when divided by 2\n")
            elif user_num == (number_to_guess//2):
                print("You are almost halfway there\n")
            elif (user_num - number_to_guess) > 10:
                print("You are coming close, keep guessing!!")
            elif abs(user_num - number_to_guess) <= 10:
                print(f"You are off by {number_to_guess - user_num}") if user_num < number_to_guess else print(f"You are guessed more by {user_num - number_to_guess}")
            elif user_num > number_to_guess:
                print("You have guessed way more than my number!!")

guess()    
        