import copy
import os

import constants


os.system("")

PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS

# Colors
CYB = "\033[33m\033[1m"
CRB = "\033[31m\033[1m"
CBB = "\033[34m\033[1m"
CVB = "\033[35m\033[1m"
CGB = "\033[32m\033[1m"
CWB = "\033[37m\033[1m"
CG = "\033[0m\033[32m"
CW = "\033[0m\033[37m"

# Styles
ST = "\033[0m"
B = "\033[1m"

# Emojis
BALL = "\U0001f3c0"


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def clean_data(players):
    for player in players:
        player["height"] = int(player["height"].split(" ")[0])
        player["experience"] = player["experience"] == "YES"
        player["guardians"] = player["guardians"].split(" and ")
    return players


def balance_teams(players):
    experience_sorted = sorted(
        players, key=lambda player: player['experience'])

    teams = {team: [] for team in TEAMS}

    for player in experience_sorted:
        team = min(teams, key=lambda team: len(teams[team]))
        teams[team].append(player)

    cls()

    display_stats(teams)


def display_stats(teams):
    while True:
        cls()
        print(f"\n{CYB}" + r"""
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿                ⣿⣿
⣿⣿   BASKETBALL   ⣿⣿
⣿⣿                ⣿⣿
⣿⣿   TEAM STATS   ⣿⣿
⣿⣿                ⣿⣿
⣿⣿ ⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆ ⣿⣿
⣿⣿  ⠸⣿⡇  ⣿⣿  ⢸⣿⠇  ⣿⣿
⣿⣿   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⣿⣿
⢿⣿⣿⡇ ⣿⣿  ⣿⣿  ⣿⣿ ⢸⣿⣿⡿
     ⢻⣿⣿⣿⣿⣿⣿⣿⣿⡟     
     ⠸⣿  ⢿⡿  ⣿⠇          
  """ + ST)

        print(f"{CG}\n{'₪' * 6} MAIN MENU {'₪' * 6}\n")

        print(f"{B} 1) Display Team Stats")
        print(f"{B} 2) Quit\n{ST}")

        try:
            selected_option = int(input(f"{CG}Enter an option: {B}"))

            if selected_option not in [1, 2]:
                raise ValueError
            elif selected_option == 1:
                cls()
            elif selected_option == 2:
                break
        except ValueError:
            continue

        print(f"{CG}{'₪' * 6} TEAMS {'₪' * 6}\n{B}")

        for i, team in enumerate(teams, 1):
            print(f" {i}) {team}")

        while True:
            try:
                selected_team = int(input(f"\n{CG}Enter team number: {B}"))
                if selected_team not in range(1, len(teams) + 1):
                    raise ValueError
            except ValueError:
                print(f"{CRB}Invalid team number!{ST}")
                continue
            break

        team_name = list(teams.keys())[selected_team - 1]
        stats_header = f"    Team {CYB}{team_name}{CG} Stats    "
        print(f"\n{CG}{'╔' + '═' * (len(stats_header) - 18) + '╗'}\n║{stats_header}║\n{'╙' + '─' * (len(stats_header) - 18) + '╜'}\n")

        team_players = teams[team_name]
        experienced_players = [
            player for player in team_players if player['experience']]
        inexperienced_players = [
            player for player in team_players if not player['experience']]
        players_names = [player['name'] for player in team_players]
        players_guardians = [
            guardian for player in team_players for guardian in player['guardians']]
        average_height = sum([player['height']
                             for player in team_players]) / len(team_players)

        print(f" {BALL} {CG}Total players: {CBB}{len(team_players)}{ST}")
        print(f" {BALL} {CG}Total experienced: {CVB}{len(experienced_players)}{ST}")
        print(
            f" {BALL} {CG}Total inexperienced: {CVB}{len(inexperienced_players)}{ST}")
        print(f" {BALL} {CG}Average height: {CWB}{average_height:.2f}{ST}")
        print(f"\n{CG}{'┉' * (len(stats_header) - 17)}")
        print(f"\n{CGB}Players:\n\n {BALL} {CBB}{', '.join(players_names)}{ST}")
        print(
            f"\n{CGB}Guardians:\n\n {BALL} {CBB}{', '.join(players_guardians)}{ST}\n")
        input(f"{CG}Press {B}ENTER{CG} to {CYB}continue{CW}…{ST}")

        cls()
    print(f"\nDoeiiiiiii!\n{ST}")


def main():
    shiny_players = clean_data(copy.deepcopy(PLAYERS))
    balance_teams(shiny_players)


if __name__ == "__main__":
    main()