import pyautogui as pag
import os, time, sys, pdb, logging

logging.basicConfig(filename='watch.log',level=logging.DEBUG)

def load_game():
    pag.click(174, 882)
    time.sleep(1)
    pag.typewrite('bluestacks')
    time.sleep(1)
    pag.hotkey('enter')
    logging.info('Open exe')
    time.sleep(5)
    pag.click(1296, 82)
    logging.info('Open app full screen')
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
    logging.info('Video start')
    watch_video()
except KeyboardInterrupt:
    print('\n')
