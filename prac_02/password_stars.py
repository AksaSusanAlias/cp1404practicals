def main():
    # Setting minimum length for the password_input
    Minimum_length = 10

    # Function to check password_input length
    def get_password():
        while True:
            password_input = input("Enter Your Password: ")
            if len(password_input) >= Minimum_length:
                return password_input
            else:
                print(f"Password must be at least {Minimum_length} characters long.")

    # Main part of the program
    password= get_password()

    # Print the asterisks, one for each character in the password_input
    print('*' * len(password))


main()
