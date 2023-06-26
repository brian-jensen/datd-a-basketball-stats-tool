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
    exp_sort = sorted(players, key=lambda player: player['experience'])
    teams = {team: [] for team in TEAMS}
    for player in exp_sort:
        team = min(teams, key=lambda team: len(teams[team]))
        teams[team].append(player)
    cls()
    main_menu(teams)


def handle_errors(err):
    err_msg = f"{CRB}{err} was not a valid option. Please try again.{ST}"
    err_msg = err_msg.replace("invalid literal for int() with base 10: ", "")
    print(err_msg)


def main_menu(teams):
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
    while True:
        print(f"{CG}\n{'₪' * 6} MAIN MENU {'₪' * 6}\n")
        print(f"{B} 1) Display Team Stats")
        print(f"{B} 2) Quit\n{ST}")
        try:
            selected_option = int(input(f"{CG}Enter an option: {B}"))
            if selected_option not in [1, 2]:
                raise ValueError(selected_option)
            elif selected_option == 1:
                cls()
                display_stats(teams)
            elif selected_option == 2:
                print(f"\nDoeiiiiiii!\n{ST}")
                break
        except ValueError as err:
            cls()
            handle_errors(err)
            continue


def display_stats(teams):
    while True:
        print(f"\n{CG}{'₪' * 6} TEAMS {'₪' * 6}\n{B}")
        for i, team in enumerate(teams, 1):
            print(f" {i}) {team}")
        try:
            selected_team = int(input(f"\n{CG}Enter team number: {B}"))
            if selected_team not in range(1, len(teams) + 1):
                raise ValueError(selected_team)
        except ValueError as err:
            cls()
            handle_errors(err)
            continue

        team_name = list(teams.keys())[selected_team - 1]
        stats_header = f"    Team {CYB}{team_name}{CG} Stats    "
        print(f"\n{CG}{'╔' + '═' * (len(stats_header) - 18) + '╗'}")
        print(f"║{stats_header}║")
        print(f"{'╙' + '─' * (len(stats_header) - 18) + '╜'}\n")

        players_raw = teams[team_name]
        players = sorted(
            players_raw, key=lambda player: player['height'], reverse=True)
        exp = [player for player in players if player['experience']]
        no_exp = [player for player in players if not player['experience']]
        names = [player['name'] for player in players]
        names_height = [f"{CBB}{name}{ST} {CW}{player['height']}\"{ST}"
                        for name, player in zip(names, players)]
        guardians = [
            guardian for player in players for guardian in player['guardians']]
        average_height = sum([player['height']
                             for player in players]) / len(players)
        print(f" {BALL} {CG}Total players: {CBB}{len(players)}{ST}")
        print(f" {BALL} {CG}Total experienced: {CVB}{len(exp)}{ST}")
        print(f" {BALL} {CG}Total inexperienced: {CVB}{len(no_exp)}{ST}")
        print(f" {BALL} {CG}Average height: {CWB}{average_height:.2f}{ST}")
        print(f"\n{CG}{'┉' * (len(stats_header) - 17)}")
        print(f"\n{CGB}Players:\n\n {BALL} {', '.join(names_height)}{ST}")
        print(f"\n{CGB}Guardians:\n")
        print(f" {BALL} {CBB}{', '.join(guardians)}{ST}\n")
        input(f"{CG}Press {B}ENTER{CG} to {CYB}continue{CW}…{ST}")
        cls()


def main():
    shiny_players = clean_data(copy.deepcopy(PLAYERS))
    balance_teams(shiny_players)


if __name__ == "__main__":
    main()
