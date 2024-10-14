name = input("Enter your name: ")
name_file = open('name.txt', 'w')
name_file.write(name)
name_file.close()

name_file = open('name.txt', 'r')
name_in_file = name_file.read()
print("Your name is", name_in_file)
name_file.close()

file_name = "numbers.txt"

with open(file_name, 'r') as number_file:
    number_1 = int(number_file.readline())
    number_2 = int(number_file.readline())
    result = number_1 + number_2
    print("The result is:", result)

number_file.close()

file = open(file_name, 'r')
total = 0
with open(file_name, 'r') as file:  # Use 'with' to open the file again

    for line in file:
        number = int(line)
        total = total + number
print("The total is:", total)
file.close()
