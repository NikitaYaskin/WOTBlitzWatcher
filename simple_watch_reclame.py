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

def open_box_menu(delay):
        """Open box menu"""
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
        video_button = (cordinates)
        play_button = (859, 616)

        logging.info("Click on play video button")
        pag.click(video_button[0], video_button[1])
        time.sleep(delay)

        logging.info("Confirm to play video")
        pag.click(play_button[0], play_button[1])
        time.sleep(35)

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
        print(login)
        pag.typewrite(login)

        logging.info("Enter password")
        time.sleep(delay)
        pag.click(721, 410)
        print(password)
        pag.typewrite(password) 

        logging.info("Press Enter")
        time.sleep(delay)
        pag.press('enter')
        time.sleep(25)
        
        if pag.pixelMatchesColor(683, 171, (238, 238, 238), tolerance=10) == None:
                back_button()
                time.sleep(5)

def change_user(login_text, password_text, delay):
    """Change user to next on list"""
    logout(delay)
    time.sleep(delay)
    #change_region( ,delay)
    login(login_text, password_text, delay)

def open_box(delay):
        """Stand for every day opaning 3 first boxes"""
        open_box_menu(delay)

        pag.click(229, 704)
        logging.info("Open first box")
        time.sleep(delay)

        close_box(delay)

def count_users(user, users):
        """Count how much users in file"""
        for key in users:
                user += len(users[key])
        return user

def zeroing():
        count, box = 1, 1

def pixel_detection(delay, spot, colour):
        """Detects colour of pixel"""
        var = False
        while not var:
                if pag.pixelMatchesColor(spot[0], spot[1] ,(colour[0], colour[1], colour[2]), tolerance=10):
                        var = 1
                        return True

def check_medium_box(delay, detection):
        """Check second and third boxes"""
        open_box_menu(delay)
        boxes = {(836, 291): (725, 684), (1331, 291): (1213, 680)}
        for item in boxes:
                if pixel_detection(delay, item, (196, 33, 22)):
                        detection = boxes[item]
                        logging.info("Detect box")
                        print(boxes[item])
                        logging.info("Open box")
                        pag.click(boxes[item])
                        time.sleep(delay)
                        back_button()
                        back_button()
                elif boxes[-1]:
                        back_button()
                else: print('No boxes')

count, box = 1, 1
user, user_counter = 0, 0
videoButtonLocation, boxDetection = False, False

timedelay = 2

logging.info("Start detecting video button")

logins, passwords, timeTake = [], [], []

users = load_logins()

REGIONS = {"EU": [721, 354],"RU": [721, 438],"NA": [721, 530],"AS": [721, 619],"AC": [721, 687]} 

reg = len(users.keys())
logging.info("There is " + str(reg) + " regions.")

user = count_users(user, users)
logging.info("There is " + str(user) + " accounts.")

#for r in users.keys(): str(r)
for i, y in users["RU"].items():
        logins.append(i)
        passwords.append(y)

if count == 1:
        login(logins[user_counter], passwords[user_counter], timedelay)
        logging.info("Login to " + str(logins[user_counter]) + " user.")
        print("Login to " + str(logins[user_counter]) + " user in ")


while True:
        if count <= 5:
                if count == 1 or count == 4:
                        open_box(timedelay)
                        time.sleep(timedelay)
                        if count == 1:
                                while not videoButtonLocation:
                                        if pag.pixelMatchesColor(1423, 385 ,(62, 152, 15), tolerance=20) or pag.pixelMatchesColor(1423, 385 ,(63, 155, 16), tolerance=20):
                                                videoButtonLocation = (1420, 390)
                                                logging.info("Video button detected in lowwer position")
                                                print(1420, 390)

                                        elif pag.pixelMatchesColor(1425, 273 ,(62, 154, 15), tolerance=20):
                                                videoButtonLocation = (1420, 282)
                                                logging.info("Video button detected in higher position")
                                                print(1420, 282)
                                                time.sleep(10)

                        if box == 1 or box == 2:
                                logging.info("Open " + str(box) + " box.")
                                print("Open " + str(box) + " box.")
                                box += 1
                play_video(videoButtonLocation, timedelay)
                logging.info("Watch " + str(count) + " video.")
                print("Watch " + str(count) + " video.")
                count += 1
                time.sleep(130)

        elif count == 6:
                xp(timedelay)
                logging.info("Get ?? XP")
                print("Get ?? XP")
                count += 1
                if box == 3:
                        time.sleep(80)
                        open_box(timedelay)
                logging.info("Open " + str(box) + " box.")
                print("Open " + str(box) + " box.")
                box += 1

        elif count == 7:
                user_counter += 1
                time.sleep(timedelay)
                if pag.pixelMatchesColor(1407, 65, (244, 244, 244), tolerance=20):
                        check_medium_box(timedelay, boxDetection)
                        
                if user_counter == user:
                        logout(timedelay)
                        print(timeTake)
                        break

                change_user(logins[user_counter], passwords[user_counter], timedelay)
                logging.info("Change user to " + str(logins[user_counter]))
                print("Change user to " + str(logins[user_counter]))
                count, box = 1, 1
