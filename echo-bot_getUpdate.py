import requests
from time import sleep

TOKEN = 'write_yor_token'
URL = 'https://api.telegram.org/bot'+ TOKEN +'/'

global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    update_id = data['result'][-1]['update_id']
    global last_update_id
    if update_id != last_update_id:
        last_update_id = update_id
        chat_id = data['result'][-1]['message']['chat']['id']
        text_message = data['result'][-1]['message']['text']
        message = {'chat_id': chat_id, 'text': text_message}
        return message
    else:
        return None

def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']

            if answer['text'] != None:
                text = 'Привет, я бот-шмот'
                send_message(chat_id, text)
        else:
            continue

    sleep(10)


if __name__ == '__main__':
    main()