import smtplib# #login to server
my_email = "sidra.essani66@gmail.com"
password = "qqju nnql ryhz cjcf"
#create object for smtp
connection = smtplib.SMTP("smtp.gmail.com")

#secure smtp connection
connection.starttls()
#login
connection.login(user=my_email, password=password)
# Send an email
connection.sendmail(
    from_addr=my_email,
        to_addrs="sidraabdulsamad270@gmail.com",
        msg="Subject: Hello \n\n This is the body of my email."

    )

# Quit the SMTP session
connection.close()
#https://medium.com/@manavshrivastava/how-to-send-emails-using-python-c89b802e0b05
