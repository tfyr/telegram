from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
import json

from telegram.telegram import send_mess
import logging

@csrf_exempt
def bot(request):
    logger = logging.getLogger("django.request")
    if request.method == 'POST':
        #print(request.body.decode('utf-8'))
        logger.info(request.body.decode('utf-8'))
        msg = json.loads(request.body.decode('utf-8'))
        '''
        if 'message' in msg:
            txt = "Контрагенты:"
            with connections['kirsa'].cursor() as cursor:
                cursor.execute("select id, name from agent where name like %s", ["%ури%",])
                rows = cursor.fetchmany(7)
                arr_btn=[]
                for row in rows:
                    id, name = row
                    #txt += name+"\n"
                    arr_btn.append([
                        {
                            "text": name,
                            "callback_data": id
                        }])
                cursor.close()
                send_mess(msg['message']['chat']['id'], txt,
                          newurl="https://api.telegram.org/bot1228961072:AAFd9Ira5XNVnnETykGhkPH8bY6YFVmdQmk/",
                          reply_markup=json.dumps(
                                  {
                                      "inline_keyboard": arr_btn
                                  }
                              )
                          )
        '''

        if 'message' in msg:
            txt = "Отчеты:"
            arr_btn=[]
            arr_btn.append([
                        {
                            "text": 'Прогноз остатков',
                            "callback_data": 'balance-forecast'
                        }])
            arr_btn.append([
                        {
                            "text": 'Статистика',
                            "callback_data": 'stat'
                        }])
            send_mess(msg['message']['chat']['id'], txt,
                      newurl="https://api.telegram.org/bot1228961072:AAFd9Ira5XNVnnETykGhkPH8bY6YFVmdQmk/",
                      reply_markup=json.dumps(
                              {
                                  "inline_keyboard": arr_btn
                              }
                          )
                      )
        elif 'callback_query' in msg:
            txt = "Строки отчета\n"
            txt += "Строка 1\n"
            txt += "Строка 2\n"
            txt += "Строка 3\n"
            send_mess(msg['callback_query']['message']['chat']['id'], txt,
                      newurl="https://api.telegram.org/bot1228961072:AAFd9Ira5XNVnnETykGhkPH8bY6YFVmdQmk/",
                      #reply_markup=json.dumps(
                      #        {
                      #            "inline_keyboard": arr_btn
                      #        }
                      #    )
                      )

        #print(bodyjson)
        return HttpResponse(
            "",
            content_type="text/plain ",
        )
