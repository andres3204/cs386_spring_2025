from dataclasses import dataclass

@dataclass
class GameModel:
    _player1: str = "Player 1"
    _player2: str = "Player 2"

    def get_player1(self):
        return self._player1

    def set_player1(self, name: str):
        self._player1 = name

    def get_player2(self):
        return self._player2

    def set_player2(self, name: str):
        self._player2 = name
