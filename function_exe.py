
def check_prime_odd_number(number):
    if number < 2 or number % 2 == 0: # for checking odd numb condition
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):  for checking prime numb condition
        if number % i == 0:
            return False

    return True

user_input = int(input('Enter a number : '))

if check_prime_odd_number(user_input):
    print(f'{user_input} is a prime and odd number')
else:
    print(f'{user_input} is not a prime and odd number')

def even_numb_check(number):
    if number % 2 == 0:
        return True

user_input = int(input('Enter a number : '))

if even_numb_check(user_input):
    print(f'{user_input} is even number')
else:
    print(f'{user_input} is not a even number')


def print_pattern():
    n = int(input("Enter the amount of row: "))
    if n % 2 == 0:
        for i in range(n, 0, -1):
            print('* ' * i)
    else:
        for i in range(1, n + 1):
            print('* ' * i)

print_pattern()











