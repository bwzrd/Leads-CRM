
import pandas as pd

name1 = input("Enter a name of lead:")
name2 = input("Job Title:")
name3 = input("Enter Company Name:")
name4 = input("Phone Number:")

import re

while True:
    name5 = input("Email address: ")
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, name5):
        break
    print("Invalid email address. Please try again.")
while True:
    name6 = input("Website: ")
    pattern = r"^[w,w,w]+.[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, name6):
        break
    print("Invalid format. Please try again.")

name7 = input("Lead Source:")
name8 = input("Lead Stage:")
name9 = input("Today's Date:")
name10 = input("Follow-up Date:")
name11 = input("Appointment Date:")
name12 = input("Important Notes:")
name13 = input("Assigned To:")
a =  float(input("Contract Amount ($): "))
b =  float(input("Commission % (decimal) :"))
c =  float(input("Referral Commission % (decimal): "))

my_tuple = ('a', 'b', 'c')
print("Gross Commission: $",a*b)
print("Referral Commission: $",a*c)
str = float((a*b) - (a*c))
print("Net Estimated Earnings:")
print("$",[(a*b) - (a*c)])
d = (a*b)
e = (a*c)
f = (([(a*b) - (a*c)]))

# Importing Panda module as jtp  
import pandas as jtp

GivenData = {'Lead Name':[name1],
             'Job Title':[name2], 
             'Company Name':[name3,],
             'Phone Number':[name4], 
             'Email':[name5],
             'Website':[name6], 
             'Lead Source':[name7],
             'Lead Stage':[name8],
             'Todays Date':[name9],
             'Followup Date':[name10],
             'Appointment Date':[name11],
             'Important Notes':[name12],
             'Assigned to':[name13],
             'Contract Amount $':[a],
             'Commission %':[b],
             'Referral Commission %':[c],
             'Commission $':[d],
             'Referral Commission $':[e],
             'Net Estimated Earnings $:':[f]}

# Creating DataFrame with DataFrame() function   
dataFrame = jtp.DataFrame(GivenData)

# Print the dataframe as result   
print(dataFrame)

# Save the DataFrame to a CSV file
dataFrame.to_csv('Lead File.csv', index=False)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Set up the email details
sender = 'brendanwise@hotmail.com'
receiver = 'brendanbwise@gmail.com'
subject = name1,':', + name3,'-' + name2,': Lead File CSV'

# Create the email message
msg = MIMEMultipart()
msg['Brendan Wise'] = sender
msg['Team Lead'] = receiver
msg[''] = subject

# Open the CSV file in binary mode
with open('Lead File.csv', 'rb') as file:
    # Add the CSV file as an attachment to the email
    payload = MIMEBase('application', 'octate-stream', Name='Lead File.csv')
    payload.set_payload((file).read())
    encoders.encode_base64(payload)

    # Add header with CSV file name
    payload.add_header('Content-Decomposition', 'attachment', filename='Lead File.csv')
    msg.attach(payload)

# Connect to the email server and send the email
mail_server = smtplib.SMTP('smtp.COMPANY_NAME.com')
mail_server.sendmail(sender, receiver, msg.as_string())
mail_server.quit()






