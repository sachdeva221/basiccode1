import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

var = Service("C:\\Users\\DELL\\Desktop\\Driver\\chromedriver.exe")

class new:
    Driver = webdriver.Chrome(service=var)
    num = ''
    def __init__(self):
        self.Driver.get('https://mail.google.com')

        self.Driver.maximize_window()
        self.Driver.find_element(By.XPATH, "//input[@type='email']").send_keys("gaurav.sachdeva1@team.cliffex.com")
        self.Driver.find_element(By.ID, "identifierNext").click()
        time.sleep(7)
        self.Driver.find_element(By.XPATH, "//input[@type= 'password']").send_keys("password")
        self.Driver.find_element(By.ID, "passwordNext").click()
        time.sleep(5)
class new2(new):
    def method(self):
        List = self.Driver.find_elements(By.CSS_SELECTOR, "div[class='yW'] span")
        for Lists in List:
            if Lists.text == "intellispine.csc":
                Lists.click()
                break
        time.sleep(2)

        A = self.Driver.find_element(By.XPATH, "(//div[@class='a3s aiL ']/h1)[1]").text
        need = A.split()
        self.num = need[3]

        new.Driver.close()