from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


def getBrowser():
    PATH = "C:\Program Files\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.maximize_window()
    driver.get('http://edonkey:8887/drive')
    driver.implicitly_wait(10)


def driDonkeyConst():
   
    x= Service('C:\Program Files\chromedriver.exe') 
    driver = webdriver.Chrome(service=x)
    
    driver.get('http://edonkey:8887/drive')
    driver.implicitly_wait(10)
    
    #set throttle max speed 
    mThrottle = driver.find_element(By.ID,'max_throttle_select')
    mThrottle_select = Select(mThrottle)
    mThrottle_select.select_by_value('0.15')

    # set mode to constant to lock movement forward
    mMthrottle = driver.find_element(By.ID,'throttle_mode_select')
    mThrottle_select = Select(mMthrottle)
    mThrottle_select.select_by_value('user')
   
    # Move Joystick
    source1 = driver.find_element(By.ID,'joystick_container')
    AC(driver).click_and_hold(source1).perform()
    #go straight
    AC(driver).move_by_offset(0,-25).perform()
    time.sleep(2)
    #turn
    AC(driver).move_by_offset(-90,-10).perform()
    time.sleep(2)
    #straight
    AC(driver).move_by_offset(100,-20).perform()
    time.sleep(1)
    #turn
    AC(driver).move_by_offset(-130,-10).perform()
    time.sleep(2)
    #straight
    AC(driver).move_by_offset(140,-10).perform()
    time.sleep(3)
    #turn
    #AC(driver).move_by_offset(-160,-10).perform()


    

    driver.close()
    



    
def activateLocalPilot():

    x= Service('C:\Program Files\chromedriver.exe') 
    driver = webdriver.Chrome(service=x)

    driver.get('http://edonkey:8887/drive')
    driver.implicitly_wait(10)

    #set max throttle speed
    mThrottle = driver.find_element_by_id('max_throttle_select')
    mThrottle_select = Select(mThrottle)
    mThrottle_select.select_by_value('0.25')

    # once have a model trained select local got loca model
    mMode = driver.find_element(By.ID,'mode_select')
    mode_Select = Select(mMode)
    mode_Select.select_by_value('local')

    #start Driving
    src = driver.find_element(By.PARTIAL_LINK_TEXT,'Vehicle')
    AC(driver).click(src)

    driver.close()
    



def stopDonkey():
    x= Service('C:\Program Files\chromedriver.exe') 
    driver = webdriver.Chrome(service=x)

    driver.get('http://edonkey:8887/drive')
    driver.implicitly_wait(10)

    # set driving mode to user
    mThrottle = driver.find_element(By.ID,'throttle_mode_select')
    mThrottle_Select = Select(mThrottle)
    mThrottle_Select.select_by_value('user')

    #test needed to stop recording
    source1 = driver.find_element(By.ID,'joystick_container')
    AC(driver).click(source1).perform()

    #this action should stop the car since throttle is set to 0
    src = driver.find_element(By.ID,'brake_button')
    AC(driver).click(src).perform()
    AC(driver).click_and_hold(src).perform()
    AC(driver).move_by_offset(0,-20).perform()


    driver.close()

def uTurn():

    x= Service('C:\Program Files\chromedriver.exe') 
    driver = webdriver.Chrome(service=x)

    driver.get("http://edonkey:8887/drive")
    driver.switch_to.frame(0)

    source1 = driver.find_element_by_id('joystick_container')
    act=webdriver.ActionChains(driver)
    act.click_and_hold(source1).perform()
    act.move_by_offset(0,-50).perform()
    time.sleep(8)
    act.move_by_offset(100,70).perform()
    time.sleep(8)
    act.move_by_offset(0,-50).perform()
    time.sleep(8)
    act.move_by_offset(100,-50).perform()
    driver.close()

if __name__ == '__main__':
    driDonkeyConst()
    stopDonkey()
    activateLocalPilot()
