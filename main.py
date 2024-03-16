import sys, shutil, os, requests, json
from lookup import soloto, linktree, ezbio, onlymyspace
from requests_html import HTMLSession, AsyncHTMLSession
from pystyle import Colorate, Colors, Center
from datetime import datetime


class Search:
    def solo(site, mode):
        if mode == "url":
            s = HTMLSession()
            data = s.get(site)
            if soloto.is_valid(data.text) != True:
                print("[+] Data for {}".format(sys.argv[2].split("https://solo.to/")[1]))
                print("[+] Service: https://solo.to/")
                soloto.get_username(data.text)
                soloto.verified_check(data.text)
                soloto.get_location(data.text)
                soloto.get_discord(data.text)
                soloto.get_telegram(data.text)
                soloto.get_mobile(data.text)
                soloto.get_pfp(data.text)
                soloto.links(data.text)

                return True

        elif mode == "username":
            s = HTMLSession()
            data = s.get("https://solo.to/" + site)
            if soloto.is_valid(data.text) != True:
                print("[+] Data for {}".format(site))
                print("[+] Service: https://solo.to/")
                soloto.get_username(data.text)
                soloto.verified_check(data.text)
                soloto.get_location(data.text)
                soloto.get_discord(data.text)
                soloto.get_telegram(data.text)
                soloto.get_mobile(data.text)
                soloto.get_pfp(data.text)
                soloto.links(data.text)

                return True
    




    def linktree(site, mode):
        if mode == "url":
            s = HTMLSession()
            data = s.get(site)

            if linktree.is_valid(data.text) != True:
                print("[+] Data for {}".format(sys.argv[2].split("https://linktr.ee/")[1]))
                print("[+] Service: https://linktr.ee")
                linktree.get_username(data.text)
                linktree.get_pfp(data.text)
                linktree.get_links(data)

                return True

        elif mode == "username":
            s = HTMLSession()
            data = s.get("https://linktr.ee/" + site)

            if linktree.is_valid(data.text) != True:
                print("[+] Data for {}".format(site))
                print("[+] Service: https://linktr.ee")
                linktree.get_username(data.text)
                linktree.get_pfp(data.text)
                linktree.get_links(data) 

                return True



    def ezbio(site, mode):
        if mode == "url":

            s = HTMLSession()
            data = s.get(site)

            if ezbio.is_valid(data.text) != True:
                print("[+] Data for {}".format(sys.argv[2].split("https://e-z.bio/")[1]))
                print("[+] Service: https://e-z.bio")
                ezbio.get_username(data.text)
                ezbio.get_ranks(data.text)
                ezbio.get_discord(data.text)
                ezbio.get_pfp(data.text)
                ezbio.get_links(data.text)

                return True

        elif mode == "username":
            s = HTMLSession()
            data = s.get("https://e-z.bio/" + site)

            if ezbio.is_valid(data.text) != True:
                print("[+] Data for {}".format(site))
                print("[+] Service: https://e-z.bio")
                ezbio.get_username(data.text)
                ezbio.get_ranks(data.text)
                ezbio.get_discord(data.text)
                ezbio.get_pfp(data.text)
                ezbio.get_links(data.text)

                return True
                


    def onlymyspace(site, mode):
        if mode == "url":
            s = HTMLSession()
            data = s.get(site)

            if onlymyspace.is_valid(data.text) != True:
                print("[+] Data for {}".format(sys.argv[2].split("https://only-my.space/")[1]))


                onlymyspace.get_username(data.text)
                onlymyspace.get_views(data.text)
                onlymyspace.get_pronouns(data.text)
                onlymyspace.get_timezone(data.text)
                onlymyspace.get_bio(data.text)
                onlymyspace.get_badges(data.text)
                onlymyspace.get_id(data.text)
                onlymyspace.get_links(data)
                onlymyspace.get_pfp(data.text)
                onlymyspace.get_discord(data.text)
                return True

        elif mode == "username":
            s = HTMLSession()
            data = s.get("https://only-my.space/" + site)

            if onlymyspace.is_valid(data.text) != True:
                print("[+] Data for {}".format(site))


                onlymyspace.get_username(data.text)
                onlymyspace.get_views(data.text)
                onlymyspace.get_pronouns(data.text)
                onlymyspace.get_timezone(data.text)
                onlymyspace.get_bio(data.text)
                onlymyspace.get_badges(data.text)
                onlymyspace.get_id(data.text)
                onlymyspace.get_links(data)
                onlymyspace.get_pfp(data.text)
                onlymyspace.get_discord(data.text)

                return True
                
                


                




class Main:


    def clear_s():
        os.system("cls") if os.name == "nt" else os.system("clear")


    def load_settings():
        with open("config.json") as f:
            config = json.load(f)
            menu = config.get("MENU")
            clear = config.get("CLEAR-S")

            return menu, clear


    def Main():
        menu, clear = Main.load_settings()
        if clear:
            Main.clear_s()
        art = """

 ____,
/.---|
`    |     ___
    (=\.  /-. |
     |\/\_|"|  |
     |_\ |;-|  ;
     | / \| |_/ \  
     | )/\/      \      ╔╦╗╔═╗╔═╗╔═╗
     | ( '|  \   |      ║║║╠═╣║ ╦║╣
     |    \_ /   \      ╩ ╩╩ ╩╚═╝╚═╝  
     |    /  \_.--\  Deved by Josh Webb
     \    |    (|\`
      |   |      |
      |   |      '.
      |  /         |
      \  \.__.__.-._)
        """
        if menu:
            print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(art)))

        if sys.argv[1] == "-s":
            print("[+] Services we support")
            services = ("solo.to", "linktr.ee", "e-z.bio", "only-my.space")
            print("\n".join(services))
        elif sys.argv[1] == "-soloto":
            if sys.argv[3] == "-u":
                Search.solo(sys.argv[2], "url")
            elif sys.argv[3] == "-U":
                Search.solo(sys.argv[2], "username")
        elif sys.argv[1] == "-linktree":
            if sys.argv[3] == "-u":
                Search.linktree(sys.argv[2], "url")
            elif sys.argv[3] =="-U":
                Search.linktree(sys.argv[2], "username")
        elif sys.argv[1] == "-ezbio":
            if sys.argv[3] == "-u":
                Search.ezbio(sys.argv[2], "url")
            elif sys.argv[3] == "-U":
                Search.ezbio(sys.argv[2], "username")

        elif sys.argv[1] == "-onlymyspace":
            if sys.argv[3] == "-u":
                Search.onlymyspace(sys.argv[2], "url")
            elif sys.argv[3] == "-U":
                Search.onlymyspace(sys.argv[2], "username")

        elif sys.argv[1] == "-h":
            help = """
( - ) Usage: python mage.py -[SITE] -[URL OR USERNAME] -[MODE]            

( - ) Example: python mage.py -soloto jwe0 -U

-h                                          Display a help message
-s                                          Available services


-a                                          Check all services
-soloto                                     Use the solo.to service
-linktree                                   Use the linktr.ee service
-ezbio                                      Use the ezio service
-onlymyspace                                Use the onlymyspace service


-u                                          Use a url from the specified website
-U                                          Use a username you have to check the specified website
            """
            print(help)




        elif sys.argv[1] == "-a":
            if sys.argv[3] == "-u":
                if Search.solo(sys.argv[2], "url"):
                    print()
                if Search.linktree(sys.argv[2], "url"):
                    print()
                if Search.ezbio(sys.argv[2], "url"):
                    print()
                Search.onlymyspace(sys.argv[2], "url")





            elif sys.argv[3] == "-U":
                if Search.solo(sys.argv[2], "username"):
                    print()
                if Search.linktree(sys.argv[2], "userame"):
                    print()
                if Search.ezbio(sys.argv[2], "username"):
                    print()
                Search.onlymyspace(sys.argv[2], "username")

                

        



if __name__ == "__main__":
    Main.Main()
