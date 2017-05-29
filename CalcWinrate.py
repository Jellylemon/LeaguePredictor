import json
import requests


class Role:


    def __init__(self, name):
        self.name = name
        self.champs = {}


class Champion:


    def __init__ (self, name, winrate):
        self.name = name
        self.winRate = winrate


def readRoleData(file, role):
    for line in file:
        line = line.strip().split()

        if len(line) != 0  and line[0] != role.name and line[0][0] != '*':
            tempName = line[:len(line)-1]
            tempWinRate = line[len(line)-1]
            tempName = " ".join(tempName).lower()
            tempChamp = Champion(tempName, tempWinRate)
            role.champs[tempName] = tempChamp



ROLES = ['top', 'jungle', 'middle', 'adc', 'support']
roles = {}
tempRole = Role('top')
roles['top'] = tempRole
tempRole = Role('jungle')
roles['jungle'] = tempRole
tempRole = Role('middle')
roles['middle'] = tempRole
tempRole = Role('adc')
roles['adc'] = tempRole
tempRole = Role('support')
roles['support'] = tempRole

topFile = open("top.txt", "r")
readRoleData(topFile, roles['top'])
topFile.close()

jungleFile = open("jungle.txt", "r")
readRoleData(jungleFile, roles['jungle'])
jungleFile.close()

middleFile = open("middle.txt", "r")
readRoleData(middleFile, roles['middle'])
middleFile.close()

adcFile = open("adc.txt", "r")
readRoleData(adcFile, roles['adc'])
adcFile.close()

supportFile = open("support.txt", "r")
readRoleData(supportFile, roles['support'])
supportFile.close()

t1wr = 0
t2wr = 0
print ("""Welcome to League Predictor!

This Program will predict which team will win based on
each champion's current winrates and give you a team winrate percentage.

(Note: Some off-meta champions' winrates are unavailable
       and the program will not be able to predict the winning team)

          """)

print("Please enter the Champions on Team 1:")
for role in ROLES:
    line = input("  Enter champion's name (" + role + "): ")
    line = line.strip().split()
    line = ' '.join(line).lower()

    while line not in roles[role].champs:
        if line == "quit":
            exit()
        line =  input("""     Error - Champion not found!
                 Please re-enter: """)
        line = line.strip().split()
        line = ' '.join(line).lower()

    t1wr += float(roles[role].champs[line].winRate)

print (" ")
print ("Please enter the Champions on Team 2:")
for role in ROLES:
    line = input("  Enter champion's name (" + role + "): ")
    line = line.strip().split()
    line = ' '.join(line).lower()

    while line not in roles[role].champs:
        if line == "quit":
            exit()
        line =  input("""     Error 404 - Champion not found!
                Please re-enter: """)
        line = line.strip().split()
        line = ' '.join(line).lower()

    t2wr += float(roles[role].champs[line].winRate)

t1wr /= 5
t2wr /= 5

print (" ")
if t1wr > t2wr:
    print("Team 1 wins with a higher Win Rate of " + str(t1wr))
else:
    print("Team 2 wins with a higher Win Rate of " + str(t2wr))

