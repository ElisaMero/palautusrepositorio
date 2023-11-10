import requests
from player import Player


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, country):
        new_list = []
        for i in self.players:
            if country == i.nationality:
                new_list.append(i)
        new_list.sort(key=lambda player: player.results, reverse=True)

        return new_list


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url)
        players_data = response.json()
        players = []

        for player_dict in players_data:
            player = Player(player_dict)
            players.append(player)
        return players
