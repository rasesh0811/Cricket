import sys
 
# total arguments
total_cmd_args = len(sys.argv)
print("Total arguments passed:", total_cmd_args)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
if(total_cmd_args>1):
    matchNumber = int(sys.argv[1])
else : matchNumber = 36

if(total_cmd_args>2):
    leagueName = str(sys.argv[2])
else : leagueName = "CSE"


import requests
import json
from requests.structures import CaseInsensitiveDict

if(leagueName == "GT"):
    input_json_file = "teamListGujarat.json"
    output_leaderboard = "LeaderBoardGujarat.csv"
elif(leagueName == "FPL"):
    input_json_file = "teamListFPL.json"
    output_leaderboard = "LeaderBoardFPL.csv"
elif(leagueName == "PBKS"):
    input_json_file = "teamListPunjab.json"
    output_leaderboard = "LeaderBoardPBKS.csv"
elif(leagueName == "CSK"):
    input_json_file = "teamListChennai.json"
    output_leaderboard = "LeaderBoardCSK.csv"
elif(leagueName == "TWITTER"):
    input_json_file = "teamListTWITTER.json"
    output_leaderboard = "LeaderBoardTWITTER.csv"
else:
    input_json_file = "teamListCSE.json"
    output_leaderboard = "LeaderBoardCSE.csv"

f = open(input_json_file) 
# returns JSON object as
# a dictionary
team_list_league = json.load(f)
f.close()









fullDetailsOfTeams = []
result = []
count = 1
total_number_of_teams = len(team_list_league["listOfAllTeams"])
print("Total number of teams", total_number_of_teams)
for team in team_list_league["listOfAllTeams"]:
    teamID = team["temid"]
    socialID = team["usrscoid"]
    teamName = team["temname"]
    teamRank = team["rank"]
    teamPoints = team["points"]
    #print("team id is:", teamID)
    #print("social id is:", socialID)    
    # # url = "https://fantasy.iplt20.com/season/services/user/guid/lb-team?optType=1&gamedayId=34&tourgamedayId=34&teamId=16520605&socialId=15573615"
    # url ="https://fantasy.iplt20.com/season/services/user/guid/lb-team/overall?optType=2&teamgamedayId=35&arrtourGamedayId=31,30,29&phaseId=1&teamId=2881010&SocialId=108074559"
    url = "https://fantasy.iplt20.com/season/services/user/guid/lb-team?optType=1&gamedayId="+str(matchNumber)+"&tourgamedayId="+str(matchNumber)+"&teamId="+str(teamID)+"&socialId="+str(socialID)
    #print("URL To fetch userInfo :", url)
    headers = CaseInsensitiveDict()
    headers["authority"] = "fantasy.iplt20.com"
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
    headers["content-type"] = "application/json;charset=utf-8"
    headers["cookie"] = "G_ENABLED_IDPS=google; _ga=GA1.2.637552169.1650699013; _gid=GA1.2.1696437790.1650699013; dh_user_id=dc1f7270-c2cf-11ec-a93b-fd3155df48ca; __csrf=5de40d54-16eb-5b80-43c5-cf42c16e5205; WZRK_G=870990de262f46e5866915c8dd992697; ajs_anonymous_id=%227006fa32-e58c-4d1d-a0eb-467e4a6b5350%22; WZRK_S_W4R-49K-494Z=%7B%22p%22%3A1%2C%22s%22%3A1650703206%2C%22t%22%3A1650703210%7D; _dd_s=rum=0&expire=1650704125802; connect.sid=s%3AUrylOzK1bxYw6eGoJ4RtUpupI5GVwmGb.xpxtUXXhIYZ27in4shGQy4JbK9EWd%2FjkqoW%2FF4z4z%2FE; d11partner=%7B%0A%20%20%22UserName%22%3A%20%22TheUnknownAcquaintance%22%2C%0A%20%20%22HasTeam%22%3A%201%2C%0A%20%20%22TeamName%22%3A%20%22TheUnknownAcquaintance%22%2C%0A%20%20%22FavTeamId%22%3A%20%222955%22%2C%0A%20%20%22SocialId%22%3A%20%22108074559%22%2C%0A%20%20%22GUID%22%3A%20%2276608e84-a9f1-11ec-a4a1-0a1b246c8927%22%2C%0A%20%20%22ActiveTour%22%3A%20null%2C%0A%20%20%22IsTourActive%22%3A%200%2C%0A%20%20%22UserId%22%3A%20%22EA2DA67911675C%22%2C%0A%20%20%22TeamId%22%3A%20%22EA2DA67911675C%22%2C%0A%20%20%22ProfileURL%22%3A%20%22https%3A%2F%2Fwww.dream11.com%2Fpublic%2Fimgs%2Fleaderboard_default_image.png%22%2C%0A%20%20%22TeamName_Allow%22%3A%20%220%22%2C%0A%20%20%22Version%22%3A%20%224%22%0A%7D; _gat_gtag_UA_193187243_1=1"
    headers["$entity"] = "d3tR0u0021t5m@sh"
    headers["referer"] = "https://fantasy.iplt20.com/season/league/view/2"
    headers["sec-ch-ua"] = "Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = "macOS"
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
    headers["x-csrf"] = "5de40d54-16eb-5b80-43c5-cf42c16e5205"



    resp = requests.get(url, headers=headers)
    # print("=======================")
    if(resp.status_code == 200):
        data = resp.json()
        # print(data)
        transfersLeft = data["Data"]["Value"]["subleft"]
        usedTransfers = 130 - transfersLeft
        if(usedTransfers==0):   
            efficiency = 99999
        else: 
            efficiency = teamPoints/usedTransfers
        result.append([teamID, teamName, teamPoints, transfersLeft, efficiency])
        # if(count == 1):
        #     print(data)
        #     print("******************")
        #     print(data["Data"]["Value"])
        #     fullDetailsOfTeams.append(data["Data"]["Value"])
    # print("=======================")
    # break;
    
    if(count%5==0):
        print(count,"/",total_number_of_teams," rows done")
    count += 1
    if(count>500):
        print("Count exceeded 500, so stopping after processing ",count," teams")
        break

print("=======================================================================")
# print(result)

import csv
# field names 
fields = ['TeamID', 'TeamName', 'Points', 'TransfersLeft', 'Efficiency'] 
    
print("Writing leaderboard to csv")  
with open(output_leaderboard, 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(result)

print("Writing leaderboard to csv: completed")

# full_details_as_json = {"detailsOfAllTeams" :fullDetailsOfTeams}
# import json

    
# with open("detailsOfAllTeams.json", "w") as outfile:
#     json.dump(full_details_as_json, outfile)