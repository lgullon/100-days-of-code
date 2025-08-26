#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"


with open("Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()

with open("Input/Letters/starting_letter.txt") as starting_letter:
    base = starting_letter.read()
    for name in names:
        with open(f"Output/ReadyToSend/letter_for_{name.strip()}.docx", "w") as letter:
                new_letter = base.replace(PLACEHOLDER, name.strip())
                letter.write(new_letter)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
