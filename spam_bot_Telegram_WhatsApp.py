import time, pyautogui, keyboard

time.sleep(5) # Задержка по времени
f = open('text_spammer.txt', 'r') # Открываем файл для чтения

for line in f:
    if not keyboard.is_pressed('space'): # остановка программы по нажатии пробела (keyboard)
        time.sleep(0.5)  # Задержка по времени
        pyautogui.typewrite(line) # Считывание текста из файла по линии
        pyautogui.press('enter') # нажатие Enter
    else:
        break
