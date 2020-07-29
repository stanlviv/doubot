from bs4 import BeautifulSoup
import requests
import telebot

bot = telebot.TeleBot("1380969339:AAFgLsHADwLkM7sYASCrzpVQ0SrwfZX0L00")

def python_jobs():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
    html_jobs = requests.get('https://jobs.dou.ua/vacancies/?category=Python&exp=0-1', headers=header)
    if  html_jobs.status_code == 200:
        soup_h = BeautifulSoup(html_jobs.text, 'html.parser')
        items_jobs = soup_h.find_all('div', class_='vacancy')
        jobs = {}
        for item in items_jobs:
            jobs.update({item.find('a', class_='vt').get_text(): [item.find('a', class_='vt').get('href'), item.find('span', class_='cities').get_text()]})
        return jobs
    else:
        return 'Error'

def qa_jobs():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
    html_jobs = requests.get('https://jobs.dou.ua/vacancies/?category=QA&exp=0-1', headers=header)
    if  html_jobs.status_code == 200:
        soup_h = BeautifulSoup(html_jobs.text, 'html.parser')
        items_jobs = soup_h.find_all('div', class_='vacancy')
        jobs = {}
        for item in items_jobs:
            jobs.update({item.find('a', class_='vt').get_text(): [item.find('a', class_='vt').get('href'), item.find('span', class_='cities').get_text()]})
        return jobs
    else:
        return 'Error'

def frontend_jobs():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
    url = "https://jobs.dou.ua/vacancies/?category=Front%20End&exp=0-1"
    html_jobs = requests.get(url, headers=header)
    if  html_jobs.status_code == 200:
        soup_h = BeautifulSoup(html_jobs.text, 'html.parser')
        items_jobs = soup_h.find_all('div', class_='vacancy')
        jobs = {}
        for item in items_jobs:
            jobs.update({item.find('a', class_='vt').get_text(): [item.find('a', class_='vt').get('href'), item.find('span', class_='cities').get_text()]})
        return jobs
    else:
        return f"Error {html_jobs.status_code}"

def java_jobs():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
    url = "https://jobs.dou.ua/vacancies/?category=Java&exp=0-1"
    html_jobs = requests.get(url, headers=header)
    if  html_jobs.status_code == 200:
        soup_h = BeautifulSoup(html_jobs.text, 'html.parser')
        items_jobs = soup_h.find_all('div', class_='vacancy')
        jobs = {}
        for item in items_jobs:
            jobs.update({item.find('a', class_='vt').get_text(): [item.find('a', class_='vt').get('href'), item.find('span', class_='cities').get_text()]})
        return jobs
    else:
        return "Error"

def pm_jobs():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
    html_jobs = requests.get("https://jobs.dou.ua/vacancies/?category=Project+Manager&search=Львів", headers=header)
    if  html_jobs.status_code == 200:
        soup_h = BeautifulSoup(html_jobs.text, 'html.parser')
        items_jobs = soup_h.find_all('div', class_='vacancy')
        jobs = {}
        for item in items_jobs:
            jobs.update({item.find('a', class_='vt').get_text(): [item.find('a', class_='vt').get('href'), item.find('span', class_='cities').get_text()]})
        return jobs
    else:
        return 'Error'

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Python', 'QA')
keyboard1.row( 'Front End', 'Project Manager')

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("Weather_Bot", url='telegram.me/stas_weather_bot'))
    bot.send_message(message.chat.id, f"Привіт, {message.from_user.first_name}", reply_markup=keyboard1)
    bot.send_message(message.chat.id, "Я шукаю доступні вакансії на dou.ua\nПросто виберіть відповідну категорію",reply_markup=keyboard, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'python':
        try:
            jobs = python_jobs()
            bot.send_message(message.chat.id, f"*{len(jobs)} Job offers for < 1 year experience:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'qa':
        try:
            jobs = qa_jobs()
            bot.send_message(message.chat.id, f"*{len(jobs)} Job offers for < 1 year experience:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'front end':
        try:
            jobs = frontend_jobs()
            bot.send_message(message.chat.id, f"*{len(jobs)} Job offers for < 1 year experience:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    elif message.text.lower() == 'project manager':
        try:
            jobs = pm_jobs()
            bot.send_message(message.chat.id, f"*{len(jobs)} Job offers for < 1 year experience in Lviv:*\n", parse_mode='Markdown')
            for key, value in jobs.items():
                position = key
                link = value[0]
                city = value[1]
                bot.send_message(message.chat.id, f"[{position}]({link})\n{city}", parse_mode='Markdown', disable_web_page_preview=True)
        except Exception:
            bot.send_message(message.chat.id, "Error")
    else:
        bot.send_message(message.chat.id, "Error")

bot.polling(interval=5)
