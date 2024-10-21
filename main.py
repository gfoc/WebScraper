from bs4 import BeautifulSoup
import requests
import time


# Prompt the user for unfamiliar skills
print("Put some skills that you are not familiar with:")
unfamiliar_skills = input(">").lower()  # Convert to lowercase for case-insensitive matching
print(f"Filtering out jobs requiring {unfamiliar_skills}")

def get_jobs():
    html_file = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
    ).text
    soup = BeautifulSoup(html_file, 'lxml')

    # Find all job postings
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text

        # Only show jobs that are posted recently (based on "ago" in the date string)
        if "few" in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()  
            skills = job.find('span', class_='srp-skills').text.lower().strip()  

            # Extract the job link for more details
            more_info = job.header.a['href']

            # Only show jobs that don't require the unfamiliar skills
            if unfamiliar_skills not in skills:
                with open(f'Post/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name} \n")
                    f.write(f"Skills Required: {skills} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f"Files Saved at: {index}")


if __name__ == "__main__":
    while True:
        get_jobs()
        wait_time = 15
        print(f"Waiting Time is { wait_time } minutes")
        time.sleep(60*wait_time)
  


