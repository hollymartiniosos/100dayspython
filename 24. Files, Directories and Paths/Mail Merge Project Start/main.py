#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

'''file = open("../../../Desktop/my_file.txt")'''

with open('./Input/Letters/starting_letter.txt') as file:
    template = file.read()
print(template)

with open("./Input/Names/invited_names.txt") as file:
    names = file.read()
print(names)


names_list = names.split("\n")
print(names_list)

for name in names_list:
    a = template.replace('[name]', name)
    print(a)
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', "w") as file:
        file.write(a)