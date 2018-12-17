from selenium import webdriver
from getpass import getpass
from pynput.keyboard import Key, Controller
import win32api, win32con
import time
import random
import sys

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
# usr = input('Enter your username or email : ')
# pwd = input('Enter your password : ')
usr="4kboffailure"
pwd="U_STUPID"

driver = webdriver.Chrome("C:/Users/Mehmet/Desktop/abc/chromedriver.exe")
driver.get('https://twitter.com/login')

usr_box = driver.find_element_by_class_name('js-username-field')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_class_name('js-password-field')
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
login_button.submit()

# new_tweet = driver.find_element_by_class_name('js-global-new-tweet')
# new_tweet.click()
# fp = open('fixed.txt') # Open file on read mode
# lines = fp.read().split("\n") # Create a list containing all lines
# fp.close()

# straw = lines[random.randint(0,len(lines)-1)]    
# berry = lines[random.randint(0,len(lines)-1)] 
# print(straw+"arse"+berry)

fp = open(sys.argv[1]+'tweet2send.txt')
tweet = fp.read();
fp.close()

keyboard = Controller()
# duran = straw.split("are")[0]
# uzan  = berry.split("are")[1]
keyboard.press(Key.f11)
keyboard.release(Key.f11)
click(875,230)

keyboard.press('n')
keyboard.release('n')
# print(straw.split("are")[0]+"are"+berry.split("are")[1])
# keyboard.type(straw.split("are")[0]+'are'+berry.split("are")[1])
keyboard.type(tweet)
keyboard.press(Key.ctrl)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.release(Key.ctrl)
click(920,250)
keyboard.press('n')
keyboard.release('n')
# keyboard.type(straw.split("are")[0]+'are'+berry.split("are")[1])
keyboard.type(tweet)
keyboard.press(Key.ctrl_l)
keyboard.press(Key.enter)
click(780,255)
keyboard.release(Key.enter)
keyboard.release(Key.ctrl_l)
click(780,255)
keyboard.press(Key.ctrl_l)
keyboard.press(Key.enter)
click(780,255)
keyboard.release(Key.enter)
keyboard.release(Key.ctrl_l)
click(780,255)
keyboard.press(Key.ctrl_l)
keyboard.press(Key.enter)
click(820,255)
click(820,255)
keyboard.release(Key.ctrl_l)
keyboard.release(Key.enter)
# click(700,130)
# click(922,181)
# click(913,310)
# click(530,230)
# click(913,310)
# tweet=driver.find_element_by_class_name('RichEditor-container')
# tweet.send_keys("debug5112592")

send_tweet = driver.find_element_by_css_selector('button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn')
send_tweet.submit()

sendbutton = driver.find_element_by_class_name('SendTweetsButton')
sendbutton.click()
