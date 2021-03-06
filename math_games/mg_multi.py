#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : Multiplications
# Version : 1.1.0
# Python  : 3.5.3
# License : MIT
# Author  : Gerard Bajona
# Created : 08/02/2019
# Changed : 10/02/2019
# URL     : http://github.com/gerardbm/scripts
# --------------------------------------------------
"""Little multiplications game for the terminal."""

import random
import time

def operation(score, count):
    """Do a question and check the answer."""
    numb1 = random.randint(1, 9)
    numb2 = random.randint(1, 9)
    result = numb1*numb2
    problem = str(numb1) + "x" + str(numb2)
    enum = str(count).zfill(2)
    question = enum + ". The result of " + problem + " = "

    while True:
        print()
        answer = input(question)
        try:
            answer = int(answer)
            break
        except ValueError:
            print("--- It must be an integer number.")

    if answer == result:
        print("--- Good!")
        score = score + 1
    else:
        print("--- Wrong!")
        score = score + 0
    return score

def emoticons(percent):
    """Display an emoticon face according to the result."""
    if percent == 100:
        emoticon = ':-)'
    elif percent >= 50 < 100:
        emoticon = ':-|'
    elif percent >= 20 < 50:
        emoticon = ':-('
    else:
        emoticon = ':_('
    return emoticon

def main():
    """Start the game and show the score at the end."""
    score = 0
    count = 0
    maxim = 10

    print()
    print("Game starts. Play!")

    start = time.time()
    while count < maxim:
        count = count + 1
        score = operation(score, count)
    end = time.time()

    rights = score
    wrongs = maxim-score
    percent = round((score/maxim)*100, 0)
    emoticon = emoticons(percent)

    print()
    print("----------")
    print("|"*int(round((score/maxim)*10, 0)), str(percent) + "%", emoticon)
    print("----------")
    print()
    print("> Rights:", rights)
    print("> Wrongs:", wrongs)
    print()
    print('> Time:', round(end-start, 2), 'sec')
    print('> Rate:', round((end-start)/maxim, 2), 'sec/question')
    print()

    replay = input("Press 'q' to quit or anything else to play again. ")
    if replay.lower() == 'q':
        import sys
        sys.exit()
    else:
        main()

if __name__ == '__main__':
    main()
