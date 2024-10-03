import smtplib

with open("Password.txt", "r") as pws:
    password = pws.read()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email_address = 'casianpantilimon98@gmail.com'
        email_password = password
        email.login(email_address, email_password)
        email.sendmail(from_addr=email_address, to_addrs="casian.pantilimon98@gmail.com",
                       msg="subject:Test Email \n\n This was sent from my IDE, hehe.\n "
                           "Also this is sent from my IDE but, just to see if the second line gets implemented.\n\n"
                           "Thank you,\nCasian ")
        print("Email sent with 0 errors.")
except (smtplib.SMTPException, smtplib.SMTPResponseException, TimeoutError, PermissionError) as err:
    print(f"And error occured: {err}")
