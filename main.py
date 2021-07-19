from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you dont know")
unmatched_skills = input('>')
print(f'Filtering out {unmatched_skills}')

data_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=django&txtLocation=&cboWorkExp1=0').text


def find_jobs():
    soup = BeautifulSoup(data_text, 'lxml')
    items = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, item in enumerate(items):
        publish_date = item.find('span', class_='sim-posted').text
        if 'few' in publish_date:
            job_title = item.find('h2').text.replace('  ', '')
            company_name = item.find(
                'h3', class_='joblist-comp-name').text.replace('  ', '')
            skills = item.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = item.header.h2.a['href']
            if unmatched_skills not in skills:
                with open(f'jobs/{index}.txt', 'w') as file:
                    file.write(f"Job Title: {job_title.strip()} \n")
                    file.write(f"Company Name: {company_name.strip()} \n")
                    file.write(f"Required Skills: {skills.strip()} \n")
                    file.write(f"More Info: {more_info} \n")
                print(f'File saved on {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} Minuites...')
        time.sleep(time_wait * 60)
