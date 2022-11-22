from hangman_art import HANGMANPICS
import os
import random

with open("word_dict.txt") as f:
    vocab = f.readlines()
vocab = [v.strip() for v in vocab]

random_word = random.choice(vocab)
vocab_len = len(random_word)
re = list('_' * vocab_len)

lives = 6
while lives:
    re_join = ''.join(re)
    if re_join == random_word:
        break

    print(re_join)
    guess = input('Let guess the word: ')
    for index in range(len(random_word)):
        if guess == random_word[index]:
            re[index] = guess
    
    if guess not in random_word:
        lives -= 1
    os.system("clear")
    print(HANGMANPICS[6 - lives])

if lives > 0:
    print("Congratulations you win")
else:
    print("You lose") 
    print("Psst the word is {}".format(random_word))