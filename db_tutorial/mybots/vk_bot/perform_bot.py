from .schedule.pars_schedule import get_schedule
import vk
# from flask import Flask, request, json
from .settings import *
import json
from .WORDS import WORDS, DAYS
from .Schedule40.schedule import get_schedule as get_arina_schedule
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt #exempt index() function from built-in Django protection
def take_care_about_call(request: 'request')->'performin bot action':

    data = json.loads(request.body) 
    
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':

        return make_a_respond(data)


def make_a_respond():

    # message = data['object']['body']

    session = vk.Session()
    api = vk.API(session, v=5.0)
    user_id = 47811061

    ar_schedule = get_arina_schedule('6г')

    api.messages.send(access_token=token, user_id=str(
                    user_id), message=ar_schedule)

    return 'ok' 
        

if __name__ == "__main__":
    
    make_a_respond()