from select import select

from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

# Di chuyển đến địa chỉ "http://hamsterbabali.com/"
test_driver.get('http://hamsterbabali.com/')

test_driver.implicitly_wait(4)          #chờ ngầm định


# Bấm vào button "Đăng nhập"
test_driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/li[2]/a').click()

# Nhập dữ liệu vào field 'email'
test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[1]/td[2]/input').send_keys('quanphung@gmail.com')

# Nhập dữ liệu vào field 'password'
test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[2]/td[2]/input').send_keys('quan123')

# Bấm vào button "Đăng nhập"
test_driver.find_element(By.CSS_SELECTOR,'#kiemtra_login').click()


#tắt testcase
# test_driver.close()
# test_driver.quit()