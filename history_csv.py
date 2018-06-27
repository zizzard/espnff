# Import the league class and set the ID
from espnff import League

## User defined data
league_id = 1743204
years = [2014, 2015, 2016, 2017]

# For loop to go through every year
for year in years:

	# Create needed objects
	league = League(league_id, year)
	settings = league.settings
	teams = league.teams
	matchup_count = int(settings.team_count / 2)

	# Output information to file
	file_name = str(year) + "season.csv"
	output = open(file_name, 'w')

	# Generate team info
	header = "Team Name (Owner),Wins,Losses,Ties,Points For,Points Against\n"
	output.writelines(header)

	for team in teams:
		s = team.team_name + " (" + team.owner + ")"
		row = s + "," + str(team.wins) + "," + str(team.losses) + "," + str(team.ties) + "," + str(team.points_for) + "," + str(team.points_against) + "\n"
		output.writelines(row)


	if year == 2017:
		# Output information to file
		file_name = str(year) + "matchups.csv"
		output = open(file_name, 'w')

		last_week = settings.final_season_count
		header = "Week,Match ID,Home Team,Home Team Score, ,Away Team Score,Away Team\n"
		output.writelines(header)


		for week in range(last_week):
			time = week + 1
			scoreboard = league.scoreboard(week=time)

			for i in range(matchup_count):

				matchup = scoreboard[i]
				row = str(time) + "," + str(i) +"," + matchup.home_team.team_name + "," + str(matchup.home_score) + ", v ," + str(matchup.away_score) + "," + matchup.away_team.team_name + "\n"
				output.writelines(row)

			output.writelines("\n")

output.close()