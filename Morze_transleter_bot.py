#Ass We Can          # Талисман кода



# Импорт библиотек
import telebot
from telebot import types


bot = telebot.TeleBot('5600142537:AAHQmOyvP7wBlOOtLwqcHfcLApCHv-cBBN4') 
answer = ''
keyboard = types.InlineKeyboardMarkup()

def morze_in_text(Inp=str):
    Tran_For_Morze = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h",
                      "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p",
                      "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x",
                      "-.---": "y", "--..": "z", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5",
                      "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0", "..--..": "?",
                      "..--.-": "_", ".-..-.": '"', ".-.-.-": ".", ".--.-.": "@", ".----.": "`", "-....-": "-",
                      "-.-.-.": ";", "-.-.--": "!", "-...-": "=", "-..-.": "/", ".-.-.": "+", "-.--..": "(",
                      "-.--.-": ")", "--..--": ",", "---...": ":", "": ""}


    Out = ""
    b = ""
    b_p = False
    
    for ch in Inp:
        if ch in " ":
            if b_p == True:
                Out += " "
                b_p = False
                pass
            b_p = True
            if b in Tran_For_Morze:
                Out += Tran_For_Morze[b]
                b = ""
        else:
            b += ch
            b_p = False
    
    Out += Tran_For_Morze[b]
    
    return Out

def text_in_morze(Inp=str):
    Tran_In_Morze = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                     "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                     "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                     "y": "-.---", "z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                     "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", "?": "..--..",
                     "_": "..--.-", '"': ".-..-.", ".": ".-.-.-", "@": ".--.-.", "`": ".----.", "-": "-....-",
                     ";": "-.-.-.", "!": "-.-.--", "=": "-...-", "/": "-..-.", "+": ".-.-.", "(": "-.--..",
                     ")": "-.--.-", ",": "--..--", ":": "---...", " ": " "}
    
    
    Out = ""
        
    for ch in Inp:
        if ch in Tran_In_Morze:
            Out += Tran_In_Morze[ch] + "  "
    
    return Out



@bot.message_handler(commands=["start"]) # Функция по обработке команды /start
def start(message, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Шифровать")
    markup.add(item1)
    item2=types.KeyboardButton("Дешифровать")
    markup.add(item2)
    
    bot.send_message(message.chat.id, "Привет! Я бот, который шифрует и дешифрут при помощи азбуки Морзе", reply_markup=markup)
    
    
@bot.message_handler(content_types=["text"]) # Функция по обработке основных кнопок
def menu(message, res=False):
    global answer

    if message.text.strip() == 'Шифровать':
        answer = "Напиши текст который хочешь зашифровать:"
        bot.register_next_step_handler(message, shif)
        
    elif message.text.strip() == 'Дешифровать':
        answer = "Напиши текст на азбуке Морзе который хочешь разшифровать:"
        bot.register_next_step_handler(message, deshif)
        
    else:
        answer = "Нажимай пожалуйста на кнопки, иначе я тебя не понимаю!"
        
    bot.send_message(message.chat.id, answer)
    
    
def shif(message, res=False):
    global answer
    
    answer = text_in_morze(message.text.strip())
    bot.send_message(message.chat.id, answer)
    

def deshif(message, res=False):
    global answer
    
    answer = morze_in_text(message.text.strip())
    bot.send_message(message.chat.id, answer)
    
    
    
bot.polling(none_stop=True, interval=0) # Запуск бота