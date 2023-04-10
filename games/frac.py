#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : Fractions game
# Version : 1.0.0
# Python  : 3.5.3
# License : MIT
# Author  : Gerard Bajona
# Created : 10/04/2023
# URL     : http://github.com/gerardbm/scripts
# --------------------------------------------------
"""Little fractions game for the terminal."""

import random
import operator
import datetime
import time
import os

def selector():
    """Show the main options menu and prompt the user to pick one."""
    print()
    print("Multiplications game")
    print("--------------------")
    print("Options menu:")
    print("  1. N/N digits")
    print("  2. NN/NN digits")
    print("  0. Quit")
    return get_option(0, 2)

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
        num1 = random.randint(1, 9)
        den1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        den2 = random.randint(1, 9)
    elif level == 2:
        num1 = random.randint(1, 99)
        den1 = random.randint(1, 99)
        num2 = random.randint(1, 99)
        den2 = random.randint(1, 99)

    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    op = random.choice(list(ops.keys()))
    result = round(ops.get(op)(num1/den1,num2/den2), 2)

    problem = str(num1) + "/" + str(den1) + " " + str(op) + " " + str(num2) + "/" + str(den2)
    question = str(count).zfill(2) + ". The result of " + problem + " = "

    while True:
        print()
        answer = input(question)
        try:
            num3,den3 = map(float, answer.split('/'))
            break
        except ValueError:
            print("--- It must be a fraction.")

    if result == round(num3/den3, 2):
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
    name = str(path + "/.fractionstats")
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
