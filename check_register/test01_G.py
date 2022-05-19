from select import select
import  time
from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


test_driver = webdriver.Chrome()
test_driver.maximize_window()

# Di chuyển đến địa chỉ "http://hamsterbabali.com/"
test_driver.get('http://hamsterbabali.com/')

test_driver.implicitly_wait(4)          #chờ ngầm định


# Bấm vào button "Đăng ký"
test_driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/li[1]/a').click()
time.sleep(1)
# Nhập dữ liệu vào field 'email'
test_driver.find_element(By.CSS_SELECTOR, '#reg_email').send_keys('nhi2342@gmail.com')
time.sleep(1)
# Nhập dữ liệu vào field 'password'
test_driver.find_element(By.CSS_SELECTOR, '#reg_password').send_keys('hoangnhi123')
time.sleep(1)
# Nhập dữ liệu vào field 'họ tên'
test_driver.find_element(By.CSS_SELECTOR, '#reg_hoten').send_keys('Hoàng Nhi')
time.sleep(1)
# select box "giới tính" và chọn giới tính Nữ
gioiTinh = Select(test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[4]/td[2]/select'))
# select by value
gioiTinh.select_by_value('0')
time.sleep(1)
# Nhập dữ liệu vào field 'tìm kiếm'
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
# Nhập dữ liệu vào field 'mã xác nhận'
test_driver.find_element(By.CSS_SELECTOR, '#reg_killbomb').send_keys('1234')
time.sleep(1)
# Bấm vào button "Đăng ký"
test_driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/center/div/div/div/form/div/table/tbody/tr[9]/td[2]/input').click()


#tắt testcase
# test_driver.close()
# test_driver.quit()