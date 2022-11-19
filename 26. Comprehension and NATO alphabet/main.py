# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)


# doubbled = [n*2 for n in range(1,5)]
# print(doubbled)

# names = ['Alex', 'Beth' , 'Caroline' , 'Dave', 'Eleanor', 'Freddie', 'Martyna']

# short_names = [name for name in names if len(name) <=4 ]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) > 5 ] 
# print(long_names)


# 26,1 from replit new list contains squered numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squered_numbers = [n**2 for n in numbers]
# print(squered_numbers)

#26,2 from replit result contains only even numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n%2 == 0]
# print(result)


#Dictionary Comprehension
# import random
# names = ['Alex', 'Beth' , 'Caroline' , 'Dave', 'Eleanor', 'Freddie', 'Martyna']

# students_scores = {student:random.randint(0,100)  for student in names}
# print(students_scores)

# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

