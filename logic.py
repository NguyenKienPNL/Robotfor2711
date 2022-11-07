import time
from datetime import date, datetime
from pygame import mixer
import speak
def play_music():
    mixer.init()
    mixer.music.load(r"C:\Users\DaSquareroot\Code\MyProjects\AIProject\audio and music\music (online-audio-converter.com).mp3")
    mixer.music.play()
    while True:
        inp = int(input())
        if inp == 1:
            mixer.music.pause()
        elif inp == 2:
            mixer.music.unpause()
        elif inp == 3:
            mixer.music.stop()
            return
def brain(request):
    if request == "":
        return "I can't hear you"
    #Command
    if request == 'Error1':
        return "I can't hear you"
    request = request.lower()
    request = request.split(' ')
    if "hi" in request or 'hello' in request:
        answer = "Nice to meet you"
    elif "date" in request:
        answer = f"It's {date.today()}"
    elif 'time' in request or 'now' in request:
        now = datetime.now().strftime("%H: %M: %S")
        answer = f"It's {now}"
    elif 'name' in request:
        return 'My name is Da Masterpiece'
    elif "bye" in request or 'goodbye' in request:
        return 'CMD1'
    elif 'music' in request:
        speak.robot_mouth('playing music')
        play_music()
        return 'CMD2'
    elif 'old' in request:
        return "I'm 1 month old"
    elif 'can' in request:
        return 'Anything'
    elif 'marry' in request:
        return 'Heck no'
    else:
        answer = "Unsupported"
    return answer
