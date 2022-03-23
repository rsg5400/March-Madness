import requests
from bs4 import BeautifulSoup
import pdb

url = 'https://www.teamrankings.com/ncb/trends/win_trends/?sc=all_games'

r=requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

## finds the table
cbb_table = soup.find('table', class_ = 'tr-table datatable scrollable')
## empty dictionary {Team Name: [wins, loses]}
teams_record = {}
## searches tbody and then tr
for team in cbb_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        ## this finds team names
        team = row.find('td', class_ = 'nowrap').text
        ## This finds there records wins-loses-ties
        record= row.find_all('td', class_ = 'text-right')[0].text
        ## split and seperated wins and lsoes
        record = record.split('-')
        wins = int(record[0])
        loses = int(record[1])
        ## {team name: [team wins, team loses]}
        teams_record[team] = [wins,loses]





url = 'https://www.teamrankings.com/ncb/trends/win_trends/?sc=is_ncaa'

r=requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')


mm_table = soup.find('table', class_ = 'tr-table datatable scrollable')

## list of teams in march madness


# for team in mm_table.find_all('tbody'):
#     rows = team.find_all('tr')
#     for row in rows:
#         team = row.find('td', class_ = 'nowrap').text
#         ## list of teams in march madnesss
#         mm_teams_list.append(team)
# print(mm_teams_list)




mm_teams_list = ["Gonzaga","Georgia St","Boise State","Memphis","Connecticut", "N Mex State","Arkansas", "Vermont",
"Alabama","Notre Dame","Texas Tech", "Montana St", "Michigan St", "Davidson", "Duke", "CS Fullerton",
"Baylor", "Norfolk St", "N Carolina", "Marquette", "St Marys", "Indiana", "UCLA",
"Akron", "Texas", "VA Tech", "Purdue", "Yale", "Murray St", "San Francisco", "Kentucky", "St Peters",
"Arizona", "Wright State", "Seton Hall", "TX Christian", "Houston", "UAB", "Illinois", "Chattanooga","Colorado St",
"Michigan", "Tennessee", "Longwood", "Ohio State", "Loyola-Chi", "Villanova", "Delaware","Kansas",
"TX Southern", "San Diego St", "Creighton", "Iowa", "Richmond", "Providence", "S Dakota St", "LSU",
"Iowa State", "Wisconsin", "Colgate", "USC", "Miami (FL)", "Auburn", "Jksnville St"]



## Team class that works as a node class
class Team:

    def __init__(self, team):
        if team in mm_teams_list:



            self.team = team
            ## team wins
            self.wins = teams_record[team][0]
            ## team loses
            self.loses = teams_record[team][1]

            self.next = None

            self.prev = None

class CreateBracket:

    def __init__(self):
        self.head = None
        self.tail = None


    def __str__(self):

        """     should print out
        Gonzaga vs SDSU

        Baylor vs villanova """


        temp  = self.head
        out = []
        while temp != None:
            out.append(temp.team)
            temp = temp.next


        return " VS ".join(out)



        # i = 0
        # while i < len(out):
        #     try:
        #         print('{} vs {} \n'.format(out[i], out[i+1]))
        #     except:
        #         print("not an even amount of teams")
        #     i +=2

    __repr__=__str__


    def __len__(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count +=1
        return count

    def add(self, team):
        new_team = Team(team.team)

        if self.head == None:
            self.head = new_team
            self.tail = new_team
            self.head.next = None
            self.head.prev = None

        else:
            # current = self.head

            # while current.next != None:
            #     current = current.next
            # new_team.prev = self.tail
            # current.next = new_team
            # new_team.next = None
            # new_team = self.tail

            new_team.prev = self.tail
            self.tail.next = new_team
            self.tail = new_team
            self.tail.next = None


    def play(self):
        current = self.head

        while current.next.next != None:






            if current.wins > current.next.wins:
                current.next.next.prev = current
                current.next = current.next.next

                current = current.next

            else:
                if current.prev == None:
                 #   pdb.set_trace()`

                    current = current.next
                    current.prev = None
                    self.head = current
                    current = current.next

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                    current = current.next.next


        if current.wins > current.next.wins:
            current.next = None


        else:
            try:
                current.prev.next = current.next
                current.next.prev = current.prev

            except:
                current = current.next
                current.prev = None
                current.next = None
                self.head = current



bracket = CreateBracket()

for team in mm_teams_list:
    bracket.add(Team(team))

#bracket.play()














