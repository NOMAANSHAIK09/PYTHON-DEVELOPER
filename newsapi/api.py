#libraris for api request
import requests
from send_email import send_email
#my api  key from newsapi.org

my_api="9cf3caebb00d4a15be0e660490ac3309"

url="https://newsapi.org/v2/everything?q=tesla&from=2025-09-12&sortBy=publishedAt&apiKey=9cf3caebb00d4a15be0e660490ac3309&language=en"
#make request
request=requests.get(url)
# to get distonaris
content=request.json()
# access the article titles and discription
body=""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body= "subject: Today's news"+"\n"+body+article["title"] + "\n" + article["description"] + "\n"+ article["url"]+ 2*"\n"
body=body.encode("utf-8")
send_email(message=body)