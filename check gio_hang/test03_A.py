from select import select
import  time
from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()
test_driver.maximize_window()

# Di chuyển đến địa chỉ "http://hamsterbabali.com/"
test_driver.get('http://hamsterbabali.com/')

test_driver.implicitly_wait(4)          #chờ ngầm định

test_driver.execute_script("window.scrollBy(0,500)","")
time.sleep(1)
# Bấm vào button "Mua"
test_driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[6]/div[1]/div[2]/div/div[1]/li[1]/div/div[2]/a[1]').click()
time.sleep(1)
# Bấm vào button "Xem giỏ hàng"
test_driver.find_element(By.XPATH,'/html/body/div[12]/div[2]/div/center/div/div[2]/center/div[2]/a').click()


#tắt testcase
# test_driver.close()
# test_driver.quit()