def interact():
    while True:  # keep looping until user reach break statement
        try:
            user_input = int(input('Please input an integer:'))     # turn the user input into an integer
        #print out the message '{user_input} is {even/odd}.'
            if user_input%2==0:
                print(f"{user_input} is even.")
            elif user_input%2!=0:
                print(f"{user_input} is odd.")
        
        except ValueError:
            print("Please input integers only.")
            
        finally:
            user_input = input('Do you want to play again? (y/N):')
            if user_input != 'y':   # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit