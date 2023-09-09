import re


class WrongNumberOfPlayersError(Exception):
    def __str__(self):
        return "WrongNumberOfPlayers"


class NoSuchStrategyError(Exception):
    def __str__(self):
        return "NoSuchStrategyError"


def rps_game_checker(player):
    check_rps = r"[R, P, S]"
    if re.match(check_rps, player[1]):
        return True
    else:
        raise NoSuchStrategyError


def rps_game_winner(players_array):
    try:
        if len(players_array) == 2:
            for i in players_array:
                rps_game_checker(i)
        else:
            raise WrongNumberOfPlayersError
    except WrongNumberOfPlayersError:
        raise WrongNumberOfPlayersError()

    if (
        players_array[0][1] == "P"
        and players_array[1][1] == "R"
        or players_array[0][1] == "R"
        and players_array[1][1] == "S"
        or players_array[0][1] == "S"
        and players_array[1][1] == "P"
    ):
        return f"{players_array[0][0]} {players_array[0][1]}"
    elif (
        players_array[0][1] == "P"
        and players_array[1][1] == "P"
        or players_array[0][1] == "R"
        and players_array[1][1] == "R"
        or players_array[0][1] == "S"
        and players_array[1][1] == "S"
    ):
        return f"{players_array[0][0]} {players_array[0][1]}"
    else:
        return f"{players_array[1][0]} {players_array[1][1]}"

#print(rps_game_winner([["player1", "P"], ["player2", "S"], ["player3", "S"]]))
#print(rps_game_winner([["player1", "P"], ["player2", "A"]]))
print(rps_game_winner([["player1", "P"], ["player2", "S"]]))
print(rps_game_winner([["player1", "P"], ["player2", "P"]]))
