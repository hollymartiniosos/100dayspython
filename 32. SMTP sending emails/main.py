# import smtplib

# my_email = "dummyemail@gmail.com"
# password = "5234tgwegbdf%$T"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appafdvsd@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my mail."
#     )

import datetime as dt
from random import choice
# import smtplib
# my_email = "dummyemail@gmail.com"
# password = "5234tgwegbdf%$T"
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6:
    with open("quotes.txt") as data_file:
        #babka tu ma: all_quotes = data_file.readlines()
        data = data_file.read()
        quote = choice(data.split("\n"))
        print(quote)
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=password)
        #     connection.sendmail(
        #         from_addr=my_email,
        #         to_addrs="appafdvsd@yahoo.com",
        #         msg=f'Subject:Motivational message\n\n{quote}'
        #     )