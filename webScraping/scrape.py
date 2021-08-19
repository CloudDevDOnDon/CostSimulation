from urllib.request import urlopen as uReq, Request
from bs4 import BeautifulSoup as soup

def connect_web(my_url,gamelist):
    uClient = uReq(my_url)

    page_html = uClient.read()

    uClient.close()
    
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.tbody.findAll("tr")

    for container in containers:
        f_con = container
        title = f_con.find_all("td")[1].a.string.strip()
        current_players = f_con.find_all("td")[2].string.strip()
        peak_players = f_con.find_all("td")[4].string.strip()
        hours_played = f_con.find_all("td")[5].string.strip()
        gamelist.append([title,current_players,peak_players,hours_played])
    return gamelist

def write_to_file(gamelist):
    filename = "games.csv"
    f = open(filename, "w", encoding="utf-8")
    headers = "Game Title , Current Players , Peak Players , Total Hours Played \n"
    f.write(headers)
    for i in range(len(gamelist)):
        title = gamelist[i][0]
        current_players = gamelist[i][1]
        peak_players = gamelist[i][2]
        hours_played = gamelist[i][3]
        f.write(title + "," + current_players + "," + peak_players + "," + hours_played + "\n")

    f.close()

gamelist = []
f_url = Request('https://steamcharts.com/top', headers={'User-Agent': 'Mozilla/5.0'})
connect_web(f_url,gamelist)
for i in range(2,10):
    link = 'https://steamcharts.com/top'+'/p.'+str(i)
    print(link)
    url = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    connect_web(url,gamelist)

write_to_file(gamelist)


