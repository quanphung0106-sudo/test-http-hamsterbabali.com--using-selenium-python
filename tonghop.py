from select import select

from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

# Di chuyển đến địa chỉ "https://vlogtruyen.net"
test_driver.get('http://hamsterbabali.com/')

test_driver.implicitly_wait(4)          #chờ ngầm định

# Nhập dữ liệu vào ô 'tìm kiếm'
test_driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/div[2]/div/form/div[1]/input').send_keys('Toàn')


# Bấm vào button "tìm kiếm"
test_driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/div[2]/div/form/div[1]/div[2]/button').click()

# select box
theloai = select(test_driver.find_element(By.XPATH, '/html/body/div[5]/form/div[1]/select'))
theloai.select_by_index(2)


#lấy dữ liệu từ list
testXpath = test_driver.find_elements(By.XPATH, '/html/body/div[6]/div[2]/ul/li')
for testXpaths in testXpath:
    try:
        TenTruyen = testXpaths.find_element(By.XPATH, 'a[2]/h3').text
        print('Tên truyện : ', TenTruyen)
    except NoSuchElementException:
        pass


#tắt testcase
# test_driver.close()
# test_driver.quit()