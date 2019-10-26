from django.shortcuts import render
from .vk_bot.perform_bot import take_care_about_call
from django.http import HttpResponse

# Create your views here.

def perform_bot(request):

    # take_care_about_call(request)

    return HttpResponse('ok')


def get_schedule(request):

    pass