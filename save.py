import csv

def save_to_file(company, jobs):
    file_name = company["name"].replace("/", " ")
    file = open(f"export/{file_name}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])

    for job in jobs:
        writer.writerow(list(job.values()))

    return