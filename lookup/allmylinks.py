from requests_html import HTMLSession, AsyncHTMLSession

def is_valid(data):
    for line in data.splitlines():
        if "<title>" in line:
            if "Not Found" in line:
                print("[+] Invalid profile")
                return True
            else:
                return False



def get_username(data):
    for line in data.splitlines():
        if "<title>" in line:
            username = line.split("<title>")[1].split(" |")[0]
            print("[+] Scraped username: {link}".format(link=username))


def get_birthday(data):
    for line in data.splitlines():
        if "class=\"all-my-icon-i040\"></i> " in line:
            birthday = line.split("class=\"all-my-icon-i040\"></i> ")[1].split("<")[0]
            print("[+] Scraped birthday: {link}".format(link=birthday))


def  get_email(data):
    used = False
    for line in data.splitlines():
        if "mailto:" in line and used != True:
            used = True
            email = line.split("mailto:")[1].split("\"")[0]
            print("[+] Scraped email: {link}".format(link=email))

def get_clips(data):
    for line in data.splitlines():
        if "data-clipboard-text=" in line and "allmylinks" not in line:
            link = line.split("data-clipboard-text=")[1].split("\"")[1]
            print("[+] Social scraped: {link}".format(link=link))


def get_location(data):
    for line in data.splitlines():
        if "class=\"all-my-icon-i39\"></i> " in line:
            location = line.split("class=\"all-my-icon-i39\"></i> ")[1].split("<")[0]
            print("[+] Scraped location: {link}".format(link=location))
        

def get_pfp(data):
    for line in data.splitlines():
        if "Profile avatar" in line:
            pfp = line.split("src")[1].split("alt=")[0].replace("\"", "").replace("=", "")
            print("[+] Scraped pfp: {link}".format(link=pfp))
