class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        """Attaque l'adversaire et lui enlève 10 points de vie"""
        if adversaire.vie > 0:
            degats = 10
            adversaire.vie -= degats
            print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégât!")
        else:
            print(f"{adversaire.nom} est déjà hors de combat!")
    
    def verifier_sante(self):
        """Vérifie si le personnage est toujours en vie"""
        return self.vie > 0
    
    def afficher_etat(self):
        """Affiche l'état de santé du personnage"""
        print(f"{self.nom} - Vie: {self.vie}")


class Jeu:
    def __init__(self):
        self.niveau = 1
    
    def choisir_niveau(self):
        """Demander au joueur le niveau de difficulté"""
        print("Choisissez un niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile):")
        niveau = int(input())
        if niveau == 1:
            self.niveau = 1
        elif niveau == 2:
            self.niveau = 2
        elif niveau == 3:
            self.niveau = 3
        else:
            print("Niveau non valide, niveau par défaut choisi (1).")
            self.niveau = 1
    
    def lancer_jeu(self):
        """Lancer le jeu en fonction du niveau"""
        # Points de vie par défaut pour le joueur et l'ennemi
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 80
        elif self.niveau == 3:
            vie_joueur = 60
            vie_ennemi = 100
        
        # Création des personnages
        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)
        
        # Lancer le combat
        self.combattre(joueur, ennemi)
    
    def combattre(self, joueur, ennemi):
        """Gère le combat entre le joueur et l'ennemi"""
        tour = 1
        while joueur.verifier_sante() and ennemi.verifier_sante():
            print(f"\n--- Tour {tour} ---")
            joueur.afficher_etat()
            ennemi.afficher_etat()

            # Tour du joueur
            print(f"\n{joueur.nom}, c'est à vous d'attaquer!")
            joueur.attaquer(ennemi)
            if not ennemi.verifier_sante():
                print(f"{ennemi.nom} est tombé ! {joueur.nom} gagne !")
                break
            
            # Tour de l'ennemi
            if ennemi.verifier_sante():
                print(f"\n{ennemi.nom} attaque !")
                ennemi.attaquer(joueur)
                if not joueur.verifier_sante():
                    print(f"{joueur.nom} est tombé ! {ennemi.nom} gagne !")
                    break
            
            tour += 1


if __name__ == "__main__":
    # Initialiser le jeu
    jeu = Jeu()

    # Choisir le niveau
    jeu.choisir_niveau()

    # Lancer le jeu
    jeu.lancer_jeu()
