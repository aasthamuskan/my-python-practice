def get_runner_up_teams():
    n = int(input())
    teams = []

    for _ in range(n):
        team, score = input().split()
        score = int(score)
        teams.append((team, score))

    sorted_teams = sorted(teams, key=lambda x: x[1], reverse=True)
    highest_score = sorted_teams[0][1]
    runner_up_teams = [team[0] for team in sorted_teams if team[1] == sorted_teams[1][1]]

    return sorted(runner_up_teams)

# Example Usage
if __name__ == "__main__":
    runner_up_teams = get_runner_up_teams()
    print(", ".join(runner_up_teams))
