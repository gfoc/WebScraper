from bs4 import BeautifulSoup
import requests
html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_file,'lxml')

jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span',class_ = 'sim-posted').text
    if "few" in published_date:
        company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(" ","")
        skills = job.find('span',class_ = 'srp-skills').text.replace(" ","")
        

        print(f"""
        Company Name: {company_name}
        skills Required: {skills}
        Published Date: {published_date}
        """)

        print("----------------------------------------------")





