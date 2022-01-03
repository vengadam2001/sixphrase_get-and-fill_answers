from    selenium                           import webdriver
from    selenium.webdriver.chrome.options  import Options
from    scrapy.selector                    import Selector 
# import time
# from bs4 import BeautifulSoup
# from lxml import etree
# import pyautogui
# from time import sleep

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("http://sixphrase.com/users/sign_in")
print(driver.title)
user = driver.find_element_by_id("user_email")
passwd = driver.find_element_by_id("user_password")
# username = input("\n\n\n\nenter baliaadu account, format: name.UniqueId: ")
username = input("enter the username from which answer should be taken")
user.send_keys(username+"@sret.edu.in")
passwd.send_keys("myslate")
driver.find_element_by_name("commit").click()
driver.get(input("\n\n\n\n Enter the answer source link including the https formating :\n\n\n\n"))
driver.find_element_by_xpath("/html/body/header/div/div/div/div/ul/li[2]/a").click()
source = driver.page_source
source = Selector(text = source)
i=1
qote="'"
qotes='"'
flag=False
while (i<=10):
    divs = source.xpath('//div[@id="code-editor'+str(i)+'"]/div[2]/div/div[3]/div')
    string =''
    for div in divs:
        for z in div.xpath('./div/span'):
            # print(z.xpath("text()").get())
            if  z.xpath("text()").get()==qotes:
                flag=not(flag)
                print("hello ggwp \n")
            if flag == False:      
                string += z.xpath("text()").get()+" "
            else:
                string += z.xpath("text()").get()
        string+='\n'
    print(i)
    f= open(str(i)+".txt",'w')
    f.write(string)
    f.close()
    i+=1
# soup = BeautifulSoup(driver.page_source, "html.parser")
# dom = etree.HTML(str(soup))
# print(dom.xpath('//div[@id="code-editor1"]/div[2]/div/div[3]/div')[0].text)
# soup = BeautifulSoup(source, 'html.parser')
# print(soup.prettify())
driver.close()
