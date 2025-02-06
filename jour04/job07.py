import random

# Classe Carte
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur  # La valeur de la carte (2 à 10, J, Q, K, A)
        self.couleur = couleur  # La couleur de la carte (Coeur, Carreau, Trèfle, Pique)

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

    def valeur_points(self):
        """Retourne la valeur en points de la carte."""
        if self.valeur in ['J', 'Q', 'K']:
            return 10
        elif self.valeur == 'A':
            return 1  # Par défaut l'As vaut 1, mais pourra être 11 selon les besoins.
        else:
            return int(self.valeur)

# Classe Jeu
class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()
        self.mains_joueur = []
        self.mains_croupier = []

    def creer_paquet(self):
        """Crée un paquet de 52 cartes."""
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        paquet = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]
        random.shuffle(paquet)  # Mélange le paquet pour le rendre aléatoire
        return paquet

    def distribuer_cartes(self):
        """Distribue 2 cartes au joueur et 2 au croupier."""
        self.mains_joueur = [self.paquet.pop(), self.paquet.pop()]
        self.mains_croupier = [self.paquet.pop(), self.paquet.pop()]

    def afficher_mains(self):
        """Affiche les mains du joueur et du croupier."""
        print("Main du Joueur:", [str(carte) for carte in self.mains_joueur])
        print("Main du Croupier:", [str(self.mains_croupier[0]), "??"])

    def calculer_total(self, main):
        """Calcule le total des points dans une main."""
        total = sum(carte.valeur_points() for carte in main)
        as_count = sum(1 for carte in main if carte.valeur == 'A')
        
        # Ajuste la valeur de l'As si nécessaire pour ne pas dépasser 21
        while total <= 11 and as_count:
            total += 10
            as_count -= 1
        
        return total

    def tour_joueur(self):
        """Le tour du joueur où il peut choisir de prendre une carte ou de passer."""
        while True:
            total_joueur = self.calculer_total(self.mains_joueur)
            print(f"Total du joueur: {total_joueur}")
            if total_joueur > 21:
                print("Le joueur a dépassé 21, il perd !")
                return False
            
            action = input("Voulez-vous 'prendre' ('1') une carte ou 'passer' ('0') ? ").lower()
            if action == 'prendre'or action == '1':
                self.mains_joueur.append(self.paquet.pop())
                print("Nouvelle carte:", self.mains_joueur[-1])
            elif action == 'passer' or action == '0':
                break
            else:
                print("Action invalide. Essayez 'prendre' ou 'passer'.")
        return True

    def tour_croupier(self):
        """Le tour du croupier. Il prend des cartes jusqu'à avoir au moins 17 points."""
        while True:
            total_croupier = self.calculer_total(self.mains_croupier)
            print(f"Total du croupier: {total_croupier}")
            if total_croupier >= 17:
                break
            else:
                print("Le croupier prend une carte...")
                self.mains_croupier.append(self.paquet.pop())
        return total_croupier

    def determiner_gagnant(self):
        """Détermine le gagnant."""
        total_joueur = self.calculer_total(self.mains_joueur)
        total_croupier = self.calculer_total(self.mains_croupier)

        print(f"Total du joueur: {total_joueur}")
        print(f"Total du croupier: {total_croupier}")
        
        if total_joueur > 21:
            print("Le joueur a perdu!")
        elif total_croupier > 21:
            print("Le croupier a perdu! Le joueur gagne!")
        elif total_joueur > total_croupier:
            print("Le joueur gagne!")
        elif total_joueur < total_croupier:
            print("Le croupier gagne!")
        else:
            print("Égalité!")
        return True
    
def rejouer():
    saisie = input("Voulez-vous rejouer (y/n)?: ").lower()
    if saisie == 'y'or saisie == '1':
        return True
    elif saisie == 'n' or saisie == '0':
        return False
    else:
        print("Action invalide. Essayez 'prendre' ou 'passer'.")
        rejouer()

def jouer():
    """Fonction principale pour jouer au jeu"""
    partie = True
    while partie == True:
        jeu = Jeu()
        jeu.distribuer_cartes()
        jeu.afficher_mains()

        if jeu.tour_joueur():
            total_croupier = jeu.tour_croupier()
            jeu.determiner_gagnant()
        partie = rejouer()


# Lancer une partie
jouer()
