import pyautogui as pag
import time, random

#wait_time = 120
#video_play = 30
count = 0

def play_video():
    video_button = (1263, 201)
    play_button = (737, 601)
    exit_button = (1382, 102)
    exit_button2 = (32, 77)
    
    pag.click(video_button)
    time.sleep(random.randint(2,4))
    pag.click(play_button)
    time.sleep(random.randint(35,45))
    pag.click(exit_button)
    #pag.click(exit_button2)
    ++count

while True:
    # default count < 6
    if count < 6:
        play_video()
        time.sleep(random.randint(135,140))
    else:
        break
        #time.sleep(86400) if script must run all day long
        #pag.click(65, 94)
