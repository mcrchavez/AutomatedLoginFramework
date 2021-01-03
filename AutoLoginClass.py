
#Basic class for automated login startup script

from selenium import webdriver
import time
import datetime as dt

day_of_week = dt.datetime.now().weekday()
class AutoGMULogin:
    def __init__(self, browser='chrome', uname='', passwd=''):
        self.browser = browser
        self.uname = uname
        self.passwd = passwd
        if browser == 'chrome':
            self.web_d = webdriver.Chrome('C:/Users/carch/Downloads/chromedriver_win32/chromedriver.exe')
    def get_site(self, link):
        try:
            self.web_d.get(link)
        except Exception as e:
            print("Failed to get url through web driver")
            print(e)
    def click_by_xpath(self, xpath=''):
        """will return button element and click element"""
        web_button = ''
        try:
            if len(xpath)>1:
                web_button = self.web_d.find_element_by_xpath(str(xpath))
                web_button.click()
            else:
                return "enter valid xpath for button"
        except Exception as e:
            print("click by xpath failed")
            print(e)
        return web_button
    def find_login_elems(self, userid='username', passid='password'):
        """returns tuple of web elements [0] == username
        [1] == password given element ids"""
       
        try:
            return (self.web_d.find_element_by_id(userid), self.web_d.find_element_by_id(passid))
        except Exception as e:
            print("webelement not found with given strings as id")
            print(e)   
    def send_keys(self, browserelem, string):
        browserelem.send_keys(string)
    



