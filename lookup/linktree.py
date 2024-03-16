from requests_html import HTMLSession, AsyncHTMLSession

def is_valid(data):
    for line in data.splitlines():
        if "<title>" in line:
            if "Page Not Found" in line:
                print("[+] Invalid profile")
                return True
            else:
                return False




def get_username(data):
    for line in data.splitlines():
        if "<h1 id=\"profile-" in line:

            username = line.split("<h1 id=\"profile-")[1].split("\"")[0]
            print("[+] Username scraped: {link}".format(link=username))


def get_links(data):
    for social in data.html.absolute_links:
        if "https://linktr.ee/" not in social:
        
            print("[+] Social scraped: {link}".format(link=social))
                



def get_pfp(data):
    used = False
    for line in data.splitlines():
        if "<img src=\"https://ugc.production.linktr.ee/" in line and used != True:
            used = True
            pfp = "https://ugc.production.linktr.ee/" +  line.split("<img src=\"https://ugc.production.linktr.ee/")[1].split("?io")[0]

            print("[+] Profile picture scraped: {link}".format(link=pfp))
            


