import pyttsx3 as pt3

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True
    raise RuntimeError('Language not found')

speaker = pt3.init()
speaker.setProperty('rate', 180)
speaker.setProperty('volume', 2)
speaker.setProperty('voice', speaker.getProperty('voice')[1])
speaker.setProperty('voice', 'vi')
#change_voice(speaker, r'b\x05vi', 'VoiceGenderFemale')
def robot_mouth(request):
    global speaker
    speaker.say(request)
    speaker.runAndWait()
