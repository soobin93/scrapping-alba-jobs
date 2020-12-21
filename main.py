import os
from company import get_companies
from job import get_jobs
from save import save_to_file

os.system("clear")

companies = get_companies()

for company in companies:
    jobs = get_jobs(company)
    print("")

    save_to_file(company, jobs)
