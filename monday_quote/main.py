import smtplib
from random import choice
import datetime as dt

my_email = "example@gmail.com"
# Can generate app password so it's different from email app - required for Google email now
password = "abcd1234()"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = choice(quotes)
    print(quote)

    #Add port number after .com to connect successfully
    with smtplib.SMTP("smtp.gmail.com") as connection:
    #Enable transport layer security to make connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        # Having subject means it's not spam. 2 \n makes it the body of the email
        connection.sendmail(from_addr=my_email, to_addrs="sample@yahoo.com",\
           msg=f"Subject:Quote\n\n{quote}")


#date_of_birth = dt.datetime(year=1995, month=12, day=15)