from requests_html import HTMLSession, AsyncHTMLSession


def is_valid(data):
    if "Page not found" in data:
        print("[+] Invalid profile")
        return True
    else:
        return False


def get_links(data):
    for line in data.splitlines():
        if "socials" in line:
            data = line.split("socials")[1].split("songs")[0].replace('"name"', "").replace(":", "").replace(":", "").replace("{", "").replace("}", "").replace(",", "").replace("url", "").replace("\"", "\n")
            for social in data.splitlines():
                if "http" in social:
                    print("[+] Social scraped: {link}".format(link=social))

def get_username(data):
    for line in data.splitlines():
        if ",\"name\":\"" in line:
            username = line.split(",\"name\":\"")[1].split("\"")[0]
            print("[+] Username scraped: {link}".format(link=username))

def get_ranks(data):
    for line in data.splitlines():
        if "ranks" in line:
            ranks = line.split("ranks")[1].split("]")[0].replace("\"", "").replace("[", "").replace(":", "").replace(",", " | ")
            print("[+] Ranks scraped: {link}".format(link=ranks))


def get_discord(data):
    for line in data.splitlines():
        if "tag" in line:
            username = line.split("tag")[1].split(",")[0].replace("\"", "").replace(":", "")
            plat_and_stat = line.split("tag")[1].split("platform")[1].split(",")[0].replace("{", "").replace("}", "").replace("\"", "").replace(":", " | ")
            badges = line.split("tag")[1].split("badges")[1].split("customStatus")[0].replace("\"", "").replace("[", "").replace("]", "").split(":")[1].replace(",", " | ")

            data = username + plat_and_stat + " | " + badges

            print("[+] Discord scraped: {link}".format(link=data))


def get_pfp(data):
    used = False
    for line in data.splitlines():
        if "https://r2-bios.e-z.host/" in line and used != True:
            used = True
            pfp = "https://r2-bios.e-z.host/" + line.split("https://r2-bios.e-z.host/")[1].split("\"")[0]
            print("[+] Profile picture scraped: {link}".format(link=pfp))

