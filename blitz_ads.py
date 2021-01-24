import pyautogui as pag
import time, random, logging, datetime, ast

logging.basicConfig(filename='blitz.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info('Started')

def screenResolution():
       x, y = pag.size()
       return x, y

def halfOfScreen()
        x, y = screenResolution()
        x_axis = x / 2
        y_axis = y / 2
        return x_axis, y_axis

def screenshot(login):
        time.sleep(2)
        imgName = 'count//' + login + str(datetime.datetime.today()).replace(".", " ", 1).replace(":", "-", 1) + '.png'
        pag.screenshot(imgName, region=(117, 50, 1197, 42))

def check_if_main_menu():
        """Checking if on desplay main menu"""
        if pag.locateOnScreen('img//Wboi1.png', confidence=0.9) == None:
                back_button()
                time.sleep(3)
                check_if_main_menu()

def locate_video_button(videoButtonLocation):
        """Find location of video button and return if it is"""
        while not videoButtonLocation:
                if pag.locateOnScreen('img//reclama2.png', confidence=0.8) != None:
                        videoButtonLocation = pag.locateOnScreen('img//reclama2.png', confidence=0.9)
                        print(videoButtonLocation)
                        logging.info("Location of video button if " + str(videoButtonLocation))
                        return videoButtonLocation

def locate_box():
        "Locate if able to open a box"
        box = False
        while not box:
                if pag.locateOnScreen('img//box2.png', confidence=0.8, region=(1355, 44, 100, 100)) != None:
                        box = True
                        return True
			
def load_logins():
        """Load logins from logins.txt file and return it like users variable"""
        logging.info("Load logins from logins.txt file")
        with open("logins.txt", "r") as f:
                contents = f.read()
        users = ast.literal_eval(contents)
        return users

def close_video():
        """Clicks cross button, to close video"""
        exit_button = (1400, 82)
        exit_button2 = (32, 77)
        pag.click(exit_button[0], exit_button[1])

def back_button():
        """Clicks back button, to return to main menu"""
        pag.click(51, 75)

def open_box_menu(delay):
        """Open box menu"""
        if locate_box():
                logging.info("Start opaning box")
                pag.click(1381, 100)

                logging.info("Open menu")
                time.sleep(delay)

                pag.click(1101, 160)
                logging.info("Open box menu")
                time.sleep(delay)

def close_box(delay):
        back_button()
        logging.info("Close opaned prise")
        time.sleep(delay)

        back_button()
        back_button()
        logging.info("Back to main manu")

def play_video(cordinates, delay):
        """Start playng the wideo, after 33 seconds close video"""
        logging.info("Start plaing video")
        logging.info("Locating the video button")
        print(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
        video_button = locate_video_button(videoButtonLocation)
        play_button = (859, 616)

        logging.info("Click on play video button")
        pag.click(video_button)
        time.sleep(delay)

        logging.info("Confirm to play video")
        pag.click(play_button[0], play_button[1])
        time.sleep(45)
        
        logging.info("Close video after 35 sec delay")
        close_video()

def xp(delay):
        """Xp method stand for getting xp after watching video"""
        box = pag.locateOnScreen('img//xp.png', grayscale=True, confidence=0.9, region=(0, 174, 109, 816)) # Old coordinates (54, 410)
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
        time.sleep(delay)
        logging.info("Move to end of side menu")
        pag.click(55, 832)

        logging.info("Click on settings icon")
        time.sleep(delay)
        pag.click()

        logging.info("Disconnect")
        time.sleep(delay)
        pag.click(1163, 663)
        time.sleep(4)

def change_region(region, delay):
        """Change account region"""
        logging.info("Change region")
        pag.moveTo(849, 755, delay)
        pag.click()

        logging.info("Change to yuor region")
        pag.moveTo(region[0], region[1], delay)
        pag.click()

def enterText(comment, delay, text, point, typingSpeed):
        logging.info(comment)
        time.sleep(delay)
        pag.click(point)
        time.sleep(1)
        pag.typewrite(text, interval=typingSpeed)

def login(login, password, delay):
        typingSpeed = 0.1
        """Login to account"""
        logging.info("Start login")
        logging.info("Remove previos login")
        pag.click(989, 320, delay)

        enterText("Enter login", delay, login, (721, 325), typingSpeed)
        
        enterText("Enter password", delay, password, (721, 410), typingSpeed)

        logging.info("Press Enter")
        time.sleep(delay)
        pag.press('enter')
        time.sleep(30)
        
        check_if_main_menu()

def change_user(login_text, password_text, delay):
        """Change user to next on list"""
        logout(delay)
        time.sleep(delay)
        #change_region( ,delay)
        login(login_text, password_text, delay)

def open_medium_box(delay):
        """Check second and third boxes"""
        check_if_main_menu()
        open_box_menu(delay)
        x, y = pag.size()
        x_axis = x / 2
        y_axis = y / 2
        for pos in pag.locateAllOnScreen('img//openBox.png', confidence=0.8, region=(x_axis, y_axis, x, y)):
                pag.click(pos)
                time.sleep(delay)
                back_button()
                back_button()
                if pos == None:
                        pass
        back_button()

def open_box(counter, delay):
        """Stand for every day opaning 3 first boxes"""
        open_box_menu(delay)

        if pag.locateOnScreen('img//openBox.png', confidence=0.9, region=(86, 636, 368, 710)):
                pag.click(229, 704)
                logging.info("Open first box")
                time.sleep(delay)

                close_box(delay)
        else:
                back_button()
        

def count_users(user, users):
        """Count how much users in file"""
        for key in users:
                user += len(users[key])
        return user

def zeroing():
        count, box = 1, 1
        videoButtonLocation, boxDetection = False, False

def pixel_detection(delay, spot, colour):
        """Detects colour of pixel"""
        var = False
        while not var:
                if pag.pixelMatchesColor(spot[0], spot[1] ,(colour[0], colour[1], colour[2]), tolerance=10):
                        var = 1
                        return True
                

count, box = 1, 1
user, user_counter = 0, 0
videoButtonLocation, boxDetection = False, False

timedelay = 3

logging.info("Start detecting video button")

logins, passwords, timeTake = [], [], []

users = load_logins()

REGIONS = {"EU": [721, 354],"RU": [721, 438],"NA": [721, 530],"AS": [721, 619],"AC": [721, 687]} 

reg = len(users.keys())
logging.info("There is " + str(reg) + " regions.")

user = count_users(user, users)
logging.info("There is " + str(user) + " accounts.")

#for c in users.keys(): str(r)
for i, y in users["RU"].items():
        logins.append(i)
        passwords.append(y)

if count == 1:
        login(logins[user_counter], passwords[user_counter], timedelay)
        logging.info("Login to " + str(logins[user_counter]) + " user.")
        print("Login to " + str(logins[user_counter]) + " user in ")
        screenshot(logins[user_counter][:5])

while True:
        check_if_main_menu()
        if count <= 5:
                if count == 1 or count == 4:
                        if box == 1:
                                logging.info("Open " + str(box) + " box.")
                                print("Open " + str(box) + " box.")
                                box += 1
                                open_box(count, timedelay)
                                screenshot(logins[user_counter][:5])
                        time.sleep(timedelay)

                        if count == 4:
                                xp(timedelay)
                                logging.info("Get ?? XP")
                                print("Get ?? XP")
                                logging.info("Open " + str(box) + " box.")
                                print("Open " + str(box) + " box.")
                                open_box(count, timedelay)
                                screenshot(logins[user_counter][:5])
                                box += 1
        
                play_video(videoButtonLocation, timedelay)
                screenshot(logins[user_counter][:5])
                logging.info("Watch " + str(count) + " video.")
                print("Watch " + str(count) + " video.")
                count += 1
                time.sleep(110)

        elif count == 6:
                screenshot(logins[user_counter][:5]) 
                count += 1
                
                if box == 3:
                        time.sleep(90)
                        open_box(count, timedelay)
                        screenshot(logins[user_counter][:5])
                        
                        logging.info("Open " + str(box) + " box.")
                        print("Open " + str(box) + " box.")
                        box += 1

        elif count == 7:
                screenshot(logins[user_counter][:5])
                user_counter += 1
                time.sleep(3)
                if pag.locateOnScreen('img//box2.png', confidence=0.8):
                        open_medium_box(timedelay)
                        check_if_main_menu()
                
                if user_counter == user:
                        logout(timedelay)
                        print(timeTake)
                        break

                change_user(logins[user_counter], passwords[user_counter], timedelay)
                logging.info("Change user to " + str(logins[user_counter]))
                print("Change user to " + str(logins[user_counter]))
                count, box = 1, 1
                videoButtonLocation, boxDetection = False, False

