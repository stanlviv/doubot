from bs4 import BeautifulSoup
import requests
import telebot

bot = telebot.TeleBot("1380969339:AAFgLsHADwLkM7sYASCrzpVQ0SrwfZX0L00")

class Parser:
    def __init__(self, link):
        self.link = link
    
    def get_info(self):
        try:
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
            html_jobs = requests.get(self.link, headers=header)
            if  html_jobs.status_code == 200:
                soup_h = BeautifulSoup(html_jobs.text, 'html.parser')
                items_jobs = soup_h.find_all('div', class_='vacancy')
                jobs = {}
                for item in items_jobs:
                    jobs.update({item.find('a', class_='vt').get_text(): [item.find('a', class_='vt').get('href'), item.find('span', class_='cities').get_text()]})
            return jobs
        except Exception:
            return 'Error Occured!'

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Python', 'Java', 'QA')
keyboard1.row('Front End', 'Project Manager')
keyboard1.row('Technical Writer', 'iOS/macOS')
keyboard1.row('Support', 'Analyst')

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("Weather_Bot", url='telegram.me/stas_weather_bot'))
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name}", reply_markup=keyboard1)
    bot.send_message(message.chat.id, "Я шукаю доступні вакансії для початківців на dou.ua\nПросто виберіть відповідну категорію.\n\nТакож зацініть мого друга - бота, що показує погоду! :)",reply_markup=keyboard, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'python':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=Python&exp=0-1').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'qa':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=QA&exp=0-1').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'front end':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=Front%20End&exp=0-1').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'project manager':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=Project%20Manager&search=%D0%9B%D1%8C%D0%B2%D1%96%D0%B2').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців у Львові:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'java':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=Java&exp=0-1').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'technical writer':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=Technical%20Writer&exp=0-1').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'support':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=Support&exp=0-1').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'analyst':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=Analyst&exp=0-1').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text == 'iOS/macOS':
        try:
            jobs = Parser('https://jobs.dou.ua/vacancies/?category=iOS%2FmacOS&exp=0-1').get_info()
            bot.send_message(message.chat.id, f"*{len(jobs)} Вакансій для початківців:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    else:
        bot.send_message(message.chat.id, "Помилка. Спробуйте ще раз!")

bot.polling(interval=5)
