#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : Multiplications
# Version : 1.2.0
# Python  : 3.5.3
# License : MIT
# Author  : Gerard Bajona
# Created : 08/02/2019
# Changed : 18/07/2022
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
        print('\033[32m' + "--- Good!" + '\033[0m')
        score = score + 1
    else:
        print('\033[31m' + "--- Wrong!" + '\033[0m')
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

def colorize(percent):
    """Colorize the result"""
    if percent == 100:
        color = '\033[32m'
    elif percent >= 50 < 100:
        color = '\033[36m'
    elif percent >= 20 < 50:
        color = '\033[33m'
    else:
        color = '\033[31m'
    return color

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
    color = colorize(percent)
    clean = '\033[0m'

    if percent > 0:
        bars = "█"*int(round((score/maxim)*10, 0))
    else:
        bars = "X"

    print()
    print(color + bars, str(percent) + "%", emoticon + clean)
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
