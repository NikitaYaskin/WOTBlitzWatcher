import pyautogui as pag
import time, random, logging, datetime, ast

logging.basicConfig(filename='blitz.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('Started')

def load_logins():
	"""Load logins from logins.txt file and return it like users variable"""
	logging.info("Load logins from logins.txt file")
	file = open("logins.txt", "r")
	contents = file.read()
	users = ast.literal_eval(contents)
	file.close()
	return users

def close_video():
	"""Clicks cross button, to close video"""
    exit_button = (1400, 82)
    exit_button2 = (32, 77)

    pag.click(exit_button[0], exit_button[1])

def back_button():
	"""Clicks back button, to return to main menu"""
    pag.click(51, 75)

def play_video(cordinates, delay):
	"""Start playng the wideo, after 33 seconds close video"""
	logging.info("Start plaing video")
	video_button = (cordinates)
	play_button = (859, 616)

	logging.info("Click on play video button")
	pag.click(video_button[0], video_button[1])
	time.sleep(delay)

	logging.info("Confirm to play video")
	pag.click(play_button[0], play_button[1])
	time.sleep(33)

	logging.info("Close video after 35 sec delay")
	close_video()

def xp(delay):
    """Xp method stand for getting xp after watching video"""
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
	"""Logout account"""
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
	"""Change account region"""
	logging.info("Change region")
	pag.moveTo(849, 755, delay)
	pag.click()

	logging.info("Change to yuor region")
	pag.moveTo(region[0], region[1], delay)
	pag.click()

def login(login, password, delay):
	"""Login to account"""
	logging.info("Start login")
	logging.info("Remove previos login")
	pag.click(989, 320, delay)

	logging.info("Enter login")
	time.sleep(delay)
	pag.click(721, 325)
	pag.typewrite(login) 

	logging.info("Enter password")
	time.sleep(delay)
	pag.click(721, 410)
	pag.typewrite(password) 

	logging.info("Press Enter")
	time.sleep(delay)
	pag.press('enter')
	time.sleep(20)
	back_button()

def change_user(login_text, password_text, delay):
    
    logout(delay)
    time.sleep(delay)
    #change_region( ,delay)
    login(login_text, password_text, delay)

def open_box(delay):
	"""Stand for every day opaning 3 first boxes"""
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

def zeroing():
	count, box = 1, 1

count, box = 1, 1
user, user_counter = 0, 0
timedelay = 2
x = False
logins, passwords = [], []

users = load_logins()

REGIONS = {"EU": [721, 354],"RU": [721, 438],"NA": [721, 530],"AS": [721, 619],"AC": [721, 687]} 

reg = len(users.keys())
logging.info("There is " + str(reg) + " regions.")

user = count_users(user, users)
logging.info("There is " + str(user) + " accounts.")

for r in users.keys():
	for i, y in users[str(r)].items():
		logins.append(i)
		passwords.append(y)

login(logins[user_counter], passwords[user_counter], timedelay)
logging.info("Login to " + str(logins[user_counter]) + " user.")

while True:
	if count <= 5:
		if count == 1 or count == 4:
			open_box(timedelay)
			time.sleep(timedelay)
			if count == 1:
				logging.info("Start detecting video button")
				while not x:
					if pag.pixelMatchesColor(1423, 385 ,(62, 152, 15), tolerance=10) or pag.pixelMatchesColor(1423, 385 ,(63, 155, 16), tolerance=10):
						x = (1423, 385)
						logging.info("Video button detected in upper position")
					elif pag.pixelMatchesColor(1425, 273 ,(62, 154, 15), tolerance=10):
						x = (1425, 273)
						logging.info("Video button detected in lower position")
					time.sleep(10)
			if box == 1 or box == 2:
				box += 1
				logging.info("Open " + str(box) + " box.")
		play_video(x, timedelay)
		logging.info("Watch " + str(count) + " video.")
		count += 1
		time.sleep(130)

	elif count == 6:
		xp(timedelay)
		logging.info("Get ?? XP")
		count += 1
		if box == 3:
			time.sleep(80)
			open_box(timedelay)
		box += 1
		logging.info("Open " + str(box) + " box.")

	elif count == 7:
		user_counter += 1
		if user_counter == user:
			logout(timedelay)
			break

		change_user(logins[user_counter], passwords[user_counter], timedelay)
		logging.info("Change user to " + str(logins[user_counter]))
		count, box = 1, 1
		pag.click(65, 94)