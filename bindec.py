#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : bindec
# Version : 1.0.3
# License : MIT
# Author  : Gerard Bajona
# Created : 11/11/2017
# Changed : 14/11/2017
# URL     : http://github.com/gerardbm/scripts
# --------------------------------------------------
"""This script is a tool to convert the units of data storage between the
decimal system (SI prefixes) and the binary system (IEC prefixes)."""

def selector():
    """Show the main options menu and prompt the user to pick one."""
    print()
    print("Data Storage Units Converter")
    print("----------------------------")
    print("Options menu:")
    print("  1. Convert from decimal system (SI) to binary system (IEC)")
    print("  2. Convert from binary system (IEC) to decimal system (SI)")
    print("  0. Quit")
    option = validate_int()
    while option < 0 or option > 2:
        print("Unknown option. Try it again.")
        option = validate_int()
    return option

def storage():
    """Prompt the user to enter an amount of data storage."""
    while True:
        print()
        amount = input("Enter the amount of data storage to convert: ")
        try:
            amount = float(amount)
            break
        except ValueError:
            print()
            print("Wrong format, type numbers instead.")
            print("(Decimals allowed: use a point as separator).")
    return amount

def binary_menu():
    """Show the binary system menu and prompt the user to pick one."""
    print()
    print("Binary system (IEC):")
    print("  1. KiB (kibibyte)")
    print("  2. MiB (mebibyte)")
    print("  3. GiB (gibibyte)")
    print("  4. TiB (tebibyte)")
    print("  5. PiB (pebibyte)")
    print("  6. EiB (exbibyte)")
    print("  7. ZiB (zebibyte)")
    print("  8. YiB (yobibyte)")
    option = validate_int()
    while option < 1 or option > 8:
        print("Unknown option. Try it again.")
        option = validate_int()
    return option

def decimal_menu():
    """Show the decimal system menu and prompt the user to pick one."""
    print()
    print("Decimal system (SI):")
    print("  1. kB (kilobyte)")
    print("  2. MB (megabyte)")
    print("  3. GB (gigabyte)")
    print("  4. TB (terabyte)")
    print("  5. PB (petabyte)")
    print("  6. EB (exabyte)")
    print("  7. ZB (zettabyte)")
    print("  8. YB (yottabyte)")
    option = validate_int()
    while option < 1 or option > 8:
        print("Unknown option. Try it again.")
        option = validate_int()
    return option

def binary_values():
    """Determine the equivalent power for each IEC prefix."""
    binopt = binary_menu()
    if binopt == 1:
        binval = 10
        binpre = "KiB"
    elif binopt == 2:
        binval = 20
        binpre = "MiB"
    elif binopt == 3:
        binval = 30
        binpre = "GiB"
    elif binopt == 4:
        binval = 40
        binpre = "TiB"
    elif binopt == 5:
        binval = 50
        binpre = "PiB"
    elif binopt == 6:
        binval = 60
        binpre = "EiB"
    elif binopt == 7:
        binval = 70
        binpre = "ZiB"
    elif binopt == 8:
        binval = 80
        binpre = "YiB"
    system = "(IEC)"
    return binval, binpre, system

def decimal_values():
    """Determine the equivalent power for each SI prefix."""
    decopt = decimal_menu()
    if decopt == 1:
        decval = 3
        decpre = "kB"
    elif decopt == 2:
        decval = 6
        decpre = "MB"
    elif decopt == 3:
        decval = 9
        decpre = "GB"
    elif decopt == 4:
        decval = 12
        decpre = "TB"
    elif decopt == 5:
        decval = 15
        decpre = "PB"
    elif decopt == 6:
        decval = 18
        decpre = "EB"
    elif decopt == 7:
        decval = 21
        decpre = "ZB"
    elif decopt == 8:
        decval = 24
        decpre = "YB"
    system = "(SI)"
    return decval, decpre, system

def validate_int():
    """If the user is not entering an integer, catch the error."""
    while True:
        print()
        option = input("Enter an option: ")
        try:
            option = int(option)
            break
        except ValueError:
            print()
            print("It must be an integer number.")
    return option

def convertd2b(amount, x_pow, y_pow, decpre, binpre):
    """Apply the equation to get the result (decimal to binary direction)."""
    res = amount * (10 ** x_pow / 2 ** y_pow)
    cad = str(round(res, 3))
    d2b = str(amount) + " " + decpre + " = " + cad + " " + binpre
    return d2b

def convertb2d(amount, x_pow, y_pow, decpre, binpre):
    """Apply the equation to get the result (binary to decimal direction)."""
    res = amount * (2 ** y_pow / 10 ** x_pow)
    cad = str(round(res, 3))
    b2d = str(amount) + " " + binpre + " = " + cad + " " + decpre
    return b2d

def user_request(amount, pre_a, pre_b, sys_a, sys_b):
    """Print the requested options before showing the result."""
    requested = "You selected to convert " + str(amount) + " "
    requested += pre_a + " " + sys_a + " to " + pre_b + " " + sys_b
    return requested

def display(entered, result):
    """Display de selected options and the result.
    Wait for a keypress (Enter) at the end."""
    print()
    print(">>", entered)
    print(">> Result:", result)
    print()
    input("Press Enter to continue...")

def main():
    """According to the first selected option, do the conversion in one
    direction (binary to decimal) or in another (decimal to binary).
    Finally, display the conversion result."""
    main_option = 1
    while main_option != 0:
        main_option = selector()
        if main_option == 1:
            myval = storage()
            decval, decpre, decsys = decimal_values()
            binval, binpre, binsys = binary_values()
            entered = user_request(myval, decpre, binpre, decsys, binsys)
            result = convertd2b(myval, decval, binval, decpre, binpre)
            display(entered, result)
        elif main_option == 2:
            myval = storage()
            binval, binpre, binsys = binary_values()
            decval, decpre, decsys = decimal_values()
            entered = user_request(myval, binpre, decpre, binsys, decsys)
            result = convertb2d(myval, decval, binval, decpre, binpre)
            display(entered, result)
        else:
            print()
            print("Good bye :-)")

main()
