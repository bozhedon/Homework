import requests
import telebot
from html.parser import HTMLParser

# def send_response(user_id, text):
#     SEND_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
#     CHAT_ID = user_id
#     url = SEND_URL.format(
#         BOT_API_TOKEN,
#         CHAT_ID,
#         text
#     )
#     requests.get(url)


BOT_API_TOKEN = '1033051975:AAHq6OBtzYy2vTYBKmvgN-mLz-NYI_Il4ZY'
# CHAT_ID = '@nefu_puthon'
# url = SEND_URL.format(
#     BOT_API_TOKEN,
#     CHAT_ID,
#     'privet guys!'
# )
# READ_URL = 'https://api.telegram.org/bot{}/getupdates'
# url = READ_URL.format(BOT_API_TOKEN)
# response = requests.get(url)
# updates = response.json().get('result', [])
# for msg in updates:
#     text = msg['message']['text']
#     user_id = msg['message']['from']['id']
#     print(user_id, text)
#     if 'погода' not in text.lower():
#         continue
#     send_response(user_id, 'pogoda')

READ_URL = 'https://news.ykt.ru/article/95454'
response = requests.get(READ_URL)


class ArticleParser(HTMLParser):

    def __init__(self):
        self.statusRead = False
        self.myText = ''
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.statusRead = True

    def handle_endtag(self, tag):
        if tag == 'p' and self.statusRead:
            self.statusRead = False

    def handle_data(self, data):
        if self.statusRead and data.strip() not in ('Источник:', 'News.Ykt.Ru', 'Зарегистрироваться', 'Это интересно'):
            self.myText += data.strip()

    def feed(self, data):
        super().feed(data)
        return self.myText


parser = ArticleParser()
gg = parser.feed(response.text)
print(gg)
