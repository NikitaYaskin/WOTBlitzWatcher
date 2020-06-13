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

def play_video():
    '''Play video method stand for play video, and close it after video ends'''
    video_button = (1373, 422)
    play_button = (859, 616)
    

    #pag.moveTo(video_button[0], video_button[1], random.randint(3,4))
    pag.click(video_button[0], video_button[1])
    #pag.moveTo(play_button[0], play_button[1], random.randint(3,4))
    time.sleep(random.randint(1, 3))
    pag.click(play_button[0], play_button[1])
    time.sleep(random.randint(40, 50))
    close_video()

def xp():
    '''Xp method stand for getting 1000 xp after watching video'''
    box = (54, 410)
    box_xp = (982, 395)
    
    #Open tasks
    #pag.moveTo(box[0], box[1], random.randint(2,4))
    pag.click(box)
    time.sleep(random.randint(1, 3))
    
    #Get 1000 xp
    #pag.moveTo(box_xp[0], box_xp[1], random.randint(2,4))
    pag.click(box_xp)
    time.sleep(random.randint(1,3))

    #Back to main menu
    back_button()

def change_user():
    pag.moveTo(55, 832, random.randint(2, 4))
    #Move to end of side menu
    pag.click()

    #Click on settings icon
    time.sleep(random.randint(2,4))
    pag.click()

    #Disconnect
    pag.moveTo(1163, 663, random.randint(2, 4))
    pag.click()

    #Change region (if you have second account on same password and login)
    pag.moveTo(849, 755, random.randint(2, 4))
    pag.click()

    #Change to europe
    pag.moveTo(721, 438, random.randint(2, 4))
    pag.click()
    '''#Europe
    (721, 354)
    #Russia
    (721, 438)'''

    #Enter password
    pag.moveTo(744, 410, random.randint(2, 4))
    pag.click()
    pag.typewrite('OlaDiana2', interval=0.15) 

    #Press Enter
    pag.press('enter')

def open_box():
    logging.info("Start opaning box")
    pag.click(1381, 97)
    logging.info("Open menu")
    time.sleep(random.randint(2,4))
    #pag.screenshot("\\actions\\" + str(datetime.datetime.now()).replace(":", "-") + ".png")
    
    pag.click(1318, 198)
    logging.info("Open box menu")
    time.sleep(random.randint(2,4))
    
    pag.click(229, 704)
    logging.info("Open first box")
    time.sleep(random.randint(2,4))

    pag.click()
    logging.info("Close opaned prise")
    time.sleep(random.randint(2,4))

    back_button()
    logging.info("Back to main manu")

def open_game():
    pag.hotkey('win', 's')
    time.sleep(random.randint(1,3))
    pag.typewrite('bluestacks')
    time.sleep(random.randint(1,3))
    pag.hotkey('enter')

#open_game()
count = 2
box = 2
while True:
    # default count < 6
    
    if count <= 5:
        if count == 1 or count == 4:
            open_box()
            if box == 1 or box == 2:
                box += 1
                logging.info("Open " + str(box) + " box.")
        play_video()
        logging.info("Watch " + str(count) + " video.")
        count += 1
        time.sleep(random.randint(132, 140))
        
    elif count == 6:
        xp()
        logging.info("Get ?? XP")
        count += 1
        time.sleep(random.randint(100, 160))
        open_box()
        box += 1
        logging.info("Open " + str(box) + " box.")

    elif count == 7:
        #change_user()
        #logging.info("Сменил пользователя")
        #count = 1
        break
        #time.sleep(86400) if script must run all day long
        #pag.click(65, 94)
