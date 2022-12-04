import pandas
import time
# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv('C:/Users/Martyna/projects/100dayspython/26. Comprehension and NATO alphabet/NATO-alphabet-start/gnato.csv')
# print(data)

dict_frame = pandas.DataFrame(data)
# {str(key):str(value) for (key, value) in data.items()}

dict_frame = {row.letter:row.code for (index, row) in dict_frame.iterrows()} 


# dict_frame2 = {letter:code for letter, code in zip(data['letter'],data['code'])}


# 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetics():
    word = input("Enter word: ").upper()

    try:
        word_list = [dict_frame[letter] for letter in word]
    
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics() 
    else:
        print(word_list)

generate_phonetics()        