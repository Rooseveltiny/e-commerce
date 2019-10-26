from django.shortcuts import render
from .vk_bot.perform_bot import take_care_about_call

# Create your views here.

def perform_bot(request):

    take_care_about_call(request)