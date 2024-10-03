# Scraping tools
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date

# Email Tools
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Fetch data from the website
url = "https://www.cursbnr.ro/"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", class_="table table-striped table-lg").tbody.find_all("tr")

# Process the data
lista_monede = []
for i in table:
    moneda = i.find_all("td")[0].text.strip()
    valoare = i.find_all("td")[2].text.strip()
    today = date.today()
    dictionar_monede = {
        "Moneda": moneda,
        f"Valoare la data: {today}": valoare,
    }
    lista_monede.append(dictionar_monede)

valori_interes = [
    lista_monede[0],  # EUR
    lista_monede[1],  # USD
    lista_monede[3],  # GBP
    lista_monede[17]  # GOLD
]

# Create a DataFrame with today's data
df_new = pd.DataFrame(valori_interes)

# Read the existing Excel file
filename = "Pret_Monede.xlsx"
try:
    df_existing = pd.read_excel(filename)
except FileNotFoundError:
    # If the file doesn't exist, create a new DataFrame with only the new data
    df_existing = df_new[['Moneda']]

# Merge the existing data with the new data
df_combined = pd.merge(df_existing, df_new, on="Moneda", how="outer")

# Save the updated DataFrame to Excel
df_combined.to_excel(filename, index=False)

# Email setup
with open("Password.txt", "r") as pws:
    password = pws.read().strip()  # Strip any extraneous newline characters

email_address = 'casianpantilimon98@gmail.com'
recipient_addresses = ['casian.pantilimon98@gmail.com', "adina.ilisie@stefanini.com", "miruna.lujanski@stefanini.com",]
subject = f"Curs BNR: {date.today()}"
body = """Hello,
Below you will find the today's stats from: https://www.cursbnr.ro/

Thank you,
Casian"""

# Create the email
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = ', '.join(recipient_addresses)
msg['Subject'] = subject

# Attach the body
msg.attach(MIMEText(body, 'plain'))

# Attach the updated Excel file
try:
    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={filename}',
        )
        msg.attach(part)
except FileNotFoundError:
    print(f"File {filename} not found.")
    exit()

# Send the email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(email_address, password)
        server.sendmail(email_address, recipient_addresses, msg.as_string())
        print("Email sent with 0 errors.")
except (smtplib.SMTPException, smtplib.SMTPResponseException, TimeoutError, PermissionError) as err:
    print(f"An error occurred: {err}")


