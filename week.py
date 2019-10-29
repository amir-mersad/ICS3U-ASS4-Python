#!/usr/bin/env python3

# Created by Amir Mersad
# Created on October 2019
# This program gives you the number of the day in the week


def main():
    number_int = input("Please enter the number of the day: ")
    try:
        number = int(number_int)
        if number == 1:
            print("Monday")
        elif number == 2:
            print("Tuesday")
        elif number == 3:
            print("Wednesday")
        elif number == 4:
            print("Thursday")
        elif number == 5:
            print("Friday")
        elif number == 6:
            print("Saturday")
        elif number == 7:
            print("Sunday")
        else:
            print("Please enter a number between 1 and 7!")
    except(Exception):
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
