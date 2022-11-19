student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key,value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a data frame:
for (key,value) in student_data_frame.items():
      print(value)

#Looping through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print(index)   
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)
