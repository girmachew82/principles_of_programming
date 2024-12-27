while True:
    try:
        x = int(input('Enter the value of x '))
    except ValueError as e:
        print('Operation error. That was not valid number. Try again ... ')