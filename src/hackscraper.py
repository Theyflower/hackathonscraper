#!/usr/bin/python
import mechanicalsoup
from bs4 import BeautifulSoup as soup

browser = mechanicalsoup.Browser()

def populate_pagelist(page):
	'''
	how do i docstrings good?
	takes a page and then gives you an int list of the pages containing data we need to scrape aw yeah
	'''
	the_div = page.soup.find('div', class_='pagination') #finds the div that has the links with data we want
	links = the_div.findAll('a') #gets the links
	links = [int(link.string) for link in links if link.string is not None] #extracts the number from them, one of them is None so we do the is not None
	return links #yatta

def scrape_hackathon(pdagedata):
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

hackathons = []
for page in pages:
	current_url = "{}{}".format(base_url,page)
	hackathons.append(scrape_hackathon(page))
	#get the page
	#scrape it good