
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







