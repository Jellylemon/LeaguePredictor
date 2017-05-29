import json
import requests



class champ:
    def __init__(self, name, rate):
        self.name = name
        self.winRate = rate



#gives list of champions from highest to lowest winrate
def getStats (role, key):
    f = open(role + '.txt', 'w')
    pg = 1
    first = 1;
    Champions = []

    f.write(role + "\n\n")
    while(1):
        url = "http://api.champion.gg/stats/role/"
        url += role
        url += "/mostWinning?api_key="
        url += key
        url += "&page="
        url += (str(pg))
        url += "&limit="

        r = requests.get(url)
        r = r.json()

        if len(r['data']) == 0:
            break

        if (first == 1):
            bestWinRate = r['data'][0]['general']['winPercent']
            first = 0;

        worstWinRate = r['data'][len(r['data'])-1]['general']['winPercent']

        for i in range (len(r['data'])):
            Champions.append(champ(r['data'][i]['name'], r['data'][i]['general']['winPercent']))

        pg += 1

    if (bestWinRate - worstWinRate > 11.0):
        interval = (bestWinRate - worstWinRate)/6
        numTiers = 6
    else:
        interval = (bestWinRate - worstWinRate)/5
        numTiers = 5

    tiers = []
    #tiers are the numerical winrate thresholds

    for i in range(numTiers):
        if (i == numTiers - 1):
            tiers.append(worstWinRate)
        else:
            tiers.append(bestWinRate - (interval)*(i + 1))


    f.write("***************** Tier 1 *****************\n")
    j = 0
    for i in range(len(Champions)):
        if (Champions[i].winRate < tiers[j]):   #when champ winrate falls below tier threshold, create new tier and increment to next tier threshold
            j += 1
            f.write("\n")
            f.write("\n")
            f.write("***************** Tier " + str(j+1) + " *****************\n")

        f.write("%-25s%s" % (Champions[i].name, str(Champions[i].winRate)))
        f.write("\n")

key = input("Please enter your Developer API Key: ")
choices = ['top', 'jungle', 'middle', 'adc', 'support']
role = input("What role would you like to update?\nEnter: (top, jungle, middle, adc, support)\n")
while role not in choices:
	role = input("Please enter one of the following: (top, jungle, middle, adc, support)\n")

getStats(str(role), key)
