#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : Multiplications game
# Version : 2.0.0
# Python  : 3.5.3
# License : MIT
# Author  : Gerard Bajona
# Created : 08/02/2019
# Changed : 30/10/2022
# URL     : http://github.com/gerardbm/scripts
# --------------------------------------------------
"""Little multiplications game for the terminal."""

import random
import datetime
import time
import os

def selector():
    """Show the main options menu and prompt the user to pick one."""
    print()
    print("Multiplications game")
    print("--------------------")
    print("Options menu:")
    print("  1. N×N digits")
    print("  2. N×NN digits")
    print("  3. NN×NN digits")
    print("  0. Quit")
    return get_option(0, 3)

def get_option(first, last):
    """Get and validate the option value as integer."""
    while True:
        try:
            print()
            option = int(input("Enter an option: "))
        except ValueError:
            print("> It must be an integer number.")
            continue
        else:
            if option < first or option > last:
                print("> Unknown option. Try it again.")
                continue
        return option

def letsplay(level):
    """Start the game and show the score at the end."""
    score = 0
    count = 0
    maxim = 10

    print()
    print("Game starts. Play!")

    start = time.time()
    while count < maxim:
        count = count + 1
        score = operation(score, count, level)
    end = time.time()

    rights = score
    wrongs = maxim-score
    percent = round((score/maxim)*100, 0)
    emoticon = emoticons(percent)
    color = colorize(percent)
    clean = '\033[0m'
    interval = end-start

    if rights == maxim:
        savetocsv(interval, level)

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
    print('> Time:', round(interval, 2), 'sec')
    print('> Rate:', round((interval)/maxim, 2), 'sec/question')
    print()

def operation(score, count, level):
    """Do a question and check the answer."""
    if level == 1:
        numb1 = random.randint(1, 9)
        numb2 = random.randint(1, 9)
    elif level == 2:
        numb1 = random.randint(1, 9)
        numb2 = random.randint(10, 99)
    elif level == 3:
        numb1 = random.randint(10, 99)
        numb2 = random.randint(10, 99)

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

def savetocsv(interval, level):
    """Save the result in a CSV file"""
    path = os.path.expanduser('~')
    name = str(path + "/.multistats")
    date = datetime.datetime.now()
    now = str(date.strftime("%d/%m/%Y %H:%M"))
    lvl = ', lvl: ' + str(level)
    sec = ', ' + str(round(interval, 2)) + ' sec\n'
    result = now + lvl + sec
    with open(name, 'a+', encoding='utf8') as file_handle:
        file_handle.write(result)

def main():
    """Main program."""
    option = selector()
    if option != 0:
        letsplay(option)
        main()
    else:
        print()
        print("Good bye :-)")

if __name__ == '__main__':
    main()
