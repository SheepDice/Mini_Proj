import random

class le_juste_prix:
    def __init__(self):
        self.number_to_guess = random.randint(0, 100)
        self.propal = -1;

    def boucle_de_jeu(self):
        print("Un nombre a été défini entre 0 et 100\nA vous de le deviner.")
        while(self.propal != self.number_to_guess):
            self.propal = int(input("Quelle est votre proposition ?"))
            if self.propal == self.number_to_guess:
                print("Bravo vous avez trouvé !")
                break
            elif self.propal > self.number_to_guess:
                print("Essayez encore, c'est moins")
            else:
                print("Essayez encore, c'est plus")