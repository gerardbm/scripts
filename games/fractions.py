#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Aquí tens un exemple de programa en Python que permet fer operacions amb fraccions:

# python
# Copy code
from fractions import Fraction

# Funció per sumar fraccions
def sum_fracs(frac1, frac2):
    return frac1 + frac2

# Funció per restar fraccions
def sub_fracs(frac1, frac2):
    return frac1 - frac2

# Funció per multiplicar fraccions
def mul_fracs(frac1, frac2):
    return frac1 * frac2

# Funció per dividir fraccions
def div_fracs(frac1, frac2):
    return frac1 / frac2

# Funció per simplificar fraccions
def simplify(frac):
    return frac.numerator / frac.denominator

# Funció principal
def main():
    # Llegir fraccions de l'usuari
    num1 = int(input("Introdueix el numerador de la primera fracció: "))
    den1 = int(input("Introdueix el denominador de la primera fracció: "))
    num2 = int(input("Introdueix el numerador de la segona fracció: "))
    den2 = int(input("Introdueix el denominador de la segona fracció: "))

    # Crear objectes de fraccions
    frac1 = Fraction(num1, den1)
    frac2 = Fraction(num2, den2)

    # Mostrar les fraccions a l'usuari
    print("Fracció 1:", frac1)
    print("Fracció 2:", frac2)

    # Realitzar operacions amb les fraccions
    suma = sum_fracs(frac1, frac2)
    resta = sub_fracs(frac1, frac2)
    producte = mul_fracs(frac1, frac2)
    divisió = div_fracs(frac1, frac2)
    simplificada = simplify(frac1)

    # Mostrar el resultat de les operacions
    print("Suma:", suma)
    print("Resta:", resta)
    print("Producte:", producte)
    print("Divisió:", divisió)
    print("Fracció 1 simplificada:", simplificada)

if __name__ == '__main__':
    main()

# Aquest programa utilitza la llibreria estàndard de Python "fractions" per crear objectes de fraccions i realitzar operacions amb ells. Les funcions "sum_fracs", "sub_fracs", "mul_fracs" i "div_fracs" sumen, resten, multipliquen i divideixen les fraccions, respectivament. La funció "simplify" simplifica la fracció.

# A la funció principal "main", l'usuari introdueix les fraccions que vol operar. El programa mostra les fraccions introduïdes i els resultats de les operacions realitzades. Per simplificar la fracció 1, s'utilitza la funció "simplify".

# Aquest és només un exemple senzill de programa per fer operacions amb fraccions. Es pot ampliar afegint altres operacions o funcions per a la manipulació de fraccions.
