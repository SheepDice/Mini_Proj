

class Morpion():
    def __init__(self):
        self.table = [" " for i in range(0, 9)]
        self.current_player = "O"
        self.played_case = []

    def play_one_turn(self):
        self.afficherPlateau()
        pos = int(input("Player %s, choisissez une position entre 1 et 9\n" % self.current_player))
        if pos in self.played_case :
            print("case déjà occupée")
            return
        else:
            self.table[pos - 1] = self.current_player
            self.played_case.append(pos)

    def check_result(self):
        if self.table[0] == self.table[1] == self.table[2] != " " or \
                self.table[3] == self.table[4] == self.table[5] != " " or \
                self.table[6] == self.table[7] == self.table[8] != " " or \
                self.table[0] == self.table[3] == self.table[6] != " " or \
                self.table[1] == self.table[4] == self.table[7] != " " or \
                self.table[2] == self.table[5] == self.table[8] != " " or \
                self.table[0] == self.table[4] == self.table[8] != " " or \
                self.table[2] == self.table[4] == self.table[6] != " " :
            self.afficherPlateau(self.current_player)
            return 1
        self.current_player = "X" if self.current_player == "O" else "O"
        return 0

    def afficherPlateau(self, gagnant=None):
        print(" " + self.table[0] + " | " + self.table[1] + " | " + self.table[2] + " ")
        print("---+---+---")
        print(" " + self.table[3] + " | " + self.table[4] + " | " + self.table[5] + " ")
        print("---+---+---")
        print(" " + self.table[6] + " | " + self.table[7] + " | " + self.table[8] + " ")
        if gagnant:
            print("""* Partie terminée : le joueur {0} a gagné. *""".format(gagnant))

    def game(self):
        while self.check_result() != 1:
            self.play_one_turn()

    def exec(self):
        self.game()