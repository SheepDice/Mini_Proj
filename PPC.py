import random


class PPC():
    def __init__(self):
        self.bot_tool = 0
        self.player_tool = 0
        self.score_bot = 0
        self.score_player = 0
        self.game_mode = 0

    def choose_mode(self):
        self.game_mode = 0
        while self.game_mode not in (1, 2):
            print("Choisissez un mode de jeu : \n1. Trois points\n2. Trois manches")
            self.game_mode = int(input("1 ou 2 ?  "))

    def play_one_turn(self):
        self.bot_tool = random.randint(1,3)
        self.player_tool = int(input("1. Pierre ? 2.Papier ? 3.Ciseau ?"))
        if (self.bot_tool == 1 and self.player_tool == 2) or  (self.bot_tool == 2 and self.player_tool == 3) or \
                (self.bot_tool == 3 and self.player_tool == 1):
            print("bien ouej")
            self.score_player += 1
        else:
            print("looser")
            self.score_bot += 1
        print("LES SCORES :\n1. PLAYER : %d\nBOT : %d\n" % (self.score_player, self.score_bot))

    def three_turns(self):
        for i in range(0, 3):
            self.play_one_turn()
            if self.score_bot == 2:
                print ("Dommage, vous avez perdu, looser")
                return
            elif self.score_player == 2:
                print ("Bien ouej frero, c'est win")
                return

    def three_points(self):
        while (self.score_player < 3 and self.score_bot < 3):
            self.play_one_turn()
        if self.score_bot > self.score_player :
            print ("Dommage, vous avez perdu, looser")
        else :
            print ("Bien ouej frero, c'est win")

    def game(self):
        while (True):
            self.choose_mode()
            if self.game_mode == 1:
                self.three_points()
            else:
                self.three_turns()
            continuer = int(input("Continuer ?\n1- Oui\n2- Non\n"))
            if continuer == 2:
                break
            self.score_bot = 0
            self.score_player = 0
