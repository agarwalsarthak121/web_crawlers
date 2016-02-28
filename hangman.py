#! /usr/bin/python3

import random

fr = open('movies.txt','r')
movie_name = fr.read()
movie_name = movie_name.split('\n')
i = random.randint(0,len(movie_name)-2)
movie = movie_name[i]
letters = []
display = []
for letter in movie:
    if letter == ' ':
        letters.append(letter)
        display.append(letter)
    else:
        letters.append(letter)
        display.append('_')
print (''.join(display))
print ()

guess_left = 5
print ('You have '+str(guess_left)+' guesses available')
guess_letters = []

while True:
    while True:
        guess = input('Enter an alphabet: ')
        if guess.lower() in guess_letters or guess.upper() in guess_letters:
            continue
        else:
            break
    count = 0
    guess_letters.append(guess)
    
    for i in range(0,len(letters)):
        if guess.lower() == letters[i] or guess.upper() == letters[i]:
            display[i] = letters[i]
            count += 1
            
    print (''.join(display))
    print ()
    if display == letters:
        print ('Congrats you won!!')
        break
    if count == 0 :
        guess_left -= 1
        if guess_left == 0:
            print ('No more guesses left')
            print ()
            print ('Righ answer: '+movie)
            break
        print ('Wrong Guess , Guesses left = '+str(guess_left)+' ,Guess again')
        print ()
    else :
        print ('Guess again')
        print ()

print ('Game Over')
