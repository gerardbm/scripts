#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name     : bindec
# Version  : 1.0.0
# Author   : Gerard Bajona
# License  : MIT
# --------------------------------------------------

def main_menu():
    print()
    print("What do you want to do?")
    print("  1. Convert binary to decimal")
    print("  2. Convert decimal to binary")
    print("  0. Quit")
    option = validate_int()
    while option < 0 or option > 2:
        print("Unknown option. Try it again.")
        option = validate_int()
    return option

def storage():
    while True:
        print()
        amount = input("Enter the amount of storage to convert: ")
        try:
            amount = float(amount)
            break
        except ValueError:
            print()
            print("Wrong format, type numbers instead.")
    return amount

def binary_menu():
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
    binopt = binary_menu()
    if binopt == 1:
        binval = 10
        binpre = "KiB (IEC)"
    elif binopt == 2:
        binval = 20
        binpre = "MiB (IEC)"
    elif binopt == 3:
        binval = 30
        binpre = "GiB (IEC)"
    elif binopt == 4:
        binval = 40
        binpre = "TiB (IEC)"
    elif binopt == 5:
        binval = 50
        binpre = "PiB (IEC)"
    elif binopt == 6:
        binval = 60
        binpre = "EiB (IEC)"
    elif binopt == 7:
        binval = 70
        binpre = "ZiB (IEC)"
    elif binopt == 8:
        binval = 80
        binpre = "YiB (IEC)"
    return binval, binpre

def decimal_values():
    decopt = decimal_menu()
    if decopt == 1:
        decval = 3
        decpre = "kB (SI)"
    elif decopt == 2:
        decval = 6
        decpre = "MB (SI)"
    elif decopt == 3:
        decval = 9
        decpre = "GB (SI)"
    elif decopt == 4:
        decval = 12
        decpre = "TB (SI)"
    elif decopt == 5:
        decval = 15
        decpre = "PB (SI)"
    elif decopt == 6:
        decval = 18
        decpre = "EB (SI)"
    elif decopt == 7:
        decval = 21
        decpre = "ZB (SI)"
    elif decopt == 8:
        decval = 24
        decpre = "YB (SI)"
    return decval, decpre

def validate_int():
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

def convertd2b(n, x, y, decpre, binpre):
    res = n * (10**x/2**y)
    cad = str(round(res, 3))
    d2b = str(n) + " " + decpre + " = " + cad + " " + binpre
    return d2b

def convertb2d(n, x, y, decpre, binpre):
    res = n * (2**y/10**x)
    cad = str(round(res, 3))
    b2d = str(n) + " " + binpre + " = " + cad + " " + decpre
    return b2d

def init():
    main_option = 1
    while main_option != 0:
        main_option = main_menu()
        if main_option == 1:
            myval = storage()
            binval, binpre = binary_values()
            decval, decpre = decimal_values()
            print()
            print("- RESULT:", \
                    convertb2d(myval, decval, binval, decpre, binpre))
        elif main_option == 2:
            myval = storage()
            decval, decpre = decimal_values()
            binval, binpre = binary_values()
            print()
            print("- RESULT:", \
                    convertd2b(myval, decval, binval, decpre, binpre))
        else:
            print()
            print("Good bye :-)")

init()
