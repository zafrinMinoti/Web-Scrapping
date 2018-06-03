# from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import re
from ast import literal_eval

root = 'http://www.ratemyprofessors.com/ShowRatings.jsp?tid='

def basic_info(soup):
	basic = dict()
	script = soup.select('script')[3].text
	info_dict = re.search(
		'pageLevelData:\s({.+}),\s*reloadInterval:', 
		script).group(1)
	basic_info = literal_eval(info_dict)

	basic['name'] = basic_info['prop7']
	basic['school'] = basic_info['prop6']
	basic['school_id'] = basic_info['schoolid']
	basic['subject'] = basic_info['prop3']

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
	basic['city'] = school[1].strip()
	basic['state'] = school[2].strip()

	return basic

def quality_info(soup):
	quality = dict()
	all_qualities = soup.select('div.grade')
	quality['overall_quality'] = all_qualities[0].get_text().strip()
	quality['take_again'] = all_qualities[1].get_text().strip()
	quality['level_of_difficulity'] = all_qualities[2].get_text().strip()
	# quality['hotness'] = re.search('chilis(.+)\.png', str(all_qualities[3])).group(1)
	# quality['hotness'] = str(all_qualities[3])
	# print(type(quality['hotness']))
	# hotness = soup.find_all('figure', text='chilis')
	hotness = re.search('chilis/(.+)\.png', str(soup)).group(1)
	# print(hotness)
	# print(type(hotness))
	quality['hotness'] = hotness

	return quality

def tags(soup):
	raw_tags = soup.select('span.tag-box-choosetags')
	tags = dict()
	for tag in raw_tags:
		tag = tag.get_text().strip()
		tag_key = tag[:-4].strip().lower()
		tag_count = tag[-2]
		tags[tag_key] = tag_count
	return tags

def student_ratings(soup):
	review_soup = soup.select('div.table.tr')

def get_prof_info(prof_id):
	prof = dict()
	# page = requests.get(root+str(prof_id))
	# html = page.text
	fhand = open('tippit.html')
	html = fhand.read()
	soup = BeautifulSoup(html, 'html.parser')
	
	prof['id'] = prof_id
	prof.update(basic_info(soup))
	prof.update(quality_info(soup))
	prof.update(tags(soup))

	rating_count = soup.select(
		'div.table-toggle')[0].get_text().strip().split()[0]
	print(rating_count)
	print()
	review_soup = soup.select('td.rating')
	print(len(review_soup))
	print(type(review_soup))
	bs = BeautifulSoup(review_soup[0].get_text(), 'html.parser')
	print()
	print(type(bs))
	print(bs)
	print()

	return prof
	# return type(basic_info)
	

print(get_prof_info(1862614))