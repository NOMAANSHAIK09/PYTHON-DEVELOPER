import smtplib
import filetype
from email.message import EmailMessage

password = "odqy oybd kqcr oima"
# sender = "engineeringmeth09@gmail.com"
sender = "nomaanshaik0915@gmail.com"
receiver ="nomaanshaik0915@gmail.com"

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "A new customer"
    email_message["From"] = sender
    email_message["To"] = receiver
    email_message.set_content("Hey, new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
        kind = filetype.guess(content)
        subtype = kind.extension if kind else "jpeg"
        # if kind:
        #     subtype = kind.extension
        # else:
        #     subtype = "octet-stream"  # fallback for unknown type

    email_message.add_attachment(content, maintype="image", subtype=subtype,filename="motion.png")


    with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
        gmail.ehlo()
        gmail.starttls()
        gmail.login(sender, password)
        gmail.send_message(email_message)
    # gmail = smtplib.SMTP("smtp.gmail.com", 587)  # ✅ fixed typo (was smpt)
    # gmail.ehlo()
    # gmail.starttls()
    # gmail.login(sender, password)
    # gmail.send_message(email_message)
    # gmail.quit()
    print("✅ Email sent successfully!")

if __name__ == "__main__":
    send_email(image_path="images/7.png")