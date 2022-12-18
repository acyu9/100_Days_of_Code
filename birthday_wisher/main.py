from datetime import datetime
import pandas
from random import randint
import smtplib

now = datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
data = data.to_dict(orient="records")

# Check if today matches a birthday in the birthdays.csv and saves that person's info in a new list of dict
birthday = [dictionary for dictionary in data if dictionary["month"] == month and dictionary["day"] == day]

my_email = "example@gmail.com"
password = "abcd1234()"

# If today is someone's birthday
if birthday != []:
    # Randomly choose one of the 3 letters
    number = randint(1, 3)
    with open(f"letter_templates\letter_{number}.txt") as file:
        letter = file.read()
        # Replace with person's name. Only 1 dict in the list so index 0
        new_letter = letter.replace("[NAME]", birthday[0]["name"])
        # Send the email with the updated letter
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday[0]["email"],\
                msg=f"Subject:Happy Birthday\n\n{new_letter}")
