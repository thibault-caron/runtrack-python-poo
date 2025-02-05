class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    # accesseurs
    def get_nom(self):
        return self.__nom
    
    def get_vie(self):
        return self.__vie
    
        # mutateurs
    def set_vie(self, nouv_vie):
        self.__vie = nouv_vie
    
    def attaquer(self, adversaire):
        """Attaque l'adversaire et lui enlève 10 points de vie"""
        if adversaire.get_vie() > 0:
            degats = 10
            vie_restante = adversaire.get_vie() - degats
            adversaire.set_vie(vie_restante)
            print(f"{self.__nom} attaque {adversaire.get_nom()} et lui inflige {degats} points de dégât!")
        else:
            print(f"{adversaire.get_nom()} est déjà hors de combat!")
    
    def verifier_sante(self):
        """Vérifie si le personnage est toujours en vie"""
        return self.__vie > 0
    
    def afficher_etat(self):
        """Affiche l'état de santé du personnage"""
        print(f"{self.__nom} - Vie: {self.__vie}")


class Jeu:
    def __init__(self):
        self.__niveau = 1
    
    def choisir_niveau(self):
        """Demander au joueur le niveau de difficulté"""
        print("Choisissez un niveau de difficulté (1: Facile, 2: Moyen, 3: Difficile):")
        niveau = int(input())
        if niveau == 1:
            self.__niveau = 1
        elif niveau == 2:
            self.__niveau = 2
        elif niveau == 3:
            self.__niveau = 3
        else:
            print("Niveau non valide, niveau par défaut choisi (1).")
            self.__niveau = 1
    
    
    def lancer_jeu(self):
        """Lancer le jeu en fonction du niveau"""
        # Points de vie par défaut pour le joueur et l'ennemi
        if self.__niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.__niveau == 2:
            vie_joueur = 80
            vie_ennemi = 80
        elif self.__niveau == 3:
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
            print(f"\n{joueur.get_nom()}, c'est à vous d'attaquer!")
            joueur.attaquer(ennemi)
            if not ennemi.verifier_sante():
                print(f"{ennemi.get_nom()} est tombé ! {joueur.get_nom()} gagne !")
                break
            
            # Tour de l'ennemi
            if ennemi.verifier_sante():
                print(f"\n{ennemi.get_nom()} attaque !")
                ennemi.attaquer(joueur)
                if not joueur.verifier_sante():
                    print(f"{joueur.get_nom()} est tombé ! {ennemi.get_nom()} gagne !")
                    break
            
            tour += 1


if __name__ == "__main__":
    # Initialiser le jeu
    jeu = Jeu()

    # Choisir le niveau
    jeu.choisir_niveau()

    # Lancer le jeu
    jeu.lancer_jeu()
