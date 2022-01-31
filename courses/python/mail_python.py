# python3 -m smtpd -n -c DebuggingServer localhost:1025

import smtplib
from email.mime.text import MIMEText

# Msg setup
msg = MIMEText('Sample Nachomachine email')
msg['Subject'] = 'An Email Alert'
msg['From'] = 'nachomachine@gmail.com'
msg['To'] = 'rmfranciacastillo@gmail.com'

# Send Email
s = smtplib.SMTP('localhost', "1025")
s.send_message(msg)
s.quit()
