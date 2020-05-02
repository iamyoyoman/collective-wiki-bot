# Input prompts
prompt_main = "What would you like to do? Input the corresponding number:\n" \
         "1: Add new entries to the wiki.\n" \
         "2: Update specific entries on the wiki.\n" \
         "3: Thoroughly update the wiki.\n" \
         "4: Add new card link templates to the wiki.\n" \
         "5: Add new tooltips for card pages to the wiki.\n" \
         "6: Update the decklist.\n" \
         "7: nothing.\n\n"
prompt_1 = "How many new cards should be submitted? (20 per new week should be enough most weeks)\n\n"
prompt_2 = "Write the exact names of the cards which should be updated separated by \"_-_\"\n" \
           "Example: \"Crushing Waves_-_Absolute Scaling_-_???\"\n\n"
prompt_4 = "How many new templates should be created? (20 per new week should be enough most weeks)\n\n"
prompt_5 = "How many new tooltips should be created? (20 per new week should be enough most weeks)\n\n"

# URLs
url_api = "https://collective.gamepedia.com/api.php"
url_cards_all = "https://server.collective.gg/api/public-cards/"
url_card_target = "https://server.collective.gg/api/card/{}"
url_leaderboard = "https://server.collective.gg/api/public/leaderboards"

# Querystring parameters
qs_token = {
    'action': "query",
    'meta': "tokens",
    'format': "json",
    'type': "login"
    }

qs_login = {
    'action': "login",
    'format': "json"
    }

qs_parse = {
    'action': "parse",
    'prop': "wikitext",
    'page': "",
    'format': "json"
    }

qs_sandbox = {
    'action': "edit",
    'title': "Collective_Wiki:Sandbox",
    'bot': True,
    'minor': True,
    'watchlist': "nochange",
    'format': "json"
    }

qs_edit = {
    'action': "edit",
    'title': "",
    'bot': True,
    'minor': True,
    'watchlist': "nochange",
    'format': "json"
    }

qs_upload = {
    'action': "upload",
    'ignorewarnings': True,
    'format': "json"
    }

qs_img_dl = {
    'action': "query",
    'format': "json",
    'prop': "imageinfo",
    'iiprop': "url",
    'titles': ""
}

# Data payload (for POST requests)
pl_login = {
    'lgname': "Collectivewikibot@CollectiveWikiBot",
    'lgpassword': "qllfor01mtshqo1jd7phpjs37gol67u5",
    'lgtoken': ""
    }

pl_edit = {
    'text': "",
    'summary': "Card infobox created/updated",
    'token': ""
    }

pl_upload = {
    'filename': "",
    'token': ""
    }

# Infobox WikiMedia template for card pages
info_template = "Infobox\n" \
                "| image = {}.png\n" \
                "| name = {}\n" \
                "| affinity = {}\n" \
                "| rarity = {}\n" \
                "| tribaltype = {}\n" \
                "| homeworld = {}\n" \
                "| releaseweek = {}\n" \
                "| cost = {}\n" \
                "| atk = {}\n" \
                "| hp = {}\n" \
                "| text = {}\n" \
                "| creatorname = {}\n" \
                "| artistname = {}\n"

deck_template = "role='presentation' class='wikitable mw-collapsible mw-collapsed'\n" \
                "!{} {} Rank {}\n" \
                "|-\n" \
                "|\n" 

deck_template_repeat = "{} [[{}]]\n" \
                       "\n" \

# Card blacklist: these won't be updated unless they are specifically targeted
blacklist = ["First Aid Manual", "Gloves", "Bandage", "Painkillers", "Scissors",
             "Assault Wings", "Replicating Mechanism"]
