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
    
    # urlGujarat = "https://fantasy.iplt20.com/season/services/leaderboard/team/2955?optType=1&gamedayId="+str(match)+"&phaseId=1&pageNo="+str(count)+"&topNo=500&pageChunk=500&pageOneChunk=500&minCount=154494"
    urlPunjab = "https://fantasy.iplt20.com/season/services/leaderboard/live/team/1107?optType=1&gamedayId="+str(match)+"&phaseId="+str(count)+"&pageNo="+str(count)+"&topNo=100&pageChunk=100&pageOneChunk=100&minCount=49494&liveVersion=4568"

    urlChennai = "https://fantasy.iplt20.com/season/services/leaderboard/team/1108?optType=1&gamedayId="+str(match)+"&phaseId="+str(count)+"&pageNo="+str(count)+"&topNo=100&pageChunk=100&pageOneChunk=100&minCount=392314"

    headers = CaseInsensitiveDict()
    headers["authority"] = "fantasy.iplt20.com"
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-GB,en;q=0.9"
    headers["content-type"] = "application/json;charset=utf-8"
    headers["cookie"] = "dh_user_id=1bb962c0-cde2-11ec-a011-315b665ba7ce; _ga=GA1.2.984211072.1651913155; _gid=GA1.2.1274811755.1651913155; __csrf=86c088b1-db1d-75f0-03da-32b9a0a35910; G_ENABLED_IDPS=google; WZRK_G=c0f5144db6cc4e6d9ecc5203a1d3b7ae; ajs_anonymous_id=%222644d9f2-ec18-4563-8035-3ba76bc9e951%22; WZRK_S_W4R-49K-494Z=%7B%22p%22%3A1%2C%22s%22%3A1651913159%2C%22t%22%3A1651913168%7D; connect.sid=s%3AnMD6ksfrPJYZMdodt0Wz2KLzeV-tEycd.%2BtH2zcGRRuCsACo5zWKJGF7%2F21ofE3B5hbuP6Wdx9aM; _dd_s=rum=0&expire=1651914079251; d11partner=%7B%0A%20%20%22UserName%22%3A%20%22PLAY%20TO%20LEARN%20%22%2C%0A%20%20%22HasTeam%22%3A%201%2C%0A%20%20%22TeamName%22%3A%20%22PLAY%20TO%20LEARN%20%22%2C%0A%20%20%22FavTeamId%22%3A%20%221108%22%2C%0A%20%20%22SocialId%22%3A%20%22133910920%22%2C%0A%20%20%22GUID%22%3A%20%224484361a-ab7a-11ec-b59d-0ade8d0f08e5%22%2C%0A%20%20%22ActiveTour%22%3A%20null%2C%0A%20%20%22IsTourActive%22%3A%200%2C%0A%20%20%22UserId%22%3A%20%22EC24A97C13665D8FB9%22%2C%0A%20%20%22TeamId%22%3A%20%22EC24A97C13665D8FB9%22%2C%0A%20%20%22ProfileURL%22%3A%20%22https%3A%2F%2Fwww.dream11.com%2Fpublic%2Fimgs%2Fleaderboard_default_image.png%22%2C%0A%20%20%22TeamName_Allow%22%3A%20%220%22%2C%0A%20%20%22Version%22%3A%20%224%22%0A%7D; _gat_gtag_UA_193187243_1=1"
    headers["$entity"] = "d3tR0u0021t5m@sh"
    headers["referer"] = "https://fantasy.iplt20.com/season/league/view/2"
    headers["sec-ch-ua"] = "Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = "macOS"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"



    respList = requests.get(urlChennai, headers=headers)
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

    
with open("teamListChennai.json", "w") as outfile:
    json.dump(team_list_as_json, outfile)
###==========================================================================================