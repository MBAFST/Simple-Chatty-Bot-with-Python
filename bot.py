def welcome():
    print("""Hello! My name is Aid.
I was created in 2020.""")


def get_name():
    print("Please, remind me your name.")
    name = input()
    return name


def get_age():
    print("""Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")

    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())

    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    return age


def counting():
    print("Now I will prove to you that I can count to any number you want.")

    n = int(input())
    counter = 0

    while counter <= n:
        print(f"{counter}!")
        counter += 1

    print("Completed, have a nice day!")


def test():
    print("""Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")

    answer = input()

    while answer != "2":
        print("Please, try again.")
        answer = input()

    print("""Completed, have a nice day!
Congratulations, have a nice day!""")


welcome()
print(f"What a great name you have, {get_name()}!")
print(f"Your age is {get_age()}; that's a good time to start programming!")
counting()
test()
