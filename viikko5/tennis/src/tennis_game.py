class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.love = 0
        self.fifteen = 1
        self.thirty = 2
        self.forty = 3
        self.score = ""
        self.temp_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.score1 = self.score1 + self.fifteen
        else:
            self.score2 = self.score2 + self.fifteen

    def get_score(self):
        if self.score1 == self.score2:
            self.score = self.tie()
        elif self.score1 >= 4 or self.score2 >= 4:
            minus_result = self.score1 - self.score2
            self.score = self.win(minus_result)
        else:
            self.score = self.get_score2()
        return self.score

    def tie(self):
        if self.score1 == self.love:
            self.score = "Love-All"
        elif self.score1 == self.fifteen:
            self.score = "Fifteen-All"
        elif self.score1 == self.thirty:
            self.score = "Thirty-All"
        else:
            self.score = "Deuce"
        return self.score

    def win(self, minus_result):
        if minus_result == self.fifteen:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= self.thirty:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"
        return self.score

    def get_score2(self):
        for i in range(1, 3):
            if i == 1:
                self.temp_score = self.score1
            else:
                self.score = self.score + "-"
                self.temp_score = self.score2
            if self.temp_score == self.love:
                self.score = self.score + "Love"
            elif self.temp_score == self.fifteen:
                self.score = self.score + "Fifteen"
            elif self.temp_score == self.thirty:
                self.score = self.score + "Thirty"
            elif self.temp_score == self.forty:
                self.score = self.score + "Forty"
        return self.score
