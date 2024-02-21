#!/usr/local/bin/python
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
class base_mail:
    #предварительная инициализация
    def __init__(self,sender,SMTPServer):
        self.__server = SMTPServer
        self.__me = sender
        return
    #полная инициализация
    def __call__(self,receiver, topic, message):
        return self._sendmail_(receiver, topic, message)
    #вывести на чистовую печать 
    def __str__(self):
        return unicode("server: "+self.__server+", sender: "+self.__me+";")
    #вывести на отладочную печать
    def __repr__(self):
        return self.__str__()
    #работа
    def _sendmail_(self, receiver, topic, message):
        result = 0
        you = receiver# кому отправить
        msg = MIMEText(message)# что отправить   
        msg['Subject'] = topic
        msg['From'] = self.__me
        msg['To'] = you
        s = smtplib.SMTP(self.__server)
        s.sendmail(self.__me, [you], msg.as_string())
        s.quit()
        return result
    pass