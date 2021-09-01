from urllib.request import urlopen as uReq, Request
from bs4 import BeautifulSoup as soup

def steam_store(app_link):
    starting_url = "https://store.steampowered.com"
    # cookies = {'birthtime': '568022401', 'mature_content': '1' }
    link = starting_url + app_link
    print(link)
    url = Request(link, headers={'User-Agent': 'Mozilla/5.0', 'Cookie':"birthtime=568022401"})
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    container = page_soup.find_all("ul")
    # print(container)
        # looper = container.find_all("li")
        
        # print(len(container.find_all("li")))
        # print(len(looper))
    for n in range(len(container)):
        looper = container[n].find_all("li")
        for i in range(len(looper)):
            # print(looper[i].get_text())
            searcher = looper[i].get_text().split(":")
            if(searcher[0] == "Storage" or searcher[0] == "Hard Disk Space" or searcher[0] == "Hard Drive"):
                return "Storage:" + searcher[1]
                # print(looper[i])
                # print(i)
                # print(container.find_all("li")[i])
                # return container.find_all("li")[i-1].get_text()
        # space = container.find_all("li")[x].get_text()
        
        # return space

# def test_app(my_url,gamelist):
#     uClient = uReq(my_url)

#     page_html = uClient.read()

#     uClient.close()
    
#     page_soup = soup(page_html, "html.parser")
#     containers = page_soup.tbody.findAll("tr")
#     f_con = containers[24]
#     app_link = f_con.find_all("td")[1].a["href"]
#     space = steam_store(app_link)
#     title = f_con.find_all("td")[1].a.string.strip()
#     current_players = f_con.find_all("td")[2].string.strip()
#     peak_players = f_con.find_all("td")[4].string.strip()
#     hours_played = f_con.find_all("td")[5].string.strip()
#     gamelist.append([title,current_players,peak_players,hours_played,space])
#     return gamelist

def connect_web(my_url,gamelist):
    uClient = uReq(my_url)

    page_html = uClient.read()

    uClient.close()
    
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.tbody.findAll("tr")

    for container in containers:
        f_con = container
        app_link = f_con.find_all("td")[1].a["href"]
        space = steam_store(app_link)
        title = f_con.find_all("td")[1].a.string.strip()
        current_players = f_con.find_all("td")[2].string.strip()
        peak_players = f_con.find_all("td")[4].string.strip()
        hours_played = f_con.find_all("td")[5].string.strip()
        gamelist.append([title,current_players,peak_players,hours_played,space])
    return gamelist

def write_to_file(gamelist):
    filename = "games.csv"
    f = open(filename, "w", encoding="utf-8")
    headers = "Game Title , Current Players , Peak Players , Total Hours Played , Space\n"
    f.write(headers)
    for i in range(len(gamelist)):
        space = gamelist[i][4]
        if(space is None):
            print("Skipped")
        else:
            title = gamelist[i][0]
            current_players = gamelist[i][1]
            peak_players = gamelist[i][2]
            hours_played = gamelist[i][3]
            f.write(title + "," + current_players + "," + peak_players + "," + hours_played + "," + space + "\n")

    f.close()

gamelist = []
f_url = Request('https://steamcharts.com/top', headers={'User-Agent': 'Mozilla/5.0'})
connect_web(f_url,gamelist)
# print(gamelist)
# test_app(f_url,gamelist)
# print(gamelist)
for i in range(2,10):
    link = 'https://steamcharts.com/top'+'/p.'+str(i)
    print(link)
    url = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    connect_web(url,gamelist)

write_to_file(gamelist)


