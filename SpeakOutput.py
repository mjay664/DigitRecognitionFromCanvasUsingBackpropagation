import pyttsx


def speak_output(str_output):
    init = pyttsx.init('sapi5')
    init.say(str_output)
    init.runAndWait()


def number_to_string(number):
    if number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    elif number == 4:
        return 'four'
    elif number == 5:
        return 'five'
    elif number == 6:
        return 'six'
    elif number == 7:
        return 'seven'
    elif number == 8:
        return 'eight'
    elif number == 9:
        return 'nine'
    else:
        return 'zero'
