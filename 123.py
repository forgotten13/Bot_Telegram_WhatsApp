import time, pyautogui, keyboard

time.sleep(5)
f = open('text_spammer.txt', 'r')
for line in f:
    time.sleep(0.5)
    if not keyboard.is_pressed('space'):
        pyautogui.typewrite(line)
        time.sleep(0.5)
        # pyautogui.press('enter')
    else:
        break

