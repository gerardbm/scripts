#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Name    : Data Storage Units Converter
# Version : 1.1.0
# Python  : 3.5.3
# License : MIT
# Author  : Gerard Bajona
# Created : 11/11/2017
# Changed : 21/05/2018
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
    print("  3. Configuration")
    print("  0. Quit")
    return get_option(0, 3)

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
    return get_option(1, 8)

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
    return get_option(1, 8)

def config_menu():
    """Show the configuration menu."""
    print()
    print("Configuration:")
    print("  1. Decimals number")
    print("  0. Back menu")
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

def get_storage():
    """Get and validate the storage value as float."""
    while True:
        try:
            print()
            amount = float(input("Enter the amount of data storage: "))
            break
        except ValueError:
            print("> Wrong format, type numbers instead.")
            print("> (Decimals allowed: use a point as separator).")
    return amount

def get_decimals():
    """Get and validate the decimals option."""
    while True:
        try:
            print()
            decimals = int(input("Enter the number of decimals: "))
            break
        except ValueError:
            print("> It must be an integer number")
    return decimals

def binary_values():
    """Determine the equivalent power for each IEC prefix."""
    binopt = binary_menu()
    if binopt == 1:
        binpow = 10
        binpre = "KiB"
    elif binopt == 2:
        binpow = 20
        binpre = "MiB"
    elif binopt == 3:
        binpow = 30
        binpre = "GiB"
    elif binopt == 4:
        binpow = 40
        binpre = "TiB"
    elif binopt == 5:
        binpow = 50
        binpre = "PiB"
    elif binopt == 6:
        binpow = 60
        binpre = "EiB"
    elif binopt == 7:
        binpow = 70
        binpre = "ZiB"
    elif binopt == 8:
        binpow = 80
        binpre = "YiB"
    system = "(IEC)"
    return binpow, binpre, system

def decimal_values():
    """Determine the equivalent power for each SI prefix."""
    decopt = decimal_menu()
    if decopt == 1:
        decpow = 3
        decpre = "kB"
    elif decopt == 2:
        decpow = 6
        decpre = "MB"
    elif decopt == 3:
        decpow = 9
        decpre = "GB"
    elif decopt == 4:
        decpow = 12
        decpre = "TB"
    elif decopt == 5:
        decpow = 15
        decpre = "PB"
    elif decopt == 6:
        decpow = 18
        decpre = "EB"
    elif decopt == 7:
        decpow = 21
        decpre = "ZB"
    elif decopt == 8:
        decpow = 24
        decpre = "YB"
    system = "(SI)"
    return decpow, decpre, system

def convertd2b(amount, x_pow, y_pow):
    """Apply the equation to get the result. Decimal to binary."""
    res = amount * (10 ** x_pow / 2 ** y_pow)
    return res

def convertd2b_(res, decimals):
    """Round the result."""
    cad = str(round(res, decimals))
    return cad

def convertd2b__(amount, cad, decpre, binpre):
    """Return the result with the equality."""
    d2b = str(amount) + " " + decpre + " = " + cad + " " + binpre
    return d2b

def convertb2d(amount, x_pow, y_pow):
    """Apply the equation to get the result. Binary to decimal."""
    res = amount * (2 ** y_pow / 10 ** x_pow)
    return res

def convertb2d_(res, decimals):
    """Round the result."""
    cad = str(round(res, decimals))
    return cad

def convertb2d__(amount, cad, decpre, binpre):
    """Return the result with the equality."""
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
    decimals = 2
    while main_option != 0:
        main_option = selector()
        if main_option == 1:
            amount = get_storage()
            decpow, decpre, decsys = decimal_values()
            binpow, binpre, binsys = binary_values()
            entered = user_request(amount, decpre, binpre, decsys, binsys)
            res = convertd2b(amount, decpow, binpow)
            cad = convertd2b_(res, decimals)
            d2b = convertd2b__(amount, cad, decpre, binpre)
            display(entered, d2b)
        elif main_option == 2:
            amount = get_storage()
            binpow, binpre, binsys = binary_values()
            decpow, decpre, decsys = decimal_values()
            entered = user_request(amount, binpre, decpre, binsys, decsys)
            res = convertb2d(amount, decpow, binpow)
            cad = convertb2d_(res, decimals)
            b2d = convertb2d__(amount, cad, decpre, binpre)
            display(entered, b2d)
        elif main_option == 3:
            config_option = 1
            while config_option != 0:
                config_option = config_menu()
                if config_option == 1:
                    decimals = get_decimals()
                else:
                    print()
                    print("Back to main menu!")
        else:
            print()
            print("Good bye :-)")

if __name__ == '__main__':
    main()
