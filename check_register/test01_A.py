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

time.sleep(2)
# Bấm vào button "Đăng ký" trên thanh header
test_driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/li[1]/a').click()

time.sleep(2)

# Bấm vào button "Đăng ký"
test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[9]/td[2]/input').click()


#tắt testcase
# test_driver.close()
# test_driver.quit()