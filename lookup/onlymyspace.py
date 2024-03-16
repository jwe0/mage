from requests_html import HTMLSession, AsyncHTMLSession

def is_valid(data):
    if "User not found" in data:
        print("[+] Invalid profile")
        return True
    else:
        return False



def get_links(data):
    for social in data.html.absolute_links:
        print("[+] Social scraped: {link}".format(link=social))

def get_id(data):
    for line in data.splitlines():
        if "const data =" in line:
            id = line.split("id")[1].split(",")[0].replace("\\", "").replace("\"", "").replace(":", "")
            print("[+] ID scraped: {link}".format(link=id))

def get_username(data):
    for line in data.splitlines():
        if "uname" in line:
            username = line.split("uname")[1].split(",")[0].replace("\\", "").replace("\"", "").replace(":", "")
            print("[+] Username scraped: {link}".format(link=username))

def get_pronouns(data):
    used = False
    for line in data.splitlines():
        if "pronnouns" in line:
            if used == True:
                pronouns = line.split("\"pronnouns")[1].split("textColor")[0].replace("\\", "").replace("\"", "").replace(":", "").replace(",", "")
                print("[+] Scraped pronouns: {link}".format(link=pronouns))
            else:
                used = True

def get_bio(data):
    for line in data.splitlines():
        if "const data = [" in line:
            bio = line.split("bio")[1].split("font")[0].replace("\\", "").replace("\"", "").replace(":", "").split("pfp")[0]
            print("[+] Scraped bio: {link}".format(link=bio))

def get_timezone(data):
    for line in data.splitlines():
        if "const data = [" in line:
            if "timezone" in line:
                    timezone = line.split("timezone")[1].split("displayTimezone")[0].replace("\\", "").replace("\"", "").replace(":", "").replace(",", "")
                    print("[+] Scraped timezone: {link}".format(link=timezone))

            

def get_pfp(data):
    for line in data.splitlines():
        if "const data = [" in line:
            pfp = line.split("pfp")[1].split("url")[1].split("no_border")[0].replace("\\", "").replace("\"", "").replace(":", "").replace(",", "").split("}")[0]
            print("[+] Scraped pfp: {link}".format(link=pfp))

def get_views(data):
    for line in data.splitlines():
        if "views" in line:
            views = line.split("views")[1].split(",")[0].replace("\\", "").replace("\"", "").replace(":", "")
            print("[+] Scraped views: {link}".format(link=views))

def get_badges(data):
    used = False
    for line in data.splitlines():
        if "badges" in line:
            if used == True:
                badges = line.split(",badges:[")[1].split("],")[0].replace("\"", "").replace(",", " | ")
                print("[+] Scraped badges: {link}".format(link=badges))
            else:
                used = True

def get_discord(data):
    used = False
    for line in data.splitlines():
        if "alt=\"discord\"" in line and used != True:
            used = True
            discord = line.split("<div class=\"tooltip\"")[1].split("<img class=")[0].replace("data-tip=\"", "").replace("\">", "")
            print("[+] Scraped Discord:{link}".format(link=discord))
