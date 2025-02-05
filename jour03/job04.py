class Joueur:
    def __init__(self, nom, numero, position):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__buts = 0
        self.__passes_decisives = 0
        self.__cartons_jaunes = 0
        self.__cartons_rouges = 0

    # accesseurs
    def get_nom(self):
        return self.__nom
    
    # mutateurs
    def set_titre(self, nouv_titre):
        self.__titre = nouv_titre
    
    def set_auteur(self, nouv_auteur):
        self.__auteur = nouv_auteur

    def marquer_but(self):
        """Incrémente le nombre de buts marqués par le joueur"""
        self.__buts += 1
    
    def effectuer_passe_decisive(self):
        """Incrémente le nombre de passes décisives du joueur"""
        self.__passes_decisives += 1
    
    def recevoir_carton_jaune(self):
        """Incrémente le nombre de cartons jaunes reçus"""
        self.__cartons_jaunes += 1
    
    def recevoir_carton_rouge(self):
        """Incrémente le nombre de cartons rouges reçus"""
        self.__cartons_rouges += 1
    
    def afficher_statistiques(self):
        """Affiche les statistiques du joueur"""
        print(f"\nNom: {self.__nom}, Numéro: {self.__numero}, Position: {self.__position}\n"
            f"Buts marqués: {self.__buts}, Passes décisives: {self.__passes_decisives}\n"
            f"Cartons jaunes: {self.__cartons_jaunes}, Cartons rouges: {self.__cartons_rouges}")
        print("-" * 30)


class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__liste_joueurs = []
    
    def ajouter_joueur(self, joueur):
        """Ajoute un joueur à l'équipe"""
        self.__liste_joueurs.append(joueur)
    
    def afficher_statistiques_joueurs(self):
        """Affiche les statistiques de tous les joueurs de l'équipe"""
        print(f"Statistiques des joueurs de l'équipe {self.__nom} :")
        for joueur in self.__liste_joueurs:
            joueur.afficher_statistiques()
    
    def mettre_a_jour_statistiques_joueur(self, nom_joueur, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
        """Met à jour les statistiques d'un joueur spécifique"""
        for joueur in self.__liste_joueurs:
            if joueur.get_nom() == nom_joueur:
                i = 0
                while i < buts:
                    joueur.marquer_but()
                    i += 1
                i = 0
                while i < passes:
                    joueur.effectuer_passe_decisive()
                    i += 1
                i = 0
                while i < cartons_jaunes:
                    joueur.recevoir_carton_jaune()
                    i += 1
                i = 0
                while i < cartons_rouges:
                    joueur.recevoir_carton_jaune()
                    i += 1
                i = 0
                break


if __name__ == "__main__":
    # Création des joueurs
    joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
    joueur2 = Joueur("Sergio Ramos", 4, "Défenseur")
    joueur3 = Joueur("Kylian Mbappé", 7, "Attaquant")
    joueur4 = Joueur("Marco Verratti", 6, "Milieu de terrain")

    # Création de l'équipe
    equipe = Equipe("Paris Saint-Germain")

    # Ajouter les joueurs à l'équipe
    equipe.ajouter_joueur(joueur1)
    equipe.ajouter_joueur(joueur2)
    equipe.ajouter_joueur(joueur3)
    equipe.ajouter_joueur(joueur4)

    # Afficher les statistiques avant le match
    equipe.afficher_statistiques_joueurs()

    # Simuler un match
    joueur1.marquer_but()  # Messi marque un but
    joueur2.recevoir_carton_jaune()  # Ramos reçoit un carton jaune
    equipe.mettre_a_jour_statistiques_joueur("Kylian Mbappé", buts=1)  # Mbappé marque un but
    joueur4.effectuer_passe_decisive()  # Verratti effectue une passe décisive
    joueur2.recevoir_carton_rouge()  # Ramos reçoit un carton rouge
    # equipe.mettre_a_jour_statistiques_joueur("Sergio Ramos", cartons_jaunes=1, cartons_rouges=1)  # autre façon de faire    

    # Afficher les statistiques après le match
    print("\nAprès le match :")
    equipe.afficher_statistiques_joueurs()
