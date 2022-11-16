import smtplib

class Mailer:
    def __init__(self, login, password, recipient_list, domen, port):
        self.__recipient_list = recipient_list
        self.__login = login

        self.__smt = smtplib.SMTP(domen, port)
        self.__smt.starttls()
        self.__smt.login(login, password)

    def send_message(self, message):
        self.__smt.sendmail(self.__login, self.__recipient_list, message)

    def quit(self):
        self.__smt.quit()
