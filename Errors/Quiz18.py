def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
    else:
        n_square = n ** 2
        print(n_square)

power_of_two()