#!/usr/bin/env python3
"""
congratulations, you are reading my code
there are a LOT of REALLY BADly named variables
if you think you know a better name for a variable then you are probably right
please fork this repo and make a pull request with refactored code

also make good docstrings because idk how to do that
"""
import mechanicalsoup
import copy
import json
#from bs4 import BeautifulSoup as soup #might actually not need this

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
			if 'current_hackathon' in locals():
				hackathon_data.append(current_hackathon)
			current_hackathon = []
		current_hackathon.append(tag)

	#yeah so the variable current_hackathon is going to be repurposed
	#if you have good ideas for better variable names please refactor my code
	#i will accept pull requests that improve variable names
	for hackathon_tags in hackathon_data:
		current_hackathon = copy.deepcopy(hackathon_template)
		for tag in hackathon_tags:#i will be the first to admit that this is not a particularly fast algorithm
									#if you make pull request with a faster one I will craciously accept it
			if " ".join(tag['class']) == 'title':
				name = tag.string.strip()
				current_hackathon['name'] = name
				print(current_hackathon['name'])

			elif " ".join(tag['class']) == 'challenge-location':
				location = tag.contents[2].strip()
				current_hackathon['location'] = location
				print(str(current_hackathon['location']))

			elif " ".join(tag['class']) == "value date-range":
				date = tag.string.strip()
				if '–' in date:
					date = [i.strip() for i in date.split('–')]
				else:
					date = [date, "NO_END_DATE"]
				current_hackathon['date'] = date
				print(current_hackathon['date'])

			elif " ".join(tag['class']) == "challenge-description":
				desc = tag.string.strip()
				desc = desc.replace("________________________________________________","")
				#this line is bad and hardcoded crap
				#@todo(aaron) use regex to make a good thing "__+" <- that's the regex
				if desc == '':
					desc = "ERROR_PARSING_DESCRIPTION"
				current_hackathon['desc'] = desc
				print(current_hackathon['desc'])

			elif " ".join(tag['class']) == "thumbnail_image image-replacement":
				logo = "{}".format(tag['src'].replace("//","").replace("https:",""))
				current_hackathon['logo'] = logo
				print(current_hackathon['logo'])
		print()
		hackathons.append(current_hackathon)
	return hackathons

def scrape():
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
	return json.dumps(hackathons, sort_keys=True, indent=4)

def jsondump():
	f = open('hackathons.JSON', 'w')
	f.write(json.dumps(scrape(), sort_keys=True, indent=4))
	f.close
