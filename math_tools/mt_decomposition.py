#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : Prime Factors Decomposition
# Version : 1.0.1
# Python  : 3.5.3
# License : MIT
# Author  : Gerard Bajona
# Created : 02/06/2018
# Changed : 12/08/2018
# URL     : http://github.com/gerardbm/scripts
# --------------------------------------------------
"""This script is a tool to decompose a number into prime factors."""

import time

def main_menu():
    """Show the main options menu and prompt the user to pick one."""
    print()
    print("Prime Factors Decomposition")
    print("---------------------------")
    print("Options menu:")
    print("  1. Enter a number")
    print("  0. Quit")
    return get_option(0, 1)

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

def get_number():
    """Get a number to decompose into prime factors."""
    while True:
        try:
            print()
            number = int(input("Enter a number to decompose: "))
            break
        except ValueError:
            print("> Wrong format, type numbers instead.")
            print("> (Decimals not allowed: type an integer).")
    return number

def decomposition(number):
    """Decompose the number into prime factors!"""
    dividend = number
    divisor = 2
    columns = []
    factors = []
    while dividend >= divisor:
        while dividend % divisor == 0:
            aligned = abs(len(str(dividend)) - len(str(number)))
            columns.extend([
                " ",
                " " * aligned,
                dividend,
                " | ",
                divisor,
                "\n",
            ])
            dividend = int(dividend / divisor)
            factors.extend([divisor])
        divisor = divisor + 1
    return columns, factors, divisor

def format_group(factors):
    """Formatted output: group factors and exponents."""
    grouped = []
    for factor in factors:
        exponent = factors.count(factor)
        grouped.extend([(factor, exponent)])
    grouped = sorted(set(grouped))
    return grouped

def format_join(grouped):
    """Formatted output: join factors and exponents."""
    joined = []
    for group in grouped:
        group = '^'.join(map(str, group))
        joined.extend([group])
    joined = ' * '.join(map(str, joined))
    return joined

def output(joined, columns, number, factors, divisor):
    """Show the result."""
    lennum = int(len(str(number)) + 3)
    lendiv = int(len(str(divisor)))
    columns = ''.join(map(str, columns))
    print()
    print(" " + ("-" * (lennum)) + ("-" * lendiv))
    print(columns)
    print('Prime decomposition:')
    print('>>', number, '=', ' * '.join(map(str, factors)))
    print()
    print('Exponential form:')
    print('>>', number, '=', joined)
    print()

def main():
    """Main program."""
    main_option = 1
    while main_option != 0:
        main_option = main_menu()
        if main_option == 1:
            number = get_number()
            start = time.time()
            columns, factors, divisor = decomposition(number)
            grouped = format_group(factors)
            joined = format_join(grouped)
            output(joined, columns, number, factors, divisor)
            end = time.time()
            print('Time required:')
            print('>>', round(end-start, 5), 'sec')
            print()
            input("Press Enter to continue...")
        else:
            print()
            print("Good bye :-)")

if __name__ == '__main__':
    main()
