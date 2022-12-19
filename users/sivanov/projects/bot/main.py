#!/usr/local/bin/python
# coding: utf-8
'''
ДОБАВИТЬ КОММЕНТАРИЙ
это модуль с тестом бота для телеги
мануал взял вот тут:
https://otus.ru/journal/bot-v-telegram-na-pitone-ot-a-do-ya/
'''
import telebot
from telebot import types
bot = telebot.TeleBot("5949080313:AAHE8ikdvHc5q30R1EeFa2se-j9F5dqokoo")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    with open('bot.log','a',encoding='utf-8') as fout:
        print(f'FROM {message.from_user.id} comes text: {message.text}',file=fout)
    print(f'message from {message.from_user.id} comes.')
    
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет пидор.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

#Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    pass

bot.polling(none_stop=True, interval=0)

def main():
    return None
if __name__ == "__main__":
    main()
    