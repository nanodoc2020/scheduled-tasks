# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import datetime as dt
import pandas as pd
import random as rnd
import smtplib as smtp
import os


# import os and use it to get the Github repository secrets
sender = os.environ.get("MY_EMAIL")
app_password = os.environ.get("MY_PASSWORD")

bday_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
sender = 'larsene300@gmail.com'
app_password = "jtxh pmhp vhet ding"

now = dt.datetime.now()
month = now.month
day = now.day
year = now.year

birthdays_df = pd.read_csv('birthdays.csv')

for row in birthdays_df.iterrows():
    bd_month = row[1]["month"]
    bday = row[1]["day"]
    if month == bd_month and day == bday:
        name = row[1]["name"]
        email = row[1]["email"]
        letter_choice = rnd.choice(bday_letters)
        letter_path = "letter_templates/" + letter_choice
        with open(letter_path, 'r' ) as f:
            data = f.read()
            data = data.replace('[NAME]', name)
            print(data)
        try:
            with smtp.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(sender, app_password)
                connection.sendmail(sender, email, msg="Subject:Happy Birthday!\n\n" + data)
        except smtp.SMTPException as error:
            print(f'Something went wrong: {error}')
        else:
            print("Birthday emails sent!")
        finally:
            connection.close()
