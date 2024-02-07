indian = ['samosa', 'dal', 'naan']
chinese = ['egg role', 'chowmein', 'fried rice']
italian = ['pizza','pasta', 'risotto']

dish = input('enter a dish name: ')

if dish in indian:
    print('it is a indian dish')
elif dish in chinese:
    print('it is a chinese dish')
elif dish in italian:
    print('it is a italian dish')
else:
    print("sorry it's not in the menu")

# message = 'number is even ' if n % 2 == 0 else 'number is odd'
# print(message)


