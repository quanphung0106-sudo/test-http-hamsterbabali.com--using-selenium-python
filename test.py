from select import select

from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

# Di chuyển đến địa chỉ "http://hamsterbabali.com/"
test_driver.get('http://hamsterbabali.com/')

test_driver.implicitly_wait(4)          #chờ ngầm định

# Nhập dữ liệu vào field 'email'
test_driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div/div/li[2]/a').click()

# Bấm vào button "Xem giỏ hàng"
script = "document.getElementByClassName('ui-slider-handle').style.left = '30.9677%';"
test_driver.execute_script(test_driver.find_element((By.XPATH, '/html/body/div[4]/div/div[5]/div/center[1]/div/div/span[1]')))

#tắt testcase
# test_driver.close()
# test_driver.quit()