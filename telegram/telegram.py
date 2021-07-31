import requests

url = "..."

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text, newurl=None, reply_markup=None, parse_mode=None):
    params = {'chat_id': chat, 'text': text}
    if reply_markup:
        params['reply_markup'] = reply_markup
    if parse_mode:
        params['parse_mode'] = parse_mode
    response = requests.post((url if not newurl else newurl)+ 'sendMessage', data=params)
    return response


def send_mediagroup(chat, media, newurl=None,):
    params = {'chat_id': chat, 'media': media}
    response = requests.post((url if not newurl else newurl)+ 'sendMediaGroup', data=params)
    return response


def send_image(chat_id, newurl=None, multipart_formdata=None, caption=None):
    return requests.post((url if not newurl else newurl)+ 'sendPhoto', files=multipart_formdata, data={'chat_id' : chat_id, 'caption':caption, })



