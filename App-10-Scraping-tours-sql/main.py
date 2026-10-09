import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    """Scrape the page source from the url"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    selector = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = selector.extract(source)["tours"]
    return value


if __name__ == "__main__":
    scraped_data = scrape(URL)
    extracted_data = extract(scraped_data)
    print(extracted_data)