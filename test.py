import sys
import io
from selenium import webdriver


driver = webdriver.Chrome(r'C:\\dev\\Chromedriver\\chromedriver.exe')
# 크롬드라이버 있는 곳 

driver.implicitly_wait(5)

driver.get('http://localhost:8280/kbn/login/login.do') # 로그인 페이지
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input').send_keys('counsel1') # 비밀번호 입력

driver.find_element_by_xpath('//*[@id="loginForm"]/button').click()     # 로그인 버튼 클릭

driver.get('http://localhost:8280/kbn/sell/applyMain.do?authCode=counsel') # 사진찍을 페이지 

driver.save_screenshot("C:\\dev\\test/website1.png") # 사진 저장위치

driver.implicitly_wait(5) #기다림 

driver.quit() # 종료 

