import smtplib

email = 'wenjunsang@gmail.com' # Your email
password = '871015swj' # Your email account password
send_to_email = '18601670329@163.com' # Who you are sending the message to
message = 'This is my message2' # The message in the email

server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
server.starttls() # Use TLS
server.login(email, password) # Login to the email server
server.sendmail(email, send_to_email , message) # Send the email
server.quit() # Logout of the email server
print('email sent')

