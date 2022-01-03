from    selenium                           import webdriver
from    selenium.webdriver.chrome.options  import Options
import time
import pyautogui
from time import sleep
chrome_options = Options()
chrome_options.add_argument("--window-size=1200,1080")
driver = webdriver.Chrome('./chromedriver.exe',options=chrome_options)
driver.get("http://sixphrase.com/users/sign_in")
print(driver.title)
user = driver.find_element_by_id("user_email")
passwd = driver.find_element_by_id("user_password")
user.send_keys(input("enter the username"))
passwd.send_keys("myslate")
driver.find_element_by_name("commit").click()
driver.get("http://sixphrase.com/course/5fb95ef719ab0a0f150e856c")
# print(input("enter something when you complete selecting the test"))
print(input("\n\n\n\nOpen the test and enter something when cursor is on the text box\n\n\n\n"),pyautogui.position())
x,y=pyautogui.position()
save = driver.find_element_by_id("save")
submit = driver.find_element_by_id("submit_code")
next = driver.find_element_by_id("next")
for i in range(0,10):
    pyautogui.click(x,y)
    f=open(str(i+1)+".txt",'r')    
    string = f.read()
    print("")
    pyautogui.typewrite(string)
    cnt=0
    for s in string:
        if s=='{':
            cnt+=1
    # pyautogui.keyDown("ctrl")
    # pyautogui.keyDown("shift")
    # pyautogui.press("up")
    # pyautogui.keyUp("ctrl")
    # pyautogui.keyUp("shift")
    # pyautogui.press("del")
    print("")
    sleep(10)
    save.click()
    submit.click()
    sleep(20)
    if i!=9:
        next.click()
    else:
        print("\n\n\n\n\t\t\tcompleted "+input("absd")+"\n\n\n\n")
sleep(10)
driver.close()