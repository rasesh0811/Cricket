import math
from re import T
from tabulate import tabulate
import requests
import json
import joblib
# import numpy

import cmath
  
def quadSolver(a,b,c):  
  # calculating discriminant using formula
  dis = b * b - 4 * a * c 
  sqrt_val = math.sqrt(abs(dis)) 
    
  # checking condition for discriminant
  if dis > 0: 
      # print(" real and different roots ") 
      # print((-b + sqrt_val)/(2 * a)) 
      # print((-b - sqrt_val)/(2 * a)) 
      ans1 = (-b + sqrt_val)/(2 * a)
      ans2 = (-b - sqrt_val)/(2 * a)
  elif dis == 0: 
      # print(" real and same roots") 
      # print(-b / (2 * a)) 
      ans1 = ans2 = -b / (2 * a)
    
  # when discriminant is less than 0
  else:
      print("Complex Roots")
      ans1 = ans2 = "NA" 
      print(- b / (2 * a), " + i", sqrt_val) 
      print(- b / (2 * a), " - i", sqrt_val) 
  return (ans1,ans2)

class Team :
  def __init__(self, name, runsScored, ballsFaced, runsConceded, ballsDelivered):
    self.name = name
    self.runsScored = runsScored
    self.ballsFaced = ballsFaced
    self.runsConceded = runsConceded
    self.ballsDelivered = ballsDelivered

  def currentNRR(self):
    return (self.runsScored/self.ballsFaced - self.runsConceded/self.ballsDelivered)*6


#==============CONSTANTS==============
expected_min_total = 100
expected_max_total = 250
runs_in_increments_of = 10
ballsPerInnings = 120 #FOR T20, 300 for ODI
#=====================================

#================================================= INIT DATA =======================================================
teams = {}
team_codes_list = []
#===============================================================================================================
def convertOversToBalls(oversStr):
  fullOvers = oversStr.split('.')[0]
  balls = oversStr.split('.')[1]
  return int(fullOvers) * 6 + int(balls)

def print_current_nrrs():
  ''' Print the current NRR for all available teams. '''
  table = [['Team Code','Team Name', 'NRR']]
  for teamCode in teams:
    teamObject = teams[teamCode]
    tableRow = [teamCode, teamObject.name, str(round(teamObject.currentNRR(), 4))]
    table.append(tableRow)
  print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

def add_new_team():
  ''' name, runsScored, ballsFaced, runsConceded, ballsDelivered):'''
  code = input("Enter Team Code:")
  code = code.upper()
  if code not in teams:
    name = input("Enter Team Name:")
    runsScored = int(input("Enter Total Runs Scored:"))
    ballsFaced = int(input("Enter Total Balls Faced:"))
    runsConceded = int(input("Enter Total Runs Conceded:"))
    ballsDelivered = int(input("Enter Total Balls Delivered:"))
    new_team = Team(name, runsScored, ballsFaced, runsConceded, ballsDelivered)
    teams[code] = new_team
    team_codes_list.append(code)
  else:
    print("This team code already exists.")

def compare():
  ''''''
  

  teamCode = input("Enter my team code ("+str(team_codes_list)+") : ")
  teamCode = teamCode.upper()
  if teamCode in teams:
    myTeam = teams[teamCode]
  else:
    print("Invalid code for 'my team' provided. Aborting!")
    return
  
  oppTeamCode = input("Enter opp. team code ("+str(team_codes_list)+") : ")
  oppTeamCode = oppTeamCode.upper()
  if oppTeamCode in teams:
    oppTeam = teams[oppTeamCode]
  else:
    print("Invalid code for 'opp. team' provided. Aborting!")
    return
  
  compare_table_chase = []
  compare_table_set_target = []
  
  print("My Team: "+myTeam.name+", NRR of my team:" + str(myTeam.currentNRR()))
  print("Opp Team: "+oppTeam.name+", NRR of opp. team:" + str(oppTeam.currentNRR()))
  print("==========================================")
  print("When my team bats first")
  runsInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
  checkForAParticularScore = int(input("Enter custom value for runs scored: "))
  if(checkForAParticularScore>0):
    runsInFinalInnings.append(checkForAParticularScore)
  for runsScoredInCurrentInnings in runsInFinalInnings:
    #TEAM1
    rs1 = myTeam.runsScored + runsScoredInCurrentInnings #+ marginOfVictory
    bf1 = myTeam.ballsFaced + ballsPerInnings
    rc1 = myTeam.runsConceded + runsScoredInCurrentInnings
    bd1 = myTeam.ballsDelivered + ballsPerInnings

    #TEAM2
    rs2 = oppTeam.runsScored + runsScoredInCurrentInnings
    bf2 = oppTeam.ballsFaced + ballsPerInnings
    rc2 = oppTeam.runsConceded + runsScoredInCurrentInnings #+ marginOfVictory
    bd2 = oppTeam.ballsDelivered + ballsPerInnings

    #(rs1+mv)/bf1 - rc1/bd1 = rs2/bf2 - (rc2 + mv)/bd2
    marginOfVictory = (rs2/bf2 + rc1/bd1 - rs1/bf1 - rc2/bd2)/(1/bf1 + 1/bd2)
    marginOfVictory = math.ceil(marginOfVictory)
    # if(marginOfVictory > 0):
    #     marginOfVictory = math.ceil(marginOfVictory)
    # else: 
    #     marginOfVictory = math.floor(marginOfVictory)
    # print("After setting a target of: "+ str(runsScoredInCurrentInnings)+" ,We will need to win by " + str(marginOfVictory)+" runs.")
    compare_table_set_target.append((runsScoredInCurrentInnings,marginOfVictory))
  print(tabulate(compare_table_set_target, headers=['Runs Scored', 'Margin of Victory Required'], tablefmt='fancy_grid'))
  print("==========================================")
  print("When my team bowls first")
  runsConcededInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
  checkForAParticularScore = int(input("Enter custom value for runs conceded: "))
  if(checkForAParticularScore>0):
    runsConcededInFinalInnings.append(checkForAParticularScore)
  scoreDiff = int(input('Enter final score difference(0 for super over victory, default = 1): ') or 1)
  for runsConcededInCurrentInnings in runsConcededInFinalInnings:
    

    #TEAM1
    rs1 = myTeam.runsScored + runsConcededInCurrentInnings + scoreDiff
    bf1 = myTeam.ballsFaced #+ toBeChasedInBalls
    rc1 = myTeam.runsConceded + runsConcededInCurrentInnings
    bd1 = myTeam.ballsDelivered + ballsPerInnings

    #TEAM2
    rs2 = oppTeam.runsScored + runsConcededInCurrentInnings
    bf2 = oppTeam.ballsFaced + ballsPerInnings
    rc2 = oppTeam.runsConceded + runsConcededInCurrentInnings + scoreDiff
    bd2 = oppTeam.ballsDelivered #+ toBeChasedInBalls

    #rs1/(bf1+toBeChasedInBalls) + rc2/(bd2+toBeChasedInBalls) = rs2/bf2 + rc1/bd1 
    # rs1/(bf1+toBeChasedInBalls) + rc2/(bd2+toBeChasedInBalls) = rs2/bf2 + rc1/bd1 

    c1 = rs1
    c2 = bf1
    c3 = rc2
    c4 = bd2
    c5 = rs2/bf2 + rc1/bd1 

    (ans1, ans2) = quadSolver(1,(c2+c4 - (c1+c3)/c5),(c2*c4 - (c1*c4+c2*c3)/c5))

    if ans1 == "NA" or (ans1<0 and ans2<0):
      toBeChasedInBalls = "Not Possible"
      print("After conceding a target of: "+ str(runsConcededInCurrentInnings)+" No possible chase will make NRR equal")
      # continue
    else:
      if(ans1>0 and ans2>0):
        toBeChasedInBalls = min(ans1,ans2)
      elif(ans1>0):
        toBeChasedInBalls = ans1
      elif(ans2>0):
        toBeChasedInBalls = ans2
      
      toBeChasedInBalls = math.floor(toBeChasedInBalls)
      # if(toBeChasedInBalls > 0):
      #   toBeChasedInBalls = math.floor(toBeChasedInBalls)
      # else:
      #   toBeChasedInBalls = math.ceil(toBeChasedInBalls)
      
    # print("After conceding a target of: "+ str(runsConcededInCurrentInnings)+" ,We will need to chase it in " + str(toBeChasedInBalls)+" balls.")
    compare_table_chase.append((runsConcededInCurrentInnings,toBeChasedInBalls))
  print(tabulate(compare_table_set_target, headers=['Runs Scored', 'Margin of Victory Required'], tablefmt='fancy_grid'))
  print(tabulate(compare_table_chase, headers=['Runs Conceded', 'To be chased in Balls'], tablefmt='fancy_grid'))

def acquireTargetNRR():
  teamCode = input("Enter team code ("+str(team_codes_list)+") : ")
  teamCode = teamCode.upper()
  if teamCode in teams:
    teamObject = teams[teamCode]
    print("Calculating for Team: "+teamObject.name)
    print("Current NRR: "+str(round(teamObject.currentNRR(), 4)))
  
  bowl1 = teamObject.ballsFaced
  bowl2 = teamObject.ballsDelivered
  bat1 = teamObject.runsScored
  bat2 = teamObject.runsConceded

  targetNRR = float(input("Enter the NRR to reach:"))
  toss = input("Enter whether '(bat/bowl)' first in this match: ") 
  if(toss == "bat"):
    compare_table_set_target = []
    
    ballsFaced = bowl1 + ballsPerInnings
    ballsDelivered = bowl2 + ballsPerInnings
    runsInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
    checkForAParticularScore = int(input("Enter custom value for runsScored: "))
    if(checkForAParticularScore>0):
      runsInFinalInnings.append(checkForAParticularScore)
    for runsScored in runsInFinalInnings:
      totalRunsScored = bat1 + runsScored
      marginOfVictory = 0  
      #targetNRR = (totalRunsScored/ballsFaced - (bat2 + runsScored - marginOfVictory)/ballsDelivered)*6
      marginOfVictory = bat2 + runsScored - ((totalRunsScored/ballsFaced) - (targetNRR/6))*ballsDelivered
      marginOfVictory = math.ceil(marginOfVictory)
      # if(marginOfVictory > 0):
      #   marginOfVictory = math.ceil(marginOfVictory)
      # else: 
      #   marginOfVictory = math.floor(marginOfVictory)
      #print("After setting a target of: "+ str(runsScored)+" the team would require a margin of: "+ str(marginOfVictory)+" runs.")
      compare_table_set_target.append((runsScored, marginOfVictory))
    print(tabulate(compare_table_set_target, headers=['Runs Scored', 'Margin of Victory Required'], tablefmt='fancy_grid'))
  elif(toss == "bowl"):
    compare_table_chase = []
    
    ballsFaced = bowl1
    ballsDelivered = bowl2 + ballsPerInnings
    runsConcededInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
    checkForAParticularScore = int(input("Enter custom value for runsConceded: "))
    scoreDiff = int(input('Enter final score difference(0 for super over victory, default = 1): ') or 1)
    if(checkForAParticularScore>0):
      runsConcededInFinalInnings.append(checkForAParticularScore)
    for runsConceded in runsConcededInFinalInnings:
      totalRunsConceded = bat2 + runsConceded
      totalRunsScored = bat1 + runsConceded + scoreDiff
      #targetNRR = ((totalRunsScored/(ballsFaced +toBeChasedInBalls) - (totalRunsConceded/ballsDelivered)))*6
      toBeChasedInBalls = (totalRunsScored/((targetNRR/6) + (totalRunsConceded/ballsDelivered))) - ballsFaced
      toBeChasedInBalls = math.floor(toBeChasedInBalls)
      # if(toBeChasedInBalls > 0):
      #   toBeChasedInBalls = math.floor(toBeChasedInBalls)
      # else:
      #   toBeChasedInBalls = math.ceil(toBeChasedInBalls)
      # print("After conceding: "+str(runsConceded)+" runs, it should be chased in: "+str(math.floor(toBeChasedInBalls))+ " balls")
      compare_table_chase.append((runsConceded, toBeChasedInBalls))

    print(tabulate(compare_table_chase, headers=['Runs Conceded', 'To be chased in Balls'], tablefmt='fancy_grid'))
            
def customCheckNRR():
  totalRunsScored = int(input("Enter total runs scored"))
  totalBallsFaced = int(input("Enter total balls faced"))
  totalRunsConceded = int(input("Enter total runs conceded"))
  totalBallsDelivered = int(input("Enter total balls delivered"))
  nrr = (totalRunsScored/totalBallsFaced - totalRunsConceded/totalBallsDelivered)*6
  print("Current NRR = "+ str(nrr))

def barestOfMarginForNonDecrementOfNRR():
  '''Finding the barest of margin required for keeping NRR atleast what it is at the moment'''
  teamCode = input("Enter team code ("+str(team_codes_list)+") : ")
  teamCode = teamCode.upper()
  if teamCode in teams:
    teamObject = teams[teamCode]
    print("Calculating for Team: "+teamObject.name)
    print("Current NRR: "+str(round(teamObject.currentNRR(), 4)))
  
  print("When my team bats first")
  compare_table_set_target = []
  runsInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
  checkForAParticularScore = int(input("Enter custom value for runs scored: "))
  if(checkForAParticularScore>0):
    runsInFinalInnings.append(checkForAParticularScore)
  for runsScoredInCurrentInnings in runsInFinalInnings:
    
    marginOfVictory = (teamObject.ballsFaced + ballsPerInnings) * (teamObject.currentNRR()/6 - teamObject.runsScored/(teamObject.ballsFaced+ ballsPerInnings) + teamObject.runsConceded/(teamObject.ballsDelivered+ballsPerInnings) -(runsScoredInCurrentInnings*(1/(teamObject.ballsFaced + ballsPerInnings) - 1/(teamObject.ballsDelivered + ballsPerInnings))))
    marginOfVictory = math.ceil(marginOfVictory)
    # if(marginOfVictory > 0):
    #     marginOfVictory = math.ceil(marginOfVictory)
    # else: 
    #     marginOfVictory = math.floor(marginOfVictory)
    # print("After setting a target of: "+ str(runsScoredInCurrentInnings)+" ,We will need to win by " + str(marginOfVictory)+" runs.")
    compare_table_set_target.append((runsScoredInCurrentInnings,marginOfVictory))
  print(tabulate(compare_table_set_target, headers=['Runs Scored', 'Barest Margin of Victory Required'], tablefmt='fancy_grid'))

  print("When my team bowls First")
  compare_table_chase = []
  runsConcededInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
  checkForAParticularScore = int(input("Enter custom value for runs conceded: "))
  if(checkForAParticularScore>0):
    runsConcededInFinalInnings.append(checkForAParticularScore)
  
  c1 = teamObject.runsScored
  c2 = teamObject.ballsFaced
  c3 = teamObject.ballsDelivered + ballsPerInnings
  c4 = teamObject.runsScored/teamObject.ballsFaced - teamObject.runsConceded/teamObject.ballsDelivered + teamObject.runsConceded/teamObject.ballsDelivered+ballsPerInnings
  for runsConceded in runsConcededInFinalInnings:
    toBeChasedInBalls = (c2*c3*c4 - c1*c3 -runsConceded*(c3 - c2))/(c3*c4 - runsConceded)
    toBeChasedInBalls = math.floor(toBeChasedInBalls)
    compare_table_chase.append((runsConceded, toBeChasedInBalls))
  print(tabulate(compare_table_chase, headers=['Runs Conceded', 'Barest To be chased in balls Required'], tablefmt='fancy_grid'))

def fetchPointsTable():
  if(len(team_codes_list) > 0):
    print("Some existing teams found. Use Save data and reset option")
    return
  #check the sheet teamStatsData.py for previous IPLs and sample data format of the teamStats object used below.
  url = "https://hs-consumer-api.espncricinfo.com/v1/pages/series/standings?lang=en&seriesId=1345038"


  resp = requests.get(url)
  myjson = json.loads(resp.content)
  standings = myjson['content']['standings']
  # print(type(standings['groups']))
  groups = standings['groups']
  teamStats = groups[0]['teamStats']
  print(len(teamStats), "Teams Found in the points table")
  print("================================")
  for team in teamStats:
      # for key in team.keys():
      #     print(key)
      # print(team['teamInfo']['longName'], team['teamInfo']['abbreviation'])
      # print(team['nrr'])
      # print(team['for'])
      # print(team['against'])
      # print(type(team['against']))
      # print("===============")
      code = team['teamInfo']['abbreviation']
      name = team['teamInfo']['longName']
      runsScored = int(team['for'].split('/')[0])
      ballsFaced = convertOversToBalls(team['for'].split('/')[1])
      runsConceded = int(team['against'].split('/')[0])
      ballsDelivered = convertOversToBalls(team['against'].split('/')[1])
      new_team = Team(name, runsScored, ballsFaced, runsConceded, ballsDelivered)
      teams[code] = new_team
      team_codes_list.append(code)
      print("Number of teams:", len(team_codes_list))
      # break

def saveTeamDataToFileAndReset(): 
  ''' save the current team_codes_list and teams object to file and clear them'''
  # Dumps into file
  # print("before dump:", teams)
  # joblib.dump(team_codes_list, 'team_codes_list.pkl')
  # joblib.dump(teams, 'teams_dict.sav')
  allTeamsData = []
  for team in teams:
    teamData = []
    teamData.append(team)
    teamData.append(teams[team].name)
    teamData.append(teams[team].runsScored)
    teamData.append(teams[team].ballsFaced)
    teamData.append(teams[team].runsConceded)
    teamData.append(teams[team].ballsDelivered)
    allTeamsData.append(teamData)
  print("before dump:", allTeamsData)
  joblib.dump(allTeamsData, 'allTeamsData.sav')
  teams.clear()
  team_codes_list.clear()
  
def loadDataFromFile():
  allTeamsData = joblib.load('allTeamsData.sav')
  print("from file:", allTeamsData)
  for team in allTeamsData:
    teamCode = team[0]
    team_codes_list.append(teamCode)
    newTeam = Team(team[1], team[2], team[3], team[4], team[5])
    teams[teamCode] = newTeam
  print(len(team_codes_list), "Teams Loaded")

while True:
  print("============================")
  print("1. Print NRR For all teams.")
  print("2. Add a new team data.")
  print("3. Acquire target NRR.")
  print("4. Compare NRR.")
  print("5. Check Custom NRR.")
  print("6. Minimum margin to avoid decrement of NRR")
  print("7. Fetch Points Table Data")
  print("8. Save Data and Reset")
  print("9. Load Saved Data From Files")
  print("============================")
  print("Choose an option: ", end='')
  choice = int(input())
  if (choice == 1):
    print_current_nrrs()
  elif (choice == 2):
    add_new_team()
  elif (choice == 3):
    acquireTargetNRR()
  elif (choice == 4):
    compare()
  elif (choice == 5):
    customCheckNRR()
  elif (choice == 6):
    barestOfMarginForNonDecrementOfNRR()
  elif (choice == 7):
    fetchPointsTable()
  elif (choice == 8):
    saveTeamDataToFileAndReset()
  elif (choice == 9):
    loadDataFromFile()
  else:
    print("Choose valid option: ")
  print()


def backupImplementation():
  ''' backup implementation'''
  while True:
    teamName = input("Enter team code ("+str(team_codes_list)+") : ")
    if teamName in teams:
      teamObject = teams[teamName]
      print("Calculating for Team: "+teamObject.name)
      bat1 = teamObject.runsScored
      bat2 = teamObject.runsConceded
      bowl1 = teamObject.ballsFaced
      bowl2 = teamObject.ballsDelivered
      print("Current NRR: "+str(round(teamObject.currentNRR(), 3)))
      # if batting first or "bowl" if bowling first
      while True:
        toss = input("Enter whether '(bat first/bowl first/compare)' in this match: ") 
        if(toss == "bat"):
          compare_table_set_target = []
          targetNRR = float(input("Enter the NRR to reach:"))
          ballsFaced = bowl1 + ballsPerInnings
          ballsDelivered = bowl2 + ballsPerInnings
          runsInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
          checkForAParticularScore = int(input("Enter custom value for runsScored: "))
          if(checkForAParticularScore>0):
            runsInFinalInnings.append(checkForAParticularScore)
          for runsScored in runsInFinalInnings:
            totalRunsScored = bat1 + runsScored
            marginOfVictory = 0  
            #targetNRR = (totalRunsScored/ballsFaced - (bat2 + runsScored - marginOfVictory)/ballsDelivered)*6
            marginOfVictory = bat2 + runsScored - ((totalRunsScored/ballsFaced) - (targetNRR/6))*ballsDelivered
            if(marginOfVictory > 0):
              marginOfVictory = math.ceil(marginOfVictory)
            else: 
              marginOfVictory = math.floor(marginOfVictory)
            print("After setting a target of: "+ str(runsScored)+" the team would require a margin of: "+ str(marginOfVictory)+" runs.")
            compare_table_set_target.append((runsScored, marginOfVictory))
          print("Results:******************")
          print(compare_table_set_target)
          print("**************************")
        elif(toss == "bowl"):
          compare_table_chase = []
          targetNRR = float(input("Enter the NRR to reach:"))
          ballsFaced = bowl1
          ballsDelivered = bowl2 + ballsPerInnings
          runsConcededInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
          checkForAParticularScore = int(input("Enter custom value for runsConceded: "))
          if(checkForAParticularScore>0):
            runsConcededInFinalInnings.append(checkForAParticularScore)
          for runsConceded in runsConcededInFinalInnings:
            totalRunsConceded = bat2 + runsConceded
            totalRunsScored = bat1 + runsConceded + 1 #atleast 1 more than the other team
            #targetNRR = ((totalRunsScored/(ballsFaced +toBeChasedInBalls) - (totalRunsConceded/ballsDelivered)))*6
            toBeChasedInBalls = (totalRunsScored/((targetNRR/6) + (totalRunsConceded/ballsDelivered))) - ballsFaced
            if(toBeChasedInBalls > 0):
              toBeChasedInBalls = math.floor(toBeChasedInBalls)
            else:
              toBeChasedInBalls = math.ceil(toBeChasedInBalls)
            print("After conceding: "+str(runsConceded)+" runs, it should be chased in: "+str(math.floor(toBeChasedInBalls))+ " balls")
            compare_table_chase.append((runsConceded, toBeChasedInBalls))
          print("Results:******************")
          print(compare_table_chase)
          print("**************************")
        elif(toss == "compare"):
          compare_table_chase = []
          compare_table_set_target = []
          oppTeamName = input("Enter opp. team code ("+str(team_codes_list)+") : ")
          myTeam = teamObject
          oppTeam = teams[oppTeamName]
          print("NRR of my team:" + str(myTeam.currentNRR()))
          print("NRR of opp. team:" + str(oppTeam.currentNRR()))
          print("==========================================")
          print("When my team bats first")
          runsInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
          checkForAParticularScore = int(input("Enter custom value for runs scored: "))
          if(checkForAParticularScore>0):
            runsInFinalInnings.append(checkForAParticularScore)
          for runsScoredInCurrentInnings in runsInFinalInnings:
            #TEAM1
            rs1 = myTeam.runsScored + runsScoredInCurrentInnings #+ marginOfVictory
            bf1 = myTeam.ballsFaced + ballsPerInnings
            rc1 = myTeam.runsConceded + runsScoredInCurrentInnings
            bd1 = myTeam.ballsDelivered + ballsPerInnings

            #TEAM2
            rs2 = oppTeam.runsScored + runsScoredInCurrentInnings
            bf2 = oppTeam.ballsFaced + ballsPerInnings
            rc2 = oppTeam.runsConceded + runsScoredInCurrentInnings #+ marginOfVictory
            bd2 = oppTeam.ballsDelivered + ballsPerInnings

            #(rs1+mv)/bf1 - rc1/bd1 = rs2/bf2 - (rc2 + mv)/bd2
            marginOfVictory = (rs2/bf2 + rc1/bd1 - rs1/bf1 - rc2/bd2)/(1/bf1 + 1/bd2)
            
            if(marginOfVictory > 0):
                marginOfVictory = math.ceil(marginOfVictory)
            else: 
                marginOfVictory = math.floor(marginOfVictory)
            print("After setting a target of: "+ str(runsScoredInCurrentInnings)+" ,We will need to win by " + str(marginOfVictory)+" runs.")
            compare_table_set_target.append((runsScoredInCurrentInnings,marginOfVictory))
          print("==========================================")
          print("When my team bowls first")
          runsConcededInFinalInnings = [i for i in range(expected_min_total,expected_max_total,runs_in_increments_of)]
          checkForAParticularScore = int(input("Enter custom value for runs conceded: "))
          if(checkForAParticularScore>0):
            runsConcededInFinalInnings.append(checkForAParticularScore)
          for runsConcededInCurrentInnings in runsConcededInFinalInnings:
            

            #TEAM1
            rs1 = myTeam.runsScored + runsConcededInCurrentInnings + 1
            bf1 = myTeam.ballsFaced #+ toBeChasedInBalls
            rc1 = myTeam.runsConceded + runsConcededInCurrentInnings
            bd1 = myTeam.ballsDelivered + ballsPerInnings

            #TEAM2
            rs2 = oppTeam.runsScored + runsConcededInCurrentInnings
            bf2 = oppTeam.ballsFaced + ballsPerInnings
            rc2 = oppTeam.runsConceded + runsConcededInCurrentInnings + 1 
            bd2 = oppTeam.ballsDelivered #+ toBeChasedInBalls

            #rs1/(bf1+toBeChasedInBalls) + rc2/(bd2+toBeChasedInBalls) = rs2/bf2 + rc1/bd1 
            # rs1/(bf1+toBeChasedInBalls) + rc2/(bd2+toBeChasedInBalls) = rs2/bf2 + rc1/bd1 

            c1 = rs1
            c2 = bf1
            c3 = rc2
            c4 = bd2
            c5 = rs2/bf2 + rc1/bd1 

            (ans1, ans2) = quadSolver(1,(c2+c4 - (c1+c3)/c5),(c2*c4 - (c1*c4+c2*c3)/c5))

            if ans1 == "NA" or (ans1<0 and ans2<0):
              print("After conceding a target of: "+ str(runsConcededInCurrentInnings)+" No possible chase will make NRR equal")
              continue
            if(ans1>0 and ans2>0):
              toBeChasedInBalls = min(ans1,ans2)
            elif(ans1>0):
              toBeChasedInBalls = ans1
            elif(ans2>0):
              toBeChasedInBalls = ans2

            if(toBeChasedInBalls > 0):
              toBeChasedInBalls = math.floor(toBeChasedInBalls)
            else:
              toBeChasedInBalls = math.ceil(toBeChasedInBalls)
            
            print("After conceding a target of: "+ str(runsConcededInCurrentInnings)+" ,We will need to chase it in " + str(toBeChasedInBalls)+" balls.")
            compare_table_chase.append((runsConcededInCurrentInnings,toBeChasedInBalls))
          print()
          print("compare_table_chase:",compare_table_chase)
          print()
          print("compare_table_set_target:",compare_table_set_target)
          print()        
        else:
          print("====================")
          break
    else:
      print("Invalid Team Code! Try Again!")