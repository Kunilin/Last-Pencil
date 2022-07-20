moves = ['1', '2', '3']
x = input('How many pencils would you like to use: ')
while x.isdigit() == False or int(x) <= 0:
    x = input('The number of pencils should be numeric and positive: ')
x = int(x)
y = str(input('Who will be the first (John, Jack): '))
while y != 'John' and y != 'Jack':
    y = str(input('Input is incorrect and re-query the input with "Choose between "John" and "Jack": '))
while x > 0:
    print(int(x) * '|')
    z = input(f"{y}'s turn: ")
    while z.isdigit() == False or int(z) > x or z not in moves:
        if z not in moves:
            print("Possible values: '1', '2', '3': ")
        elif int(z) > x:
            print('Too many pencils were taken: ')
        elif z.isdigit() == False:
            print("The number of pencils should be numeric: ")
        z = input()
    x -= int(z)
    if y == 'John':
        y = 'Jack'
    else:
        y = 'John'
print(f'{y} won!')
