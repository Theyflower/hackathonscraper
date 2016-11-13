#!/usr/bin/python
"""
congratulations, you are reading my code
there are a LOT of REALLY BADly named variables
if you think you know a better name for a variable then you are probably right
please fork this repo and make a pull request with refactored code

also make good docstrings because idk how to do that
"""
import mechanicalsoup
from bs4 import BeautifulSoup as soup #might actually not need this

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

def scrape_hackathons(page):
	'''
	takes a page and then scrapes all the hackathons from it and then puts them into a list or dictionary or something
	its gonna be awesome
	the variable names in this
	'''
	hackathons = []
	desired_classnames = ["challenge-location","title","value date-range","challenge-description","thumbnail_image image-replacement"] 
	hackathon_template = {'name' : None, 'location' : None, 'desc': None, 'date' : {'start' : None, 'end' : None}, 'logo' : None	}
	#
	# hacksdata = page.soup.findAll('article',class_='challenge-listing')
	tags = page.soup.findAll(True, {'class':desired_classnames})

	ZERO_CLASS = tags[0]['class']
	hackathon_data = []
	for tag in tags:
		if tag['class'] == ZERO_CLASS:
			if 'curr_hackathon' in locals():
				hackathon_data.append(current_hackathon)
			current_hackathon = []
		current_hackathon.append(tag)

	#yeah so the variable current_hackathon is going to be repurposed
	#if you have good ideas for better variable names please refactor my code
	#i will accept pull requests that improve variable names

	for hackathon_tags in hackathon_data:
		current_hackathon = deepcopy(hackathon_template)
		print(hackathon_tags)

	return range(10) #this is temporary


base_url = "https://devpost.com/hackathons?utf8=✓&search=&challenge_type=in-person&sort_by=Submission+Deadline&page="
maxpage = 9001 #this script will break if there are over nine thousand pages of hackathons

#make sure maxpage is higher than the amount of pages there actually are
 
current_url = "{}{}".format(base_url,maxpage) #classname pagination has the page 
current_page = browser.get(current_url)

#populate a list of pages

pageids = populate_pagelist(current_page) #gvn is an acronum for good variable name #todo(aaron) make up a better one

hackathons = []
for pageid in pageids:
	current_url = "{}{}".format(base_url,pageid)
	page = browser.get(current_url)
	for hackathon in scrape_hackathons(page):
		hackathons.append(hackathon)
	#get the page
	#scrape it good

#write the data to a JSON file? how the heck does JSON work