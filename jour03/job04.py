class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_but(self):
        """Incrémente le nombre de buts marqués par le joueur"""
        self.buts += 1
    
    def effectuer_passe_decisive(self):
        """Incrémente le nombre de passes décisives du joueur"""
        self.passes_decisives += 1
    
    def recevoir_carton_jaune(self):
        """Incrémente le nombre de cartons jaunes reçus"""
        self.cartons_jaunes += 1
    
    def recevoir_carton_rouge(self):
        """Incrémente le nombre de cartons rouges reçus"""
        self.cartons_rouges += 1
    
    def afficher_statistiques(self):
        """Affiche les statistiques du joueur"""
        print(f"\nNom: {self.nom}, Numéro: {self.numero}, Position: {self.position}\n"
            f"Buts marqués: {self.buts}, Passes décisives: {self.passes_decisives}\n"
            f"Cartons jaunes: {self.cartons_jaunes}, Cartons rouges: {self.cartons_rouges}")
        print("-" * 30)


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []
    
    def ajouter_joueur(self, joueur):
        """Ajoute un joueur à l'équipe"""
        self.liste_joueurs.append(joueur)
    
    def afficher_statistiques_joueurs(self):
        """Affiche les statistiques de tous les joueurs de l'équipe"""
        print(f"Statistiques des joueurs de l'équipe {self.nom} :")
        for joueur in self.liste_joueurs:
            joueur.afficher_statistiques()
    
    def mettre_a_jour_statistiques_joueur(self, nom_joueur, buts=0, passes=0, cartons_jaunes=0, cartons_rouges=0):
        """Met à jour les statistiques d'un joueur spécifique"""
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                joueur.buts += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges
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
