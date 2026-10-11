import time
import sqlite3
import requests
import selectorlib
import smtplib


connection = sqlite3.connect("data.db")


cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        band TEXT,
        city TEXT,
        date TEXT
    )
""")

connection.commit()


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
    row = extracted_data.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()


def read(extracted_data):
    row = extracted_data.split(" ")
    row = [item.strip() for item in row]
    band, city, date = row[0], row[1], row[2]
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? and city =? and date =? ", (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return rows
    
   

if __name__ == "__main__":
    while True:
        scraped_data = scrape(URL)
        extracted_data = extract(scraped_data)
        print(extracted_data)

       

        if extracted_data != "No upcoming tours":
            row = read(extracted_data)
            if not row:
                store(extracted_data)
                Send_Email("Hey, a new event was found: " + extracted_data)
        time.sleep(3)        


    
    
    

