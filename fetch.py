import requests
from bs4 import BeautifulSoup

data = requests.get('https://stackexchange.com/leagues/1/alltime/stackoverflow/2008-07-31?sort=reputationchange&pagesize=50')
soup = BeautifulSoup(data.text, 'html.parser')

leaderboard = soup.find('div', {'id': 'leagueUserList'})
stats = leaderboard.find_all('span', {'class': 'number'})

for tag in stats:
    print(tag.text.strip())

names = leaderboard.find_all('h2')
for tag in names:
    print(tag.text.strip())

date = leaderboard.find_all('span', {'class':'faintText'})
for tag in date:
    print(tag.text.strip())



# print(*stats[0::1], sep = '\n')
# print(*stats[1::2], sep = '\n') # Only gets the data from second span
