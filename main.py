import hear
import logic
import speak
import CalcModulo as CM
import time

hearing = False
is_calc_mode = False
inp = input('Select your mode: auto/ manual: ')
if inp == 'auto':
    hearing = True

while True:
    time.sleep(1)
    if hearing:
        text = hear.robot_ear()
        speak.robot_mouth('Recorded')
    else:
        text = input('Give your command: ')
    if 'calculator' in text:
        is_calc_mode = True
        speak.robot_mouth('Activating calculator mode')
        continue
    if is_calc_mode:
        if 'down' in text or 'exit' in text:
            speak.robot_mouth('Exiting calculator mode')
            is_calc_mode = False
            continue
        else:
            try:
                temp = CM.calc_mode(text)
                answer = f"The answer is {temp.calc(temp.arr)}"
            except:
                answer = 'Invalid operator'
    else:
        answer = logic.brain(text)
        if answer == 'CMD1': #Exit
            speak.robot_mouth('Exiting system')
            break
        elif answer == 'CMD2': #Music
            continue
    speak.robot_mouth(answer)