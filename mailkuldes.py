import smtplib

gmail_user = 'xxxxxx@gmail.com'
gmail_password = 'xxxx xxxx xxxx xxxx' #kulon generaltatni kell

sent_from = gmail_user
to = 'xxxxxx@yahoo.com'
subject = 'Try'
body = 'Message_you_need_to_send'

try:
    #SMTP
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

   #TLS
    smtp.starttls()

    #azonositas
    smtp.login(gmail_user, gmail_password)

    #uzenet szovege
    message = "Message_you_need_to_send"

    #kuldes honnan hova mit
    smtp.sendmail(sent_from, to, message)

    #visszajelzes
    smtp.quit()
    print ("Email sent successfully!")

except Exception as ex:
    print("Something went wrong....",ex)