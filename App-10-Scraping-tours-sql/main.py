import requests
import selectorlib
import smtplib

URL = "http://programmer100.pythonanywhere.com/tours/"


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    selector = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = selector.extract(source)["tours"]
    return value


def Send_Email(message):
    username = "app8flask@gmail.com"
    password = "ptcr fbbs qxyo lbzx"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(username, password)
    server.sendmail(username, username, message)

    server.quit()
    print("Email sent successfully")

def store(extracted_data):
    with open("data.txt", "a") as file:
        file.write(extracted_data + "\n")
    print("Data has been stored in data.txt")


def read():
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scraped_data = scrape(URL)
    extracted_data = extract(scraped_data)
    print(extracted_data)

    content = read()

    if extracted_data != "No upcoming tours":
        if extracted_data not in content:
            store(extracted_data)
            Send_Email("Hey, a new event was found: " + extracted_data)


    
    
    

