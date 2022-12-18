##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
from random import randint
import datetime as dt

#MY_EMAIL= "dafabva@wp.pl"
#MY_PASSWORD = "dgvgvdanln23413"
now = dt.datetime.now()
today = (now.month, now.day)


data= pd.read_csv("birthday/birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person_name = birthdays_dict[today]
    file_path= f'birthday/letter_templates/letter_{randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        correct_content = contents.replace("[NAME]", birthday_person_name["name"])
        
    print(correct_content)  

    #wysyłanie email
    #with smtplib.SMTP("smtp.wp.pl") as connection:
    #    connection.starttls()
    #    connection.login(MY_EMAIL, MY_PASSWORD)
    #    connection.sendemail(
    #           from_addr=MY_EMAIL,
    #           to_addr=  birtday_person["email"],
    #           msg=f"Subject:Happy Birthday!\n\n{correct_content}  
    # )