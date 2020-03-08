from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys												#								----copied above part-----------			
import time
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options
opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode ----> remove this line if assertion error is thrown
browser = Chrome('C:\\Users\\suraj\\Desktop\\usb\\Found files\\Lost partition 0\\suraj\\selenium\\chromedriver.exe')
browser.get('https://quora.com')



#login part
email = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[1]/input')
email.clear()
email.send_keys('surajyadav0149@gmail.com')
password = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/input')
password.clear()
password.send_keys('2Aug@Sd0')
time.sleep(1)
login = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[3]/input')
login.click()
time.sleep(3)


#asking question
failed=[]
f = open('/home/suraj/selenium/q.txt','r')
l = f.read().splitlines()
#console.write(l)
for q in l:
	
		q+=' '
		question = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div/div')
		question.click()
		time.sleep(3)
		#make it private
		try:
			lim = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div[1]/div/div/div[2]/div/div/div")
			lim.click()
			time.sleep(1)
			pr = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div[1]/div")
			pr.click()
			time.sleep(1)
			#private till here
		except:
			pass
		qa = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/textarea")
		time.sleep(2)
		qa.clear()
		qa.send_keys(q)	#question content
		add = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div/span[2]/a")
		add.click()
		time.sleep(5)
		#suggestion click
		s1 = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div/span[2]/a")
		s1.click()
		time.sleep(6)
		try:
			#next button
			next = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div/span[2]/a/div")
			next.click()					#done button
			time.sleep(2)
			alert = browser.switch_to.alert
			alert.accept()
			time.sleep(7)
			for i in range(1,25):
				pa = "/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div["+str(i)+"]/div/div/div/div[2]/div/div[2]/div/a/div/div/div"
				rb = browser.find_element_by_xpath(pa)
				rb.click()
				time.sleep(0.2)
			done = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div[1]/span[2]/a/div/div")
			done.click()
			time.sleep(2)
			#exception
			action = webdriver.common.action_chains.ActionChains(browser)
			ac = browser.find_element_by_xpath("/html/body")
			action.move_to_element_with_offset(ac,80,200)
			action.click()
			action.perform()
			time.sleep(2)
		except:
			failed.append(q)
			#print(sys.exc_info()[0])
			action = webdriver.common.action_chains.ActionChains(browser)
			ac = browser.find_element_by_xpath("/html/body")
			action.move_to_element_with_offset(ac,80,80)
			action.click()
			action.perform()
			time.sleep(2)
print(failed)

