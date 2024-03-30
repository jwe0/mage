# Mage

```
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
```

Mage is a python based profile link website enumerator. It works by checking and scraping data from these websites. Data could include email addresses, locations, mobile numbers and general info.

| Site          | Support     | Features |
|---------------|-----------|------------|
| solo.to       | ✅       |    username, location, discord, telegram, mobile number, pfp, links
| linktr.ee     | ✅       |  username, pfp, links     |
| e-z.bio       | ✅       |  username, ranks, discord, pfp, links
| only-my.space | ✅       | username ,views, pronouns, timezone, bio, badges, id, links, pfp, discord
| allmylinks.com | ✅ | username, birthday, email, location, pfp, clipboard items

# Install
1. Run `git clone https://github.com/jwe0/mage` to clone the repository
2. Run `cd mage` to change your location to the active directory
3. Run `pip install -r requirements.txt` to install requirements
4. Finally run `python mage.py -h` for mage help.
5. Enjoy :)

# Help
```
( - ) Usage: python mage.py -[SITE] -[URL OR USERNAME] -[MODE]            

( - ) Example: python mage.py -soloto jwe0 -U

-h                                        Display a help message
-s                                        Available services


-a                                        Check all services                                       requires -U not -u
-soloto                                   Use the solo.to service
-linktree                                 Use the linktr.ee service
-ezbio                                    Use the ezio service
-onlymyspace                              Use the onlymyspace service
-allmylinks                               Use the allmylinks service


-scan                                     Scan a target for usernames (status code check)  
                                          - ( - ) Usage: python mage.py -scan [URL] [USER-LIST]      
                                          - ( - ) Example: python mage.py -scan https://solo.to Assets/usernames.txt   


-u                                        Use a url from the specified website
-U                                        Use a username you have to check the specified website
```

# Config.json
```json
{
    "MENU" : true,                        Display menu on run or not
    "CLEAR-S" : true,                     Clear screen on run
}
```

# Regards
I take no legal responsibility for any negative actions committed with my software. This was made for ethical purposes only <3.

If u want to add webites email me the site and I will add it or not depending on their antirobot.
