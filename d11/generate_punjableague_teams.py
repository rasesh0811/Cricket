import sys
 
# total arguments
total_cmd_args = len(sys.argv)
print("Total arguments passed:", total_cmd_args)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
if(total_cmd_args>1):
    matchNumber = int(sys.argv[1])
else : matchNumber = 49

import requests
import json
from requests.structures import CaseInsensitiveDict

###==========================================================================================
# # url = "https://fantasy.iplt20.com/season/services/leaderboard/team/2955?optType=1&gamedayId=34&phaseId=1&pageNo=1&topNo=100&pageChunk=100&pageOneChunk=100&minCount=154494"
match = matchNumber
count = 1
team_list = []
while count <= 10:
    # urlPunjab = "https://fantasy.iplt20.com/season/services/leaderboard/live/team/1107?optType=1&gamedayId="+str(match)+"&phaseId=1&pageNo=1"+str(count)+"&topNo=100&pageChunk=100&pageOneChunk=100&minCount=49490&liveVersion=4566"
    # urlGujarat = "https://fantasy.iplt20.com/season/services/leaderboard/team/2955?optType=1&gamedayId="+str(match)+"&phaseId=1&pageNo="+str(count)+"&topNo=500&pageChunk=500&pageOneChunk=500&minCount=154494"
    # urlPunjab = "https://fantasy.iplt20.com/season/services/leaderboard/live/team/1107?optType=1&gamedayId="+str(match)+"&phaseId="+str(count)+"&pageNo="+str(count)+"&topNo=100&pageChunk=100&pageOneChunk=100&minCount=49494&liveVersion=4568"
    urlPunjab = "https://fantasy.iplt20.com/season/services/leaderboard/team/1107?optType=1&gamedayId="+str(match)+"&phaseId="+str(count)+"&pageNo="+str(count)+"&topNo=100&pageChunk=100&pageOneChunk=100&minCount=53117&buster=20220504152642"
    headers = CaseInsensitiveDict()
    headers["authority"] = "fantasy.iplt20.com"
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
    headers["content-type"] = "application/json;charset=utf-8"
    headers["cookie"] = "G_ENABLED_IDPS=google; G_AUTHUSER_H=0; dh_user_id=139a2130-cbb5-11ec-bdf1-5b7073756633; _ga=GA1.2.1144185004.1651677101; _gid=GA1.2.1342532325.1651677101; _gat_gtag_UA_193187243_1=1; __csrf=4fef73a1-f4fe-9999-e5b2-690a672ed01e; ajs_anonymous_id=%22c0a94db3-325d-4ca3-beee-a016c38be6d7%22; _dd_s=rum=0&expire=1651678127547; connect.sid=s%3A3juK5qnng3gRSdKuqhL5xKkanW1AWjgi.YJzmPmllWjGggd%2FkIWMOCjLbOI1YhjbiRfU81u2Hnbg; d11partner=%7B%0A%20%20%22UserName%22%3A%20%22godoflaws%22%2C%0A%20%20%22HasTeam%22%3A%201%2C%0A%20%20%22TeamName%22%3A%20%22godoflaws%22%2C%0A%20%20%22FavTeamId%22%3A%20%221107%22%2C%0A%20%20%22SocialId%22%3A%20%22128433760%22%2C%0A%20%20%22GUID%22%3A%20%2254615236-a9c0-11ec-b40c-0ade8d0f08e5%22%2C%0A%20%20%22ActiveTour%22%3A%20null%2C%0A%20%20%22IsTourActive%22%3A%200%2C%0A%20%20%22UserId%22%3A%20%22EA24AE791164%22%2C%0A%20%20%22TeamId%22%3A%20%22EA24AE791164%22%2C%0A%20%20%22ProfileURL%22%3A%20%22https%3A%2F%2Fwww.dream11.com%2Fpublic%2Fimgs%2Fleaderboard_default_image.png%22%2C%0A%20%20%22TeamName_Allow%22%3A%20%220%22%2C%0A%20%20%22Version%22%3A%20%224%22%0A%7D"
    headers["$entity"] = "d3tR0u0021t5m@sh"
    headers["referer"] = "https://fantasy.iplt20.com/season/league/view/2"
    headers["sec-ch-ua"] = "Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = "macOS"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"



    respList = requests.get(urlPunjab, headers=headers)
    listJson = respList.json()
    # print(respList.status_code)
    # print(listJson)
    team_list.extend(listJson["Data"]["Value"])
    # print("fetched ", count*500," teams")
    count += 1

# print(team_list)
print("fetched a total of", len(team_list)," teams")
team_list_as_json = {"listOfAllTeams" :team_list}
import json

    
with open("teamListPunjab.json", "w") as outfile:
    json.dump(team_list_as_json, outfile)
###==========================================================================================