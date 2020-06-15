import pyautogui as pag
import time, random, logging, datetime
'''Open BlueStack app on full screen and run bot'''
#pag.position()
logging.basicConfig(filename='blitz.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('Started')

def close_video():
    exit_button = (1400, 82)
    exit_button2 = (32, 77)

    #pag.moveTo(exit_button[0], exit_button[1], random.randint(2,4))
    pag.click(exit_button[0], exit_button[1])

def back_button():
    back = (51, 75)

    #pag.moveTo(back[0], back[1], random.randint(2,4))
    pag.click(back[0], back[1])

def play_video(delay):
    '''Play video method stand for play video, and close it after video ends'''
    logging.info("Start plaing video")
    video_button = (1373, 316)
    play_button = (859, 616)

    logging.info("Click on play video button")
    pag.click(video_button[0], video_button[1])
    time.sleep(delay)
    
    logging.info("Confirm to play video")
    pag.click(play_button[0], play_button[1])
    time.sleep(45)
    
    logging.info("Close video after 45 sec delay")
    close_video()

def xp(delay):
    '''Xp method stand for getting 1000 xp after watching video'''
    box = (54, 410)
    box_xp = (982, 395)
    
    logging.info("Open tasks")
    pag.click(box)
    time.sleep(delay)
    
    logging.info("Get XP from combat missions menu")
    pag.click(box_xp)
    time.sleep(delay)

    logging.info("Back to main menu")
    back_button()
    time.sleep(delay)

def change_user(delay):
    
    pag.moveTo(55, 832, delay)
    #Move to end of side menu
    pag.click()

    #Click on settings icon
    time.sleep(delay)
    pag.click()

    #Disconnect
    pag.moveTo(1163, 663, delay)
    pag.click()

    #Change region (if you have second account on same password and login)
    pag.moveTo(849, 755, delay)
    pag.click()

    #Change to europe
    pag.moveTo(721, 438, delay)
    pag.click()
    '''#Europe
    (721, 354)
    #Russia
    (721, 438)'''

    #Enter password
    pag.moveTo(744, 410, delay)
    pag.click()
    pag.typewrite('Enter password', interval=0.15) 

    #Press Enter
    pag.press('enter')

def open_box(delay):
    logging.info("Start opaning box")
    pag.click(1381, 97)
    logging.info("Open menu")
    time.sleep(delay)
    
    pag.click(1318, 198)
    logging.info("Open box menu")
    time.sleep(delay)
    
    pag.click(229, 704)
    logging.info("Open first box")
    time.sleep(delay)

    pag.click(clicks=2)
    logging.info("Close opaned prise")
    time.sleep(delay)

    back_button()
    logging.info("Back to main manu")

def open_game():
    pag.hotkey('win', 's')
    time.sleep(random.randint(1,3))
    pag.typewrite('bluestacks')
    time.sleep(random.randint(1,3))
    pag.hotkey('enter')

#open_game()
count = 1
box = 1
user = 1
timedelay = random.randint(2, 4)

while True:
    # default count < 6
    
    if count <= 5:
        if count == 1 or count == 4:
            open_box(timedelay)
            if box == 1 or box == 2:
                box += 1
                logging.info("Open " + str(box) + " box.")
        play_video(timedelay)
        logging.info("Watch " + str(count) + " video.")
        count += 1
        time.sleep(random.randint(131, 135))
        
    elif count == 6:
        xp(timedelay)
        logging.info("Get ?? XP")
        count += 1
        time.sleep(random.randint(70, 100))
        open_box(timedelay)
        box += 1
        logging.info("Open " + str(box) + " box.")

    elif count == 7:
        #change_user(timedelay)
        #logging.info("Сменил пользователя")
        #user += 1
        #count = 1
        #time.sleep(86400) if script must run all day long
        #pag.click(65, 94)
        #if user == 3: break
        break
