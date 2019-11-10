import pyautogui as pag
import os, time, sys, pdb, logging

logging.basicConfig(filename='watch.log',level=logging.DEBUG)

def open_full_screen(full_screen):
    if pag.locateOnScreen('D:\\Programming\\Python\\pyAutoGui\\WOT Blitz\\img\\fullScreen.png',region=full_screen, grayscale=True):
        pag.click(pag.locateOnScreen('D:\\Programming\\Python\\pyAutoGui\\WOT Blitz\\img\\fullScreen.png',region=full_screen, grayscale=True))
        logging.info('Open app full screen')
    else:
        time.sleep(10)
        logging.info('Button not found, try again')
        open_full_screen(full_screen)
        
def load_game():
    size = pag.size()
    search_bar = int(size[0]/10)
    pag.click(search_bar, size[1])
    time.sleep(1)
    pag.typewrite('bluestacks')
    time.sleep(1)
    pag.hotkey('enter')
    logging.info('Open exe')
    time.sleep(10)
    #pag.click(1296, 82)
    top_right_corner = (0,int(size[0]/2),int(size[1]/2),size[1])
    print(f'Cordinates of top right corner {top_right_corner}')
    logging.info(f'Cordinates of top right corner {top_right_corner}')
    open_full_screen(top_right_corner)
    time.sleep(5)
    pag.click(210, 178)
    logging.info('Start game')

def watch_video():
    video_icon = (1155,163,105,90)
    #play_button =
    logging.info('Search video icon')
    if pag.locateOnScreen('/img/reclama.png',region=video_icon , grayscale=True):
        pag.click(pag.locateOnScreen('/img/reclama.png',region=video_icon ,  grayscale=True))
        logging.info('Click on icon')
        time.sleep(2)
        #pag.click(pag.locateOnScreen('/img/watch.png',  grayscale=True))
        logging.info('Start play video')
        time.sleep(60)

    
print('Press Ctrl-C to quit.')
try:
    #while True:
    logging.info('Game start')
    load_game()
    #logging.info('Video start')
    #watch_video()
except KeyboardInterrupt:
    print('\n')
