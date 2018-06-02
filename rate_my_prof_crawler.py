# from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import re
from ast import literal_eval

root = 'http://www.ratemyprofessors.com/ShowRatings.jsp?tid='

def basic_info(soup):
	prof = dict()
	script = soup.select('script')[3].text
	info_dict = re.search(
		'pageLevelData:\s({.+}),\s*reloadInterval:', 
		script).group(1)
	basic_info = literal_eval(info_dict)

	prof['name'] = basic_info['prop7']
	prof['school'] = basic_info['prop6']
	prof['school_id'] = basic_info['schoolid']
	prof['subject'] = basic_info['prop3']

	# fname = soup.select('span.pfname')[0].get_text().strip()
	# mname = soup.select('span.pfname')[1].get_text().strip()
	# lname = soup.select('span.plname')[0].get_text().strip()
	# # name = lambda _: print(fname+lname) if mname=='' else print(fname+mname+lname)
	# # print(name)
	
	# if mname == '':
	# 	name = fname+' '+lname 
	# else: 
	# 	name = fname+' '+mname+' '+lname
	# print(name)

	school = soup.select('h2.schoolname')[0].get_text().split(',')
	prof['city'] = school[1].strip()
	prof['state'] = school[2].strip()

	return prof

def get_prof_info(prof_id):
	prof = dict()
	page = requests.get(root+str(prof_id))
	html = page.text
	soup = BeautifulSoup(html, 'html.parser')

	# basic_info = name_and_school(soup)
	
	prof = basic_info(soup)
	prof['id'] = prof_id




	return prof
	# return type(basic_info)
	

print(get_prof_info(1862614))