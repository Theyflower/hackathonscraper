#!/usr/bin/python
import mechanicalsoup
from BeautifulSoup import BeautifulSoup as soup

browser = mechanicalsoup.Browser()

def populate_pagelist(page):
	'''
	how do i docstrings good?
	takes a page and then gives you an int list of the pages containing data we need to scrape aw yeah
	'''

	the_div = soup(page.soup.find('div', class_='pagination'))
#	links = the_div.soup.find_all('a')
	print(the_div)
	#pagination is the classname of stuff

	return range(10)#this is temporary

def populate_hackathonlist(pdagedata):
	'''
	takes a page and then scrapes all the hackathons from it and then puts them into a list or dictionary or something
	its gonna be awesome
	'''
	pass


base_url = "https://devpost.com/hackathons?utf8=✓&search=&challenge_type=in-person&sort_by=Submission+Deadline&page="
maxpage = 9001 #this script will break if there are over nine thousand pages of hackathons

#make sure maxpage is higher than the amount of pages there actually are
 
current_url = "{}{}".format(base_url,maxpage) #classname pagination has the page 
current_page = browser.get(current_url)

#populate a list of pages

pages = populate_pagelist(current_page) #gvn is an acronum for good variable name #todo(aaron) make up a better one

for page in pages:
	current_url = "{}{}".format(base_url,page)
	#get the page
	#scrape it good