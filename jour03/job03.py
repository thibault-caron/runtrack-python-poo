class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut
    
    def marquer_comme_finie(self):
        """Change le statut de la tâche à 'terminée'."""
        self.statut = "terminée"
    
    def __str__(self):
        """Affiche la tâche sous forme de texte."""
        return f"Titre: {self.titre}, Description: {self.description}, Statut: {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouter_tache(self, tache):
        """Ajoute une tâche à la liste."""
        self.taches.append(tache)
    
    def supprimer_tache(self, titre):
        """Supprime une tâche de la liste par son titre."""
        self.taches = [tache for tache in self.taches if tache.titre != titre]  #and tache.description != description ?
    
    def marquer_comme_finie(self, titre):
        """Marque une tâche comme terminée en fonction du titre."""
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquer_comme_finie()
                break
    
    def afficher_liste(self):
        """Affiche toutes les tâches."""
        for tache in self.taches:
            print(tache)
    
    def filtrer_liste(self, statut):
        """Filtre les tâches par leur statut."""
        return [tache for tache in self.taches if tache.statut == statut]


if __name__ == "__main__":
    # Création des tâches
    tache1 = Tache("Acheter des courses", "Aller au magasin pour acheter des légumes et du pain")
    tache2 = Tache("Faire les devoirs", "Réviser la leçon de mathématiques et de français")
    tache3 = Tache("Nettoyer la maison", "Passer l'aspirateur et laver les sols", "terminée")

    # Création de la liste de tâches
    liste_taches = ListeDeTaches()

    # Ajouter les tâches à la liste
    liste_taches.ajouter_tache(tache1)
    liste_taches.ajouter_tache(tache2)
    liste_taches.ajouter_tache(tache3)

    # Afficher toutes les tâches
    print("Toutes les tâches :")
    liste_taches.afficher_liste()

    # Supprimer une tâche par son titre
    liste_taches.supprimer_tache("Faire les devoirs")
    print("\nAprès suppression de 'Faire les devoirs' :")
    liste_taches.afficher_liste()

    # Marquer une tâche comme terminée
    liste_taches.marquer_comme_finie("Acheter des courses")
    print("\nAprès avoir marqué 'Acheter des courses' comme terminée :")
    liste_taches.afficher_liste()

    # Afficher uniquement les tâches à faire
    print("\nTâches à faire :")
    taches_a_faire = liste_taches.filtrer_liste("à faire")
    for tache in taches_a_faire:
        print(tache)