'''import smtplib as s 
obj=s.SMTP("74.125.200.108",587)    
obj.ehlo()
obj.starttls()
obj.login('mohammedabdulakifahmed@gamil.com','akif')
subject="testing mail"
body="hii how are uuuuu"
message1="Subject:{}\n\n{}".format(subject,body)
list=['abdulakif44570@gmail.com','meherunnisa943@gmail.com']
obj.sendmail('a01121267@gmail.com',list,message1)
print("hogaya")
obj.quit()'''

import smtplib as s

# Create an SMTP object and connect to the server
obj = s.SMTP("smtp.gmail.com", 587)
obj.ehlo()  # Extended Hello to the server
obj.starttls()  # Start TLS encryption

# Login credentials
sender_email = 'mohammedabdulakifahmed@gmail.com'
password = 'akif'

try:
    obj.login(sender_email, password)
    
    # Email details
    subject = "Testing Mail"
    body = "Hi, how are you?"
    message = f"Subject: {subject}\n\n{body}"
    
    # Recipients
    recipients = ['abdulakif44570@gmail.com', 'meherunnisa943@gmail.com']

    # Send the email
    obj.sendmail(sender_email, recipients, message)
    print("Email sent successfully!")

except s.SMTPAuthenticationError:
    print("Failed to login. Check your email or password.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    obj.quit()  # Close the connection

    
