from selenium import webdriver
import requests
import bs4
import os
import time

browser = webdriver.Firefox(executable_path=r'C:\Users\mathew\Documents\geko\geckodriver.exe')
browser.get("https://soundcloud.com/")

time.sleep(2) 

#method creation

def automatic_heart(genre):
	global like_speed, like_count
	url = ('https://soundcloud.com/search/sounds?q=' + genre + '&filter.created_at=last_hour')
	browser.get(url)
	print("searching genre ", genre_inp)
	print('liking posts')
	try:
		for like_index in range(2, like_count):
			like_url = ('li.searchList__item:nth-child(' + str(like_index) + ') > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
			like_element = browser.find_element_by_css_selector(like_url)
			time.sleep(0.5)
			like_element.click()
			time.sleep(0.5)
			browser.execute_script('arguments[0].scrollIntoView(true);', like_element) 
			time.sleep(like_speed)
	except:
		print("dont manipulate with the window or not enough posts")


#var

like_count = 50
like_speed = 1
loggin_indicator = False
genre_inp = "house"


#element assignment

signin_element = browser.find_element_by_css_selector('.frontHero__loginButton')


#action

signin_element.click()

print('please login using gmail or facebook')

time.sleep(2)

while loggin_indicator == False:
	if browser.current_url == "https://soundcloud.com/discover":
		print("youre now logged in")
		loggin_indicator = True

browser.maximize_window()

automatic_heart(genre_inp)

print("finished liking posts")

