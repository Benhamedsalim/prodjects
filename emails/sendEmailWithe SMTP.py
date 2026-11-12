import smtplib

senderEmail = "......"
rec_Email = "........"
password = input("Enter your password: ")
message = input("Enter your message: ")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, password)
print("Login success")
server.sendmail(senderEmail, rec_Email, message)
print(f"Email sent success to {rec_Email}")
server.quit()