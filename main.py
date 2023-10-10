##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import random
import pandas
import datetime as dt

current_dt = dt.datetime.now()
date_today = current_dt.day
month_today = current_dt.month

df = pandas.read_csv("birthdays.csv")
main_list = df.to_dict(orient="records")

temporary_list = []
birthdays_today = []

for item in main_list:
    for element in item.values():
        if item["month"] == month_today and item["day"] == date_today:
            temporary_list.append(item)

for item in temporary_list:
    if item not in birthdays_today:
        birthdays_today.append(item)

messages = []
with open("letter_templates/letter_1.txt", "r") as file:
    stringed_msg = file.readlines()
    messages.append("".join(stringed_msg))
with open("letter_templates/letter_2.txt", "r") as file:
    stringed_msg2 = file.readlines()
    messages.append("".join(stringed_msg2))
with open("letter_templates/letter_3.txt", "r") as file:
    stringed_msg3 = file.readlines()
    messages.append("".join(stringed_msg3))


my_email = "feedback.hospicare@gmail.com"
password = "cwmtflcebpiuuvbx"

for item in birthdays_today:
    receiver_name = item["name"]
    receiver_email = item["email"]
    message = random.choice(messages)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email, msg=f"Subject:Happy Birthday\n\nDear {receiver_name},\n{message}")





