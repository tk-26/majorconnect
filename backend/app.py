import requests
from bs4 import BeautifulSoup
import json

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

URL = 'https://www.gobankingrates.com/money/jobs/best-jobs-america/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#Job titles

job_titles = soup.find_all(['div','h2'],class_='listicle--slide--title')
parsed_job = [job.text.strip() for job in job_titles]
job_titles = [] #List of job titles
for element in parsed_job:
	detach_job_and_ranking = element.split('. ',1)
	final_job = detach_job_and_ranking[1]
	job_titles.append(final_job)

#Salaries

salary_start = soup.find_all('b')
salaries = [] #List of all salaries
for salary in salary_start:
	final_salary = salary.next_sibling
	salaries.append(final_salary)

#Job descriptions

job_descriptions = []
table = soup.find_all('div',class_='listicle--slide--content')
for x in table:
	job_descriptions.append(x.find('p').text)


combined_list = []
for job, salary, job_description in zip(job_titles,salaries,job_descriptions):
	combined_list.append(dict(job_title = job, salary = salary, job_description = job_description))

final_json = json.dumps(combined_list)
JOB_DATA = json.loads(final_json)

@app.route('/job_data', methods=['GET'])
def all_job_data():
    return jsonify({
        'status': 'success',
        'job_data': JOB_DATA
    })

app.run()