import requests, webbrowser
from bs4 import BeautifulSoup
from tabulate import tabulate

def google_search(query):
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    links = []
    number = 0
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = (number,title)
            results.append(item)
            links.append(link)
            number+=1
    print(tabulate(results, headers=['Sl.No.','Title']))
    enquiry = input("Please Enter Sl.No. of Website you want to visit : ")
    get_link = links[int(enquiry)]
    return get_link

if __name__ == '__main__':
    query = input("Enter what you want to search: ")
    website = google_search(query)    
    webbrowser.open(website, new=2)