def is_valid(data):
    for line in data.splitlines():
        if "<title>" in line:
            if "Not Found" in line:
                print("[+] Invalid profile")
                return True
            else:
                return False


def links(data):
    for line in data.splitlines():
        if "href" in line:
            if "https://" in line:
                if "solo.to" not in line:
                    social = line.split("href=")[1].split("id")[0].replace('"', "")
                    print("[+] Social scraped: {link}".format(link=social))


def verified_check(data):
    for line in data.splitlines():
        if "https://cdn.solo.to/images/verified.svg" in line:
            print("[+] Verified account")


def get_pfp(data):
    for line in data.splitlines():
        if "srcset=\"https://cdn.solo.to/user/a" in line:
            pfp = "https://" + line.split("https://")[1].replace("\"><img src=\"", "")
            print("[+] Profile picture scraped: {link}".format(link=pfp))



def get_location(data):
    for line in data.splitlines():
        if "profile-location-text" in line:
            location = line.split(">")[1].replace("</div", "")
            print("[+] Location scraped: {link}".format(link=location))


def get_username(data):
    for line in data.splitlines():
        if "profile-name" and "h1" in line:
            username = line.split(">")[1].replace("</h1", "")
            print("[+] Username scraped: {link}".format(link=username))


def get_discord(data):
    for line in data.splitlines():
        if "discord" in line:
            name = line.split("data-username=")[1].split("\"")[1]
            print("[+] Discord scraped: {link}".format(link=name))


def get_telegram(data):
    for line in data.splitlines():
        if "https://t.me" in line:
            tele = line.split("href")[1].split("\"")[1]
            print("[+] Scraped telegram: {link}".format(link=tele))

def get_mobile(data):
    for line in data.splitlines():
        if "tel:" in line:
            num = line.split("tel:")[1].split("\"")[0]
            print("[+] Phone scraped: {link}".format(link=num))