import config

import telebot
import os
import random
#import requests
#from bot_logic import gen_pass, gen_emodji, flip_coin, get_weather

class Student:
    name = "John"
    family = "Doe"
    age = 23
    gender = "male"

    def __init__(self, name, family, age, gender):
        self.name = name
        self.family = family
        self.age = age
        self.gender = gender

    def go_to_study(self):
        print("Study")

    def do_sports(self):
        print("Make sport")

    def info(self):
        return "name: " + str(self.name) + "\n family: " + str(self.family) + "\n age: " + str(self.age) + "\n gender: " + str(self.gender)

TOKEN = config.token

bot = telebot.TeleBot(TOKEN)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Это smarchenko744_bot!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['info', '?'])
def info(message):
    info = "Доступные команды:\n" \
    "/hello\n" \
    "/bye\n" \
    "/new_student\n" \
    "/info\n"
    bot.reply_to(message, info)

@bot.message_handler(commands=['new_student'])
def new_student(message):

    names = ['John', 'Pol', 'Duck', 'Rich']
    families = ['Smith','Taylor', 'Brown', 'Wilson']

    name = random.choice(names)
    family = random.choice(families)
    age = random.randint(20, 40)

    st_1 = Student(name, family, age, 'male') 
    bot.reply_to(message, st_1.info())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
#bot.infinity_polling()
