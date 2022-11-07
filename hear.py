import speech_recognition as sr
import speak
import time

reg = sr.Recognizer()
reg.energy_threshold = 300
mic = sr.Microphone()

def robot_ear():
    with mic as source:
        reg.adjust_for_ambient_noise(source)
        speak.robot_mouth("I'm listening")
        t1 = time.time()
        inp = reg.listen(source)
        t2 = time.time()
        if t2 - t1 > 4:
            return 'Error1'
        try:
            text = reg.recognize_google(inp)
            return text
        except sr.UnknownValueError:
            return 'Say again'
        except sr.RequestError:
            return 'Speech service down'
