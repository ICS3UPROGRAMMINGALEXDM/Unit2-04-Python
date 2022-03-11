#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/11/2022
# Description: Calculates the production cost of a pizza in accordance with the diameter.


# Import files
import constants


def calculate():
    while True:
        dia = input("What is the diameter of the pizza in inches? \n")
        try:
            diameter = float(dia)

            break
        except ValueError:
            print("Invalid input. Please try again.")

    subtotal = (
        diameter * constants.INGREDIENTS + constants.LABOUR_COST + constants.RENT_COST
    )

    tax = subtotal * constants.HST

    total = subtotal + tax

    print("The pizza will cost ${:.2f} to make.".format(total))


def main():
    calculate()


if __name__ == "__main__":
    main()
