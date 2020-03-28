from background_task import background
import requests
from bs4 import BeautifulSoup
from users.models import Users, Document, Searches
import json
@background(schedule=60)
def search_task(message):
    user = Users.objects.get(pk=message)
    query = user.first_name+"+"+user.last_name
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
            search = Searches(result='google',title=title, link=link, user=user)
            search.save()
    