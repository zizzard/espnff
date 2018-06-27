# Import table printing
from prettytable import PrettyTable

# Import the league class and set the ID
from espnff import League
league_id = 1743204
league_id = 1743205

# Output information to file
output = open('output.txt', 'w')

# An array for the years
years = [2014, 2015, 2016, 2017]

# Output league name
s = "######################\n##   " + League(league_id, 2018).settings.name + "   ##\n######################\n"
output.writelines(s)

# For loop to go through every year
for year in years:
	league = League(league_id, year)
	settings = league.settings
	matchup_count = int(settings.team_count / 2)

	# Print out year header
	s = "\n########\n# " + str(year) + " #\n########\n\n"
	output.writelines(s)

	# Hold all teams in teams array
	teams = league.teams

	# Generate team info
	table = PrettyTable(['Team Name (Owner)', 'Wins', 'Losses', 'Ties', 'Points For', 'Points Against'])
	for team in teams:
		s = team.team_name + " (" + team.owner + ")"
		table.add_row([s, team.wins, team.losses, team.ties, team.points_for, team.points_against])

	# Print team info
	output.write(table.get_string())

	if year == 2017:
		
		champion = ""
		last_week = settings.final_season_count
		for week in range(last_week):

			table = PrettyTable(['Matchup ID', 'Home Team', 'Home Team Score', ' ', 'Away Team Score', 'Away Team'])

			time = week + 1
			s = "\n\nWeek " + str(time) + "\n"
			output.writelines(s)

			scoreboard = league.scoreboard(week=time)

			for i in range(matchup_count):

				matchup = scoreboard[i]

				if i == 0 and time == last_week:
					if matchup.home_score > matchup.away_score:
						champion = matchup.home_team.team_name
					else:
						champion = matchup.away_team.team_name


				
				table.add_row([i, matchup.home_team.team_name, matchup.home_score, 'v', matchup.away_score, matchup.away_team.team_name])

			output.write(table.get_string())

		champion = "\n\nCHAMPION: " + champion
		output.writelines(champion)
		output.writelines("\n")

output.close()