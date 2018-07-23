# -*- coding: utf-8 -*-

# Use CTR-SHIFT-c to bring up webpage inspector (firefox) to find id/name/etc.
# Selenium keys: https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def selenium_button_action (button_name,action):
		# buttons = driver.find_elements_by_xpath("//*[contains(text(), 'April 2018')]")
		buttons = driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(button_name))
		buttons.clear()
		print(button_name," (num): ",len(buttons))
		assert len(buttons) == 1,"Found zero/multiple ("+str(len(buttons))+") buttons"
		for btn in buttons:
			if (action == "click"):
				btn.click()
			else:
				raise ValueError("Undefined button action.")
			time.sleep(1)

if __name__ == "__main__":
	driver = webdriver.Firefox()

	web_type = "b2"

	if (web_type == "p"):
		driver.get("http://www.python.org")
		assert "Python" in driver.title
		# elem = driver.find_element_by_name("q")
		elem = driver.find_element_by_id("id-search-field")
		time.sleep(1)
		elem.clear()
		elem.send_keys("pycon")
		time.sleep(1)
		elem.send_keys(Keys.RETURN)
		time.sleep(1)
		assert "No results found." not in driver.page_source
		time.sleep(1)
		driver.close()
	elif (web_type == "b"):
		driver.get("https://www.barchart.com/etfs-funds/quotes/xsp.to/price-history/historical")
		elem = driver.find_element_by_class_name("bc-datepicker-control")
		time.sleep(5)

		elem.clear()
		elem.send_keys(Keys.LEFT)
		time.sleep(1)

		selenium_button_action("April 2018","click")
		selenium_button_action("2018</strong>","click")
		selenium_button_action("2016","click")
	elif (web_type == "b2"):
		driver.get("https://www.barchart.com/etfs-funds/quotes/xsp.to/price-history/historical")
		elem = driver.find_element_by_name("dateFrom")
		elem.clear()
		elem.send_keys(Keys.LEFT)

		print("should have clicked. sleeping (4)")
		time.sleep(4)


	driver.close()
