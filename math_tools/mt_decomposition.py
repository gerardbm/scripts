#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : Decomposition
# Version : 0.1.0
# Python  : 3.5.3
# License : MIT
# Author  : Gerard Bajona
# Created : 02/06/2018
# Changed : 10/08/2018
# URL     : http://github.com/gerardbm/scripts
# --------------------------------------------------
"""This script is a tool to decompose a number into prime factors."""

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

def decomposition(given_num):
    """Decompose!"""
    print()
    print("  ", given_num, " ")
    print("", "-" * (len(str(given_num)) + 4))

    decom_num = given_num
    divisor = 2
    factors = []

    while decom_num >= divisor:
        while decom_num % divisor == 0:
            align = abs(len(str(decom_num)) - len(str(given_num)))
            factors.extend([divisor])
            print(" " * align, decom_num, "|", divisor)
            decom_num = int(decom_num / divisor)
        divisor = divisor + 1

    grouped = []

    for factor in factors:
        exponent = factors.count(factor)
        grouped.extend([(factor, exponent)])

    grouped = set(grouped)

    result = []

    for group in grouped:
        group = '^'.join(map(str, group))
        result.extend([group])

    result = ' * '.join(map(str, result))

    print()
    print('The prime factorization is:')
    print('>>', ' * '.join(map(str, factors)))
    print()
    print('In exponential form:')
    print('>>', result)
    print()
    input("Press Enter to continue...")

def main():
    """Main program."""
    main_option = 1
    while main_option != 0:
        main_option = main_menu()
        if main_option == 1:
            number = get_number()
            decomposition(number)
        else:
            print()
            print("Good bye :-)")

if __name__ == '__main__':
    main()
