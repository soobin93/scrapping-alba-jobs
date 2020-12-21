import requests
from bs4 import BeautifulSoup

URL = "http://www.alba.co.kr"

def extract_companies():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    super_brands = soup.find("div", {"id": "MainSuperBrand"})
    company_container = super_brands.find("ul", {"class": "goodsBox"})
    return company_container.find_all("li", {"class": "impact"})

def extract_company(html):
    company_header = html.find("a", {"class": "goodsBox-info"})
    company_name = company_header.find("span", {"class": "company"}).get_text()
    company_link = company_header["href"]

    return {
        "name": company_name,
        "link": company_link
    }

def get_companies():
    company_list = []
    companies = extract_companies()

    for company_html in companies:
        company = extract_company(company_html)
        company_list.append(company)

    return company_list