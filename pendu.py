import requests
from bs4 import BeautifulSoup
import random
import urllib
import unidecode


class Pendu():
    def __init__(self):
        self.word_to_find = ""
        self.word_to_complete = [ "_" for i in range(len(self.word_to_find))]
        self.hanged = 0

    def prepare_game(self):
        while(len(self.word_to_find) < 5 or not self.check_word(self.word_to_find)):
            self.find_rand_word()
        self.word_to_complete = ["_" for i in range(len(self.word_to_find))]
        self.find_the_place("-")
        self.find_the_place("'")

    def find_the_place(self, new_letter):
        for i, l in enumerate(self.word_to_find):
            if l == new_letter:
                self.word_to_complete[i] = new_letter

    def launch_game(self):
        self.prepare_game()
        print("The word contain %d letters" % len(self.word_to_find))
        while(True):
            print("".join(self.word_to_complete))
            new_letter = input("Which letter do you want to try ?\n")
            if len(new_letter) > 1 and new_letter.lower() == "".join(self.word_to_find).lower():
                print("Ah tu tentes un mot hein ? Bah ok t'as raison c'est %s. Gros tarba" % new_letter)
                break
            elif len(new_letter) > 1 and new_letter.lower() != "".join(self.word_to_find).lower():
                print("Ah tu tentes un mot hein ? Bah non c'est pas ça, tu vas faire quoi ?")
                continue
            if new_letter in self.word_to_find:
                print("Well done, there is %s in the word" % new_letter)
                self.find_the_place(new_letter)
            else:
                print("Nop. This is sad, you will die soon, son.")
                self.hanged += 1
                if self.hanged == 5:
                    print("Sad bro, c'est perdu. C'était %s" % self.word_to_find)
                    break
            if "_" not in self.word_to_complete:
                print("Congrat ! The word was %s !" % "".join(self.word_to_complete))
                break

    def find_label_article(self):
        url = "https://fr.wikipedia.org/wiki -/Wikipédia:Accueil_principal"
        response = requests.get(url)
        if not response.ok:
            print("Pas de wiki")
            exit()

        soup = BeautifulSoup(response.text, 'html.parser')
        acceuil_cadre = soup.find('div', {'class': 'mw-page-container'}). \
            find('div', {'class': 'mw-page-container-inner'}). \
            find('div', {'class': 'mw-content-container'}). \
            find('main', {'id': 'content'}). \
            find('div', {'id': 'bodyContent'}). \
            find('div', {'id': 'mw-content-text'}). \
            find('div', {'class': 'mw-parser-output'}). \
            find('div', {'id': 'accueil_2017_contenu'}). \
            find('div', {'class': 'portail-gauche'}). \
            find('div', {'class': 'accueil_2017_cadre'})

        a_list = acceuil_cadre.find('p').findAll('a')
        return a_list

    def find_rand_word(self):
        a_list = self.find_label_article()
        rand_num = random.randint(0,len(a_list) - 1)
        url = "https://fr.wikipedia.org" + a_list[rand_num]['href']
        response = requests.get(url)
        if not response.ok:
            print("C'est la merde")
            exit()
        soup = BeautifulSoup(response.text, 'html.parser')
        content_page = soup.find('div', {'class': 'mw-page-container'}). \
            find('div', {'class': 'mw-page-container-inner'}). \
            find('div', {'class': 'mw-content-container'}). \
            find('main', {'id': 'content'}). \
            find('div', {'id': 'bodyContent'}). \
            find('div', {'id': 'mw-content-text'}). \
            find('div', {'class': 'mw-parser-output'}).\
            find('p', recursive=False)
        list_of_words = content_page.text.split(" ")
        rand_num = random.randint(0, len(list_of_words) - 1)
        self.word_to_find = list_of_words[rand_num]
        self.clean_word()

    def clean_word(self):
        if "'" in self.word_to_find:
            self.word_to_find = self.word_to_find[2:]
        if "." in self.word_to_find:
            self.word_to_find = self.word_to_find[:-1]
        self.word_to_find = unidecode.unidecode(self.word_to_find)

    def check_word(self, word):
        url = "http://www.pallier.org/extra/liste.de.mots.francais.frgut.txt"
        urllib.request.urlretrieve(url, "./words.txt")

        with open('./words.txt', encoding='utf-8') as file :
            words = set(line.strip() for line in file)
            if word in words:
                return True
            return False




    def exec(self):
        self.launch_game()
