import requests
from Send_Email import send_email

api_key = "890603a55bfa47048e4490069ebee18c"

url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={api_key}&language=en"

#Make a Request
request = requests.get(url)

#Get the json content from the request
content = request.json()

body = ""

for article in content['articles'][:20]:
    body += "Subject: Todays News\n" f"Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}\n\n"
    
body = body.encode('utf-8')

send_email(message=body)