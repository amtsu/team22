#!/usr/local/bin/python
# coding: utf-8
from basemail import base_mail
class mail_to:
    #инициализация
    def __init__(self, receiver):
        self.__mailer = base_mail(u'sivanov@101katok.ru',u'localhost')
        self.__you = receiver
        return
    #вызов
    def __call__(self,topic, message):
        return self._sendmail_(topic, message)
    #технический вывод
    def __repr__(self):
        return self.__str__()
    #вывод в строку
    def __str__(self):
        return unicode("receiver: "+self.__you + ";  server info: " + unicode(self.__mailer))
    #послать письмо
    def _sendmail_(self, topic, message):
        return self.__mailer(self.__you, topic, message)
    pass