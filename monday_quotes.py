import datetime as dt
import pandas
import random
import smtplib

my_email = "Your Email Address"
password = "Your Password - Check Readme"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open('quotes.txt') as quotes:
        quotes = quotes.readlines()
        to_send = random.choice(quotes)

    print(to_send)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  #makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="email address to send to" ,
            msg=f"Subject:Quote\n\n{to_send}")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="email address to send to",
            msg=f"Subject:Quote\n\n{to_send}")