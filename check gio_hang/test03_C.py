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

#scroll down
test_driver.execute_script("window.scrollBy(0,480)","")
time.sleep(1)
# Bấm vào button "Mua"
test_driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[6]/div[1]/div[2]/div/div[1]/li[1]/div/div[2]/a[1]').click()
time.sleep(1)
# Bấm vào button "Xem giỏ hàng"
test_driver.find_element(By.XPATH,'/html/body/div[12]/div[2]/div/center/div/div[2]/center/div[2]/a').click()
time.sleep(1)
# Bấm vào select box "Số lượng" và chon option có value "2" trong giỏ hàng
select = Select(test_driver.find_element(By.XPATH, '/html/body/div[4]/div/div[5]/div/div[2]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]/div/select'))
# select by value
select.select_by_value('2')
time.sleep(1)
#scroll down
test_driver.execute_script("window.scrollBy(0,480)","")

#tắt testcase
# test_driver.close()
# test_driver.quit()