"""
common_passwords.py
-------------------
This file contains a large list of common and weak passwords.
Used by simple_password_checker.py to check against unsafe passwords.
"""

COMMON_PASSWORDS = [
    # Top 20 most common passwords from NordPass 2024
    "123456", "123456789", "12345678", "password", "qwerty123", 
    "qwerty1", "111111", "12345", "secret", "123123", 
    "1234567890", "1234567", "000000", "qwerty", "abc123", 
    "password1", "iloveyou", "11111111", "dragon", "monkey",

    # Additional highly common passwords
    "123123123", "123321", "qwertyuiop", "00000000", "Password",
    "admin", "welcome", "letmein", "sunshine", "baseball", 
    "princess", "football", "1q2w3e", "password123", "asdfgh",
    "admin123", "superman", "user", "guest", "1234", 
    "test", "login", "service", "changeme", "master",

    # More common passwords from breach data
    "example", "222222", "2025", "2024", "manager", "security",
    "internet", "starwars", "liverpool", "shadow", "654321",
    "root", "102030", "rockyou", "babygirl", "lovely",
    "jessica", "nicole", "daniel", "ashley", "michael",
    "tigger", "michelle", "jordan", "hunter", "trustno1",

    # Dictionary words and names
    "thomas", "robert", "access", "love", "buster", "soccer", 
    "hockey", "killer", "george", "sexy", "andrew", "charlie", 
    "asshole", "fuckyou", "dallas", "panties", "pepper", "austin", 
    "william", "golfer", "summer", "heather", "hammer", "yankees", 
    "joshua", "maggie", "biteme", "enter", "thunder", "cowboy",

    # More common passwords
    "silver", "richard", "fucker", "orange", "merlin", "corvette", 
    "bigdog", "cheese", "matthew", "patrick", "martin", "freedom", 
    "ginger", "blowjob", "sparky", "yellow", "camaro", "131313", 
    "bitch", "hello", "scooter", "please", "porsche", "guitar", 
    "chelsea", "black", "diamond", "nascar", "jackson", "cameron",

    # Technology and brands
    "computer", "amanda", "wizard", "xxxxxxxx", "money", "phoenix", 
    "mickey", "bailey", "knight", "iceman", "tigers", "purple", 
    "andrea", "horny", "dakota", "aaaaaa", "player", "morgan", 
    "boomer", "cowboys", "edward", "charles", "girls", "booboo", 
    "coffee", "bulldog", "ncc1701", "rabbit", "peanut", "john",

    # More names and words
    "johnny", "gandalf", "spanky", "winter", "brandy", "compaq", 
    "carlos", "tennis", "james", "mike", "brandon", "fender", 
    "anthony", "blowme", "ferrari", "cookie", "chicken", "maverick", 
    "chicago", "joseph", "diablo", "sexsex", "hardcore", "willie", 
    "chris", "panther", "yamaha", "justin", "banana", "driver",

    # Sports and entertainment
    "marine", "angels", "fishing", "david", "maddog", "hooters", 
    "wilson", "butthead", "dennis", "fucking", "captain", "bigdick", 
    "chester", "smokey", "xavier", "steven", "viking", "snoopy", 
    "blue", "eagle", "987654321", "666666", "555555", "777777", 
    "888888", "999999", "101010", "121212", "141414", "151515",

    # Numeric patterns
    "161616", "171717", "181818", "191919", "202020", "212121", 
    "232323", "242424", "252525", "262626", "272727", "282828", 
    "292929", "303030", "313131", "323232", "343434", "353535", 
    "363636", "373737", "383838", "393939", "404040", "414141", 
    "424242", "434343", "444444", "454545", "464646", "474747",

    # More numeric patterns
    "484848", "494949", "505050", "515151", "525252", "535353", 
    "545454", "565656", "575757", "585858", "595959", "606060", 
    "616161", "626262", "636363", "646464", "656565", "676767", 
    "686868", "696969", "707070", "717171", "727272", "737373", 
    "747474", "757575", "767676", "787878", "797979", "808080",

    # Extended numeric patterns
    "818181", "828282", "838383", "848484", "858585", "868686", 
    "878787", "898989", "909090", "919191", "929292", "939393", 
    "949494", "959595", "969696", "979797", "989898", "qwertyui", 
    "asdfghjk", "zxcvbnm", "qaz123", "wsx234", "edc345", "rfv456", 
    "tgb567", "yhn678", "ujm789", "1qaz2wsx", "2wsx3edc", "3edc4rfv",

    # Keyboard patterns
    "4rfv5tgb", "5tgb6yhn", "6yhn7ujm", "7ujm8ik,", "qazwsx", 
    "wsxedc", "edcrfv", "rfvtgb", "tgbyhn", "yhnujm", "zaq12wsx", 
    "xsw23edc", "cde34rfv", "vfr45tgb", "bgt56yhn", "nhy67ujm", 
    "jennifer", "william", "christopher", "samantha", "sarah", 
    "stephanie", "melissa", "kevin", "steven", "kimberly", "mark",

    # Names and common words
    "lisa", "maria", "susan", "karen", "ronald", "nancy", 
    "dorothy", "betty", "helen", "sandra", "donna", "carol", 
    "ruth", "sharon", "laura", "deborah", "apple", "orange", 
    "banana", "grape", "cherry", "strawberry", "technology", 
    "science", "nature", "animal", "flower", "water", "earth",

    # More dictionary words
    "fire", "music", "movie", "book", "school", "house", 
    "family", "friend", "happy", "lucky", "funny", "crazy", 
    "smart", "strong", "beautiful", "wonderful", "amazing", 
    "awesome", "perfect", "special", "unique", "different", 
    "simple", "easy", "difficult", "hard", "soft", "loud",

    # Descriptive words
    "quiet", "fast", "slow", "big", "small", "long", "short", 
    "tall", "high", "low", "hot", "cold", "warm", "cool", 
    "light", "dark", "bright", "sweet", "sour", "bitter", 
    "salty", "spicy", "delicious", "good", "bad", "new", 
    "old", "young", "fresh", "clean", "dirty", "empty",

    # More adjectives and brands
    "full", "open", "closed", "free", "busy", "rich", "poor", 
    "expensive", "cheap", "safe", "dangerous", "healthy", "sick", 
    "weak", "lakers", "steelers", "packers", "celtics", "bulls", 
    "heat", "spurs", "warriors", "knicks", "nets", "sixers", 
    "pistons", "cavs", "magic", "hawks", "hornets", "raptors",

    # Sports teams and tech brands
    "bucks", "nike", "adidas", "google", "microsoft", "facebook", 
    "amazon", "netflix", "spotify", "youtube", "instagram", 
    "twitter", "tiktok", "snapchat", "whatsapp", "telegram", 
    "discord", "zoom", "skype", "linkedin", "reddit", "pinterest", 
    "tumblr", "wordpress", "blogger", "1990", "1991", "1992",

    # Years
    "1993", "1994", "1995", "1996", "1997", "1998", "1999", 
    "2000", "2001", "2002", "2003", "2004", "2005", "2006", 
    "2007", "2008", "2009", "2010", "2011", "2012", "2013", 
    "2014", "2015", "2016", "2017", "2018", "2019", "2020", 
    "2021", "2022", "2023", "0101", "0202", "0303", "0404",

    # Dates and pop culture
    "0505", "0606", "0707", "0808", "0909", "1010", "2020", 
    "2121", "2222", "2323", "2424", "2525", "2626", "2727", 
    "2828", "2929", "3030", "3131", "pokemon", "mario", "luigi", 
    "zelda", "sonic", "batman", "spiderman", "ironman", "hulk", 
    "thor", "captain", "america", "wolverine", "deadpool", "avengers",

    # Gaming and entertainment
    "marvel", "disney", "fortnite", "minecraft", "roblox", "pubg", 
    "valorant", "overwatch", "warcraft", "starcraft", "counterstrike", 
    "callofduty", "battlefield", "fifa", "madden", "nba2k", "gta", 
    "witcher", "skyrim", "fallout", "cyberpunk", "destiny", "apex", 
    "league", "legends", "dota", "csgo", "rust", "among", "us",

    # Password variations with symbols
    "password!", "password@", "password#", "password$", "password%", 
    "password^", "password&", "password*", "password01", "password02", 
    "password03", "password04", "password05", "password06", "password07", 
    "password08", "password09", "password10", "123456!", "123456@", 
    "123456#", "123456$", "123456%", "123456^", "123456&", "123456*",

    # More variations
    "qwerty!", "qwerty@", "qwerty#", "qwerty$", "qwerty%", "qwerty^", 
    "qwerty&", "qwerty*", "admin!", "admin@", "admin#", "admin$", 
    "admin%", "admin^", "admin&", "admin*", "backup", "database", 
    "default", "support", "temp", "temporary", "public", "private", 
    "system", "network", "server", "windows", "linux", "mac",


# Extended password list - Additional common passwords

# Device defaults and admin passwords
"admin", "user", "guest", "test", "service", "support", "default", "changeme",
"master", "root", "setup", "config", "system", "network", "device", "router",
"modem", "wireless", "wifi", "internet", "broadband", "connection", "access",
"login", "signin", "password123", "admin123", "user123", "guest123", "test123",
"service123", "support123", "default123", "changeme123", "master123", "root123",

# Router and device specific defaults
"michelangelo", "epicrouter", "kpboruger", "wepkey", "speedxess", "speedstream",
"smcadmin", "private", "public", "netgear", "linksys", "belkin", "dlink",
"cisco", "tplink", "asus", "netcomm", "zyxel", "huawei", "motorola", "arris",]


# Use a set for faster lookup (important for large lists)
COMMON_PASSWORDS_SET = {pw.lower() for pw in COMMON_PASSWORDS}
