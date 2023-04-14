import random

def hang():
    f = open('words.txt', 'r')
    data = f.readline()
    words = data.split()
    word = random.choice(words)

    print('Welcome to the Hangman Game, Let\'s start guessing!!!\n\n')
    to_guess = '-'*len(word)
    total_chances = len(word) + 3 #let's give them some leeway, fiddle with it to introduce difficulty

    while True:
        print(to_guess)
        guess = input('Guess the word: ').upper()
        if guess in word:
            index = word.find(guess)
            to_guess = to_guess[:index] + guess + to_guess[index+1:]
            word = word[:index] + '$' + word[index+1:]
            word.replace(guess, '$')
        total_chances -= 1
        print(f'Your remaining chances are {total_chances}\n\n')
        if total_chances == 0:
            print('Sorry your time is up mate!!')
            break
        if '-' not in to_guess:
            print('Congratulation, You have guessed the word!!!')
            break
            

hang()