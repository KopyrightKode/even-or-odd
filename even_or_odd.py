#written by KopyrightKid
def divisible(num1, num2):
    return num1 % num2 == 0

def user_even():
    number = input("Enter a number: ")
    int_number = int(number)
    if divisible(int_number, 2):
        print("It's even!")
    else:
        print("It's odd")
user_even()
