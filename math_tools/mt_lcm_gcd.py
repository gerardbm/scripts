#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : LCM & GCD
# Version : 1.0.0
# Python  : 3.8.0
# License : MIT
# Author  : Gerard Bajona
# Created : 17/07/2022
# Changed : 17/07/2022
# URL     : http://github.com/gerardbm/scripts
# --------------------------------------------------
"""LCM & GCD calculator"""

from numpy import lcm,gcd

def main_menu():
    """Show the main options menu and prompt the user to pick one."""
    print()
    print("LCM & GCD calculator")
    print("--------------------")
    print("Options menu:")
    print("  1. Enter numbers")
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

def get_numbers():
    """Get numbers separated by comma"""
    while True:
        try:
            numbers = list(map(int,
                input("\nEnter integers separated by comma: ").split(",")))
        except ValueError:
            print("> It must be a list of integers separated by comma.")
            continue
        return numbers

def get_lcm_gcd(values):
    """LCM & GCD"""
    if len(values) > 2:
        result_lcm = lcm.reduce([*values])
        result_gcd = gcd.reduce([*values])
    else:
        result_lcm = lcm(*values)
        result_gcd = gcd(*values)

    print()
    print("> LCM =", result_lcm)
    print("> GCD =", result_gcd)

def main():
    """Main program."""
    main_option = 1
    while main_option != 0:
        main_option = main_menu()
        if main_option == 1:
            values = get_numbers()
            get_lcm_gcd(values)
        else:
            print()
            print("Good bye :-)")

if __name__ == '__main__':
    main()
