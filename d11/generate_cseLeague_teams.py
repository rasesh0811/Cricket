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
while count <= 1:
    urlCSE = "https://fantasy.iplt20.com/season/services/user/contest/live/53780101/leaderboard?optType=1&gamedayId="+str(match)+"&phaseId=1&pageNo=1&topNo=500&pageChunk=500&pageOneChunk=500&minCount=17&leagueId=53780101"

    headers = CaseInsensitiveDict()
    headers["authority"] = "fantasy.iplt20.com"
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
    headers["content-type"] = "application/json;charset=utf-8"
    headers["cookie"] = "G_ENABLED_IDPS=google; _ga=GA1.2.637552169.1650699013; _gid=GA1.2.1696437790.1650699013; dh_user_id=dc1f7270-c2cf-11ec-a93b-fd3155df48ca; __csrf=5de40d54-16eb-5b80-43c5-cf42c16e5205; WZRK_G=870990de262f46e5866915c8dd992697; ajs_anonymous_id=%227006fa32-e58c-4d1d-a0eb-467e4a6b5350%22; connect.sid=s%3AUrylOzK1bxYw6eGoJ4RtUpupI5GVwmGb.xpxtUXXhIYZ27in4shGQy4JbK9EWd%2FjkqoW%2FF4z4z%2FE; d11partner=%7B%0A%20%20%22UserName%22%3A%20%22TheUnknownAcquaintance%22%2C%0A%20%20%22HasTeam%22%3A%201%2C%0A%20%20%22TeamName%22%3A%20%22TheUnknownAcquaintance%22%2C%0A%20%20%22FavTeamId%22%3A%20%222955%22%2C%0A%20%20%22SocialId%22%3A%20%22108074559%22%2C%0A%20%20%22GUID%22%3A%20%2276608e84-a9f1-11ec-a4a1-0a1b246c8927%22%2C%0A%20%20%22ActiveTour%22%3A%20null%2C%0A%20%20%22IsTourActive%22%3A%200%2C%0A%20%20%22UserId%22%3A%20%22EA2DA67911675C%22%2C%0A%20%20%22TeamId%22%3A%20%22EA2DA67911675C%22%2C%0A%20%20%22ProfileURL%22%3A%20%22https%3A%2F%2Fwww.dream11.com%2Fpublic%2Fimgs%2Fleaderboard_default_image.png%22%2C%0A%20%20%22TeamName_Allow%22%3A%20%220%22%2C%0A%20%20%22Version%22%3A%20%224%22%0A%7D; TEAM_BUSTER=20220423111548; PUBLIC_LEAGUE_BUSTER=20220423111548; PRIVATE_LEAGUE_BUSTER=20220423111548; badge=20220423111548; profile=20220423111548; autorefresh=20220423112142"
    headers["$entity"] = "d3tR0u0021t5m@sh"
    headers["referer"] = "https://fantasy.iplt20.com/season/league/view/53780101"
    headers["sec-ch-ua"] = "Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = "macOS"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    headers["x-csrf"] = "5de40d54-16eb-5b80-43c5-cf42c16e5205"

    respList = requests.get(urlCSE, headers=headers)
    listJson = respList.json()
    print(respList.status_code)
    # print(listJson)
    team_list.extend(listJson["Data"]["Value"])
    # print("fetched ", count*100," teams")
    count += 1

# print(team_list)
print("fetched a total of", len(team_list)," teams")
team_list_as_json = {"listOfAllTeams" :team_list}
import json

    
with open("teamListCSE.json", "w") as outfile:
    json.dump(team_list_as_json, outfile)
###==========================================================================================