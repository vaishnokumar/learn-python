def main():
    x = int(input('enter x? '))
    if is_even(x):
        print('even')
    else:
        print('odd')

def is_even(n):
    return n % 2 == 0

main()