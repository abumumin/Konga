import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.konga.com/')
        driver.maximize_window()
        time.sleep(5)
        driver.find_element_by_xpath("//a[normalize-space()='Login / Signup']").click()
        time.sleep(1)
        driver.find_element_by_css_selector('#username').send_keys('zeepapka@gmail.com')
        # time.sleep(1)
        driver.find_element_by_css_selector('#password').send_keys('kwadu12@')
        time.sleep(2)
        driver.find_elements_by_class_name('#[class="_0a08a_3czMG _988cf_1aDdJ"]').click()
        time.sleep(3)
       # driver.find_element_by_xpath("//a[@class='ef511_2c5_i'][normalize-space()='Computers and Accessories']").click()
        #time.sleep(2)
        driver.find_element_by_xpath("//body[1]/div[1]/div[1]/section[1]/div[3]/section[1]/main[1]/section[2]/section[1]/section[1]/section[1]/section[1]/ul[1]/li[1]/div[1]/div[1]/div[2]/form[1]/div[4]/button[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body[1]/div[1]/div[1]/section[1]/div[3]/section[1]/main[1]/section[2]/section[1]/section[1]/section[1]/section[1]/ul[1]/li[3]/div[1]/div[1]/div[2]/form[1]/div[4]/button[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[normalize-space()='My Account']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='_12e27_1r3kc']//li[3]//a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//a[@class='_2e6a2_1gFdm fb688_312WU'])[1]").click()

        driver.find_element_by_xpath("//div[@class='_58074_2kiTq _387c1_1I1zQ']//span[contains(text(),'Request Payout')]")
        dro=select(driver.find_element_by_xpath("//div[@class='_58074_2kiTq _387c1_1I1zQ']//span[contains(text(),'Request Payout')]"))
        time.sleep(2)
        dro.select_by_visible_text('GTB')
        driver.find_element_by_xpath("//input[@id='account_number']").send_keys('0000000000')
        time.sleep(2)
        driver.find_element_by_css_selector("body > div:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(5) > section:nth-child(2) > main:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(3) > button:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='payout_amount']").send_keys('8000')
        time.sleep(2)
        driver.find_element_by_class_name("_0a08a_3czMG d28c3_1875P").click()




        time.sleep(5)
        driver.minimize_window()
        driver.quit()
findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()