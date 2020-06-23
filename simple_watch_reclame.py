import pyautogui as pag
import time, random, logging, datetime

logging.basicConfig(filename='blitz.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('Started')

def close_video():
    exit_button = (1400, 82)
    exit_button2 = (32, 77)

    pag.click(exit_button[0], exit_button[1])

def back_button():
    pag.click(51, 75)

def play_video(delay):
	logging.info("Start plaing video")
	video_button = (1373, 314)
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

def logout(delay):
	pag.moveTo(55, 832, delay)
	logging.info("Move to end of side menu")
	pag.click()

	logging.info("Click on settings icon")
	time.sleep(delay)
	pag.click()

	logging.info("Disconnect")
	pag.moveTo(1163, 663, delay)
	pag.click()

def change_region(region, delay):
	logging.info("Change region")
	pag.moveTo(849, 755, delay)
	pag.click()

	logging.info("Change to yuor region")
	pag.moveTo(region[0], region[1], delay)
	pag.click()

def login(login, password, delay):
	logging.info("Start login")
	logging.info("Remove previos login")
	pag.click(989, 320, delay)

	logging.info("Enter login")
	pag.moveTo(721, 325, delay)
	pag.click()
	pag.typewrite(login) 

	logging.info("Enter password")
	pag.moveTo(721, 410, delay)
	pag.click()
	pag.typewrite(password) 

	logging.info("Press Enter")
	pag.press('enter')
	time.sleep(10)

def change_user(login_text, password_text, delay):
    
    logout(delay)
    time.sleep(delay)
    #change_region( ,delay)
    login(login_text, password_text, delay)

def open_box(delay):
    logging.info("Start opaning box")
    pag.click(1381, 100)

    logging.info("Open menu")
    time.sleep(delay)
    
    pag.click(1024, 158)#1318, 198)
    logging.info("Open box menu")
    time.sleep(delay)
    
    pag.click(229, 704)
    logging.info("Open first box")
    time.sleep(delay)

    back_button()
    logging.info("Close opaned prise")
    time.sleep(delay)

    back_button()
    back_button()
    logging.info("Back to main manu")

def open_game():
    pag.hotkey('win', 's')
    time.sleep(random.randint(1,3))
    pag.typewrite('bluestacks')
    time.sleep(random.randint(1,3))
    pag.hotkey('enter')

def count_users(user, users):
	for key in users:
		user += len(users[key])
	return user

count, box = 1, 1
user, user_counter = 0, 0
timedelay = 3
logins, passwords = [], []
users = {"RU": {"mail1@mail.com": "password1", 
				"mail2@gmail.com": "password2"}}
REGIONS = {"EU": [721, 354],"RU": [721, 438],"NA": [721, 530],"AS": [721, 619],"AC": [721, 687]} 

reg = len(users.keys())
logging.info("There is " + str(reg) + " regions.")

user = count_users(user, users)
logging.info("There is " + str(user) + " accounts.")

for i, y in users["RU"].items():
	logins.append(i)
	passwords.append(y)

login(logins[user_counter], passwords[user_counter], timedelay)
logging.info("Login to " + str(logins[user_counter]) + " user.")

'''
while True:
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
        if box == 3:
        	time.sleep(random.randint(70, 100))
        	open_box(timedelay)
        box += 1
        logging.info("Open " + str(box) + " box.")

    elif count == 7:
    	if user_counter == user:
    		logout(timedelay)
    		break

    	user_counter += 1
    	change_user(logins[user_counter], passwords[user_counter], timedelay)
    	#TypeError: 'str' object is not callable
    	logging.info("Change user to " + str(logins[user_counter]))
    	count = 1
    	pag.click(65, 94)'''