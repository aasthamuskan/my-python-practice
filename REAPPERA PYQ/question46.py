def find_runner_up_teams(teams):
    teams.sort(key=lambda x: x[1], reverse=True)

    second_highest_score = teams[1][1]  

    runner_up_teams = [team[0] for team in teams if team[1] == second_highest_score]

    runner_up_teams.sort()

    return runner_up_teams

if __name__ == "__main__":
    num_teams = int(input("Enter the number of teams: "))
    teams = []

    for _ in range(num_teams):
        team_name, team_score = input().split()
        teams.append((team_name, int(team_score)))

    runner_up_teams = find_runner_up_teams(teams)
    print(",".join(runner_up_teams))

