import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/career-advice/finding-a-job/majors-in-demand'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

majors = []
individual_major = soup.find_all(['div','h3'],class_='styles-module--contentSection--_QWYk styles-module--heading--1dbu_')
for major in individual_major:
	final_major = major.find('h3')
	if final_major != None:
		stripped_major = final_major.text
		split_number = stripped_major.split('. ',1)
		majors.append(split_number[1])

descriptions = [] 
major_descriptions = soup.find_all('p',class_='styles-module--contentSection--_QWYk')
for major_description in major_descriptions:
	description = major_description.text
	trim_description = description.split('include ',1)
	almost_final_description = trim_description[0]
	if 'Read more' in almost_final_description:
		remove_read_more = almost_final_description.split('Read more',1)
		descriptions.append(remove_read_more[0])
	elif ('Some careers for nursing majors include' and 'Related') not in almost_final_description:
		descriptions.append(almost_final_description)

descriptions_stripped = [description for description in descriptions if not ('Some of the most in-demand majors include:' in description or 'Related job titles include:' in description or 'What you choose for your college major' in description or 'planning your college career, learning about' in description or 'Some careers for nursing majors include' in description)]
final_descriptions = [i for i in descriptions_stripped if i]

combined_list = []
for major, description in zip(majors, final_descriptions):
	combined_list.append(dict(major = major, description = description))

print(combined_list)