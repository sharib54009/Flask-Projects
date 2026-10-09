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


def Send_Email():
    print("Email has been sent!")
    

def store(extracted_data):
    with open("data.txt", "a") as file:
        file.write(extracted_data + "\n")
    print("Data has been stored in data.txt")
    
def read(extracted_data):
    with open("data.txt", "r") as file:
        data = file.read()
    return data


if __name__ == "__main__":
    scraped_data = scrape(URL)
    extracted_data = extract(scraped_data)
    print(extracted_data)
    content = read(extracted_data)
    if extracted_data != "No upcoming tours":
        if extracted_data not in content:
            store(extracted_data)
            Send_Email()