import urllib

import img as img
import pyautogui
import pytesseract
from PIL import Image
from pytesseract import *
from select import select
import  time

from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

test_driver = webdriver.Chrome()
test_driver.get('http://hamsterbabali.com/')
test_driver.implicitly_wait(4)

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Bấm vào button "Đăng ký" trên thanh header
test_driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/li[1]/a').click()
time.sleep(3)

# Nhập dữ liệu vào field 'email'
test_driver.find_element(By.CSS_SELECTOR, '#reg_email').send_keys('hoangnhi321123@gmail.com')
time.sleep(3)

# Nhập dữ liệu vào field 'password'
test_driver.find_element(By.CSS_SELECTOR, '#reg_password').send_keys('hoangnhi123')
time.sleep(1)

# Nhập dữ liệu vào field 'họ tên'
test_driver.find_element(By.CSS_SELECTOR, '#reg_hoten').send_keys('Hoàng Nhi')
time.sleep(3)

# select box "giới tính" và chọn giới tính Nữ
gioiTinh = Select(test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[4]/td[2]/select'))
# select by value
gioiTinh.select_by_value('0')
time.sleep(1)

# Nhập dữ liệu vào field 'phone'
test_driver.find_element(By.CSS_SELECTOR, '#reg_phone').send_keys('0935123123')
time.sleep(1)

# select box "tỉnh thành" và chọn "Huế"
gioiTinh = Select(test_driver.find_element(By.CSS_SELECTOR, '#reg_tinh'))
# select by value
gioiTinh.select_by_value('Huế')
time.sleep(1)

# Nhập dữ liệu vào field 'địa chỉ'
test_driver.find_element(By.CSS_SELECTOR, '#reg_diachi').send_keys('50 Nguyễn Xuân Hữu, Đà Nẵng')
time.sleep(1)

#get img source

imgSource = test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[8]/td[2]/table/tbody/tr/td[2]/div/img')

# the image link
myImg = imgSource.get_attribute('src')

#open new tab
test_driver.execute_script("window.open('');")
test_driver.switch_to.window(test_driver.window_handles[1])
test_driver.get(myImg)
myText = test_driver.save_screenshot("D:\\WorkSpace\\python\\testcase_quanphung\\check_register\\code.png")

output = pytesseract.image_to_string("D:\\WorkSpace\\python\\testcase_quanphung\\check_register\\code.png")

test_driver.switch_to.window(test_driver.window_handles[0])

# Nhập dữ liệu vào field 'mã xác nhận'
test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[8]/td[2]/table/tbody/tr/td[1]/input').send_keys(output)

time.sleep(4)
# Bấm vào button "Đăng ký"
test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[9]/td[2]/input').click()
