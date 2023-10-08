from django.shortcuts import render
from .pinpoint import main

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    # main() // needs more testing
    return render(request, "chat/room.html", {"room_name": room_name})