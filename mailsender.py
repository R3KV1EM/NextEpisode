import smtplib
from email.message import EmailMessage



email = EmailMessage()
email["from"] = "Archy Khukhka"
email['to'] = "smok3rarchy@gmail.com"
email['subject'] = "YOU ARE BADASS"

email.set_content("PYTHON MASTER IS HERE")
with smtplib.SMTP(host="smtp.mail.ru", port=465) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("shregory@inbox.ru", 'LALonely1')
    smtp.send_message(email)
    print("all good bozo")