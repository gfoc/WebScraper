from bs4 import BeautifulSoup
import requests

html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
#print(html_file)

soup = BeautifulSoup(html_file,'lxml')

job_card = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')

for job_desc in  job_card:
    company_name = job_desc.h3.text
    skills_req = soup.find_all('span',class_ = 'srp-skills').text
    print(f'{company_name} with skills required {skills_req}')
