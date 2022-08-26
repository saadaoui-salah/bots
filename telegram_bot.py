import telebot
from telebot import types
import random

bot = telebot.TeleBot('5493743085:AAEBwYbrlb1uhpIw4sdkBBfDaF0SV-FNAMA')

@bot.message_handler(commands=['start'])
def send_hello(message):
    reply = """
    HEY !!
    Welcome to my SalahForBot
    Here where you can ask for creating your
    own bot that help you for automating your 
    telegrame tasks
    If you want to play game type /play
    If you want to ask for bot type /bot
    About me /info
    """
    bot.reply_to(message, reply)

@bot.message_handler(commands=['play'])
def play_game(message):
    msg = """
        Hey again !
        we will play Rock, Paper, Seasor game
        pls chose one of the choices 
    """
    rock_button = types.InlineKeyboardButton('Rock', callback_data='Rock')
    paper_button = types.InlineKeyboardButton('Paper', callback_data='Paper')
    seasor_button = types.InlineKeyboardButton('Seasor', callback_data='Saesor')

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(rock_button)
    keyboard.add(paper_button)
    keyboard.add(seasor_button)

    bot.send_message(message.chat.id, text=msg, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def get_resposne(call):
    choices = ['Rock','Paper','Seasor']
    bot_choice = choices[random.randint(0,2)]

    if call.data == bot_choice:
        bot.send_message(call.message.chat.id, f'Bot choice is {bot_choice} \nNull Result ')

    if (call.data == 'Rock' and bot_choice == 'Paper') or  \
       (call.data == 'Paper' and bot_choice == 'Seasor' ) or \
       (call.data == 'Seasor' and bot_choice == 'Rock'):

        bot.send_message(call.message.chat.id, f'Bot choice is {bot_choice} \nYou Lose ')

    if (bot_choice == 'Rock' and call.data == 'Paper') or  \
       (bot_choice == 'Paper' and call.data == 'Seasor' ) or \
       (bot_choice == 'Seasor' and call.data == 'Rock'):
       
        bot.send_message(call.message.chat.id, f'Bot choice is: {bot_choice}\nYou Win')

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, """
    Full Name    : Saadaoui Salah
    Email        : salahsaadaoui8@gmail.com
    Phone Number : +213553979414
    """)

bot.polling()