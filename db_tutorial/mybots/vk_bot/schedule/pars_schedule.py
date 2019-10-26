# from bs4 import BeautifulSoup
import requests
import random
from datetime import datetime
from datetime import timedelta


def get_date(day):

    if day == 'today':

        return datetime.today().strftime("%d.%m.%Y")

    else:

        today_day = datetime.today()

        start = today_day - timedelta(days=today_day.weekday())
        choosen_day = start + timedelta(days=day)
        return choosen_day.strftime("%d.%m.%Y")


def get_schedule_dict(day):

    date = get_date(day)

    url = 'https://www.chsu.ru/raspisanie'

    r = requests.post(url, data=get_body(date),
                      headers=get_headers(), params=get_params())  # params=get_params())

    try:
        return r.json()
    except:

        print('Something went wrong!')


def get_body(date):

    body = '_TimeTable_WAR_TimeTableportlet_cmd=timeTable&_TimeTable_WAR_TimeTableportlet_typeTimeTable=period&_TimeTable_WAR_TimeTableportlet_group=7%D0%AD%D0%91-01-51%D0%BE%D0%BF&_TimeTable_WAR_TimeTableportlet_semester=1+%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80+2016%2F2017&_TimeTable_WAR_TimeTableportlet_type=student&_TimeTable_WAR_TimeTableportlet_startDate=' + \
        date+'&_TimeTable_WAR_TimeTableportlet_endDate=' + \
        date  # &_TimeTable_WAR_TimeTableportlet_professor=3741'

    return body


def get_headers():

    headers = {'Sec-Fetch-Mode': 'cors',
               'Sec-Fetch-Site': 'same-origin',
               'Origin': 'https://www.chsu.ru',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Accept': '*/*',
               'Referer': 'https://www.chsu.ru/raspisanie',
               'X-Requested-With': 'XMLHttpRequest',
               'Connection': 'keep-alive'}

    return headers


def get_params():

    params = {'p_p_id': 'TimeTable_WAR_TimeTableportlet',
              'p_p_lifecycle': '2',
              'p_p_state': 'normal',
              'p_p_mode': 'view',
              'p_p_cacheability': 'cacheLevelPage',
              'p_p_col_id': 'column-1',
              'p_p_col_count': '1',
              }

    return params


def get_text(data):

    result = ''
    for i in data.get('response')['items']:

        time = str(i.get('time'))
        aud = str(i.get('audience'))
        prof_name = str(i.get('professor')['name'])
        disc = str(i.get('discipline'))

        result = result + (time+' | '+disc+' | '+aud+' | '+prof_name) + '\n'

    return result if result != '' else 'нет пар'


def get_schedule(day):

    return get_text(get_schedule_dict(day))


# if __name__ == '__main__':

#     print(get_schedule('today'))
