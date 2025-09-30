import pandas as pd
import yagmail
from datetime import datetime

sender_email = "your email"
sender_password = "Your 16 digit app password(without spaces)"  

df = pd.read_csv("yourcsvfile.csv") 

yag = yagmail.SMTP(user=sender_email, password=sender_password)

today = datetime.today().strftime("%d-%m")

for index, row in df.iterrows():
    bday = datetime.strptime(row['Birthday'], "%d-%m-%Y").strftime("%d-%m")
    if bday == today:
        name = row['Name']
        recipient = row['gmail'] 
        subject = f"Happy Birthday {name}! 🎉"
        body = f"Hey {name},\n\nWishing you an amazing birthday full of joy and fun! 🥳\n\nBest wishes,\nGunaa"
        
        yag.send(to=recipient, subject=subject, contents=body)
        print(f"Sent birthday email to {name} ({recipient})")

print("All done!")
