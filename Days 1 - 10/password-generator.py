import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# *** this was my first attempt after reading the instructions

# char_list = list()
# for letter in range(0, nr_letters):
#     letter_index = random.randint(0, len(letters) - 1)
#     char_list.append(letters[letter_index])
#
# for symbol in range(0, nr_symbols):
#     symbol_index = random.randint(0, len(symbols) - 1)
#     char_list.append(symbols[symbol_index])
#
# for number in range(0, nr_numbers):
#     number_index = random.randint(0, len(numbers) - 1)
#     char_list.append(numbers[number_index])
#
# password = "".join(char_list)
# print(password)


# *** this was my edited version after reading the hint about the random.choice() thing
# char_list = list()
# for letter in range(0, nr_letters):
#     char_list.append(random.choice(letters))
# for symbol in range(0, nr_symbols):
#     char_list.append(random.choice(symbols))
# for number in range(0, nr_numbers):
#     char_list.append(random.choice(numbers))
# password = "".join(char_list)
# print(password)


# *** this is my attempt at the harder part
# char_list = list()
# char_list.append("placeholder")
#
# for letter in range(0, nr_letters):
#     rand_index = random.randint(0, len(char_list) - 1)
#     char_list.insert(rand_index, random.choice(letters))
#
# for symbol in range(0, nr_symbols):
#     rand_index = random.randint(0, len(char_list) - 1)
#     char_list.insert(rand_index, random.choice(symbols))
#
# for number in range(0, nr_numbers):
#     rand_index = random.randint(0, len(char_list) - 1)
#     char_list.insert(rand_index, random.choice(numbers))
#
# char_list.remove("placeholder")
# password = "".join(char_list)
# print(password)



# *** this is after reading the shuffle hint fml I LIKE MINE BETTER i felt smart :(
char_list = list()
for letter in range(0, nr_letters):
    char_list.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    char_list.append(random.choice(symbols))
for number in range(0, nr_numbers):
    char_list.append(random.choice(numbers))
random.shuffle(char_list)
password = "".join(char_list)
print(password)
