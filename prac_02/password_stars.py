# Setting minimum length for the password
Minimum_length = 10


# Function to check password length
def get_password():
    while True:
        password = input("Enter Your Password: ")
        if len(password) >= Minimum_length:
            return password
        else:
            print(f"Password must be at least {Minimum_length} characters long.")


# Main part of the program
password = get_password()

# Print the asterisks, one for each character in the password
print('*' * len(password))
