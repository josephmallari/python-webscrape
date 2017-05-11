import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.residentadvisor.net/events.aspx")
soup = BeautifulSoup(page.content, 'html.parser')
event_id = soup.find(id="event-listing")

for text in event_id.select('h1 > a:nth-of-type(1)'):
	print(text.get_text())

print event_items
