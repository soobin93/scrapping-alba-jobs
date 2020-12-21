import requests
from bs4 import BeautifulSoup

def extract_jobs(url):
    formatted_url = url.replace("/job/brand", "")

    print(f"URL: {formatted_url}job/brand/?page=1&pagesize=10000")
    response = requests.get(f"{formatted_url}job/brand/?page=1&pagesize=10000")
    soup = BeautifulSoup(response.text, "html.parser")

    container = soup.find("div", {"id": "NormalInfo"})
    
    if container is not None:
        job_table = container.find("table")
        jobs_a = job_table.find("tbody").find_all("tr", {"class": ""})
        jobs_b = job_table.find("tbody").find_all("tr", {"class": "divide"})
        jobs = jobs_a + jobs_b
    else:
        jobs = []

    return jobs
   
def extract_job(html):
    job_place = html.find("td", {"class": "first"}).get_text()
    job_title = html.find("td", {"class": "title"}).find("span", {"class": "company"}).get_text()
    job_time = html.find("td", {"class": "data"}).get_text()
    job_pay = html.find("td", {"class": "pay"}).get_text()
    job_date = html.find("td", {"class": "regDate"}).get_text()

    return {
        "place": job_place,
        "title": job_title,
        "time": job_time,
        "pay": job_pay,
        'date': job_date
    }

def get_jobs(company):
    print(f"Scrapping jobs for {company['name']}")

    job_list = []
    jobs = extract_jobs(company["link"])
    print(f"->Found {len(jobs)} jobs")

    for job_html in jobs:
        if len(job_html.find_all("td")) > 1:
            job = extract_job(job_html)
            job_list.append(job)

    return job_list