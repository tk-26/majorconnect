import requests
from bs4 import BeautifulSoup

URL = 'https://www.vault.com/best-jobs-and-career-guidance'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#Professions
professions = []
ulProfessions = soup.find_all(['ul','li'],class_='maxWide ArticleLinks')
parsed_job = [job.text.strip() for job in ulProfessions]
string_of_professions = ''.join(str(x) for x in parsed_job)


for job in string_of_professions.split('\n'):
	professions.append(job)

#Gets links to the individual pages
link_list = []
for item in ulProfessions:
	list_of_links = item.find_all('a',text=True)
	for link in list_of_links:
		stripped_link = link.get('href')
		link_list.append('https://www.vault.com/' + stripped_link)

#Individual profession info
salaries = []
job_descriptions = []
minimum_edu_levels = []
for link in link_list:
	individual_page = requests.get(link)
	soup_ip = BeautifulSoup(individual_page.content, 'html.parser')
	#Salary info
	salary_blob = soup_ip.find_all('strong')[0]
	salaries.append(salary_blob.text)
	#Job description
	job_description_blob = soup_ip.find_all('p',class_='blw default_cotent')
	for job_description in job_description_blob:
		stripped_job = job_description.text
		job_descriptions.append(stripped_job.replace('\n',''))
	#Minimum Education Level
	min_edu_blob = soup_ip.find_all('strong')[1]
	minimum_edu_levels.append(min_edu_blob.text)


combined_list = []
for job, salary, job_description, minimum_edu_level in zip(professions,salaries,job_descriptions,minimum_edu_levels):
	combined_list.append(dict(job_title = job, salary = salary, job_description = job_description, minimum_education_level = minimum_edu_level))

print(combined_list)