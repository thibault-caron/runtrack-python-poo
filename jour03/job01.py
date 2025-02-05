class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants
    
    def get_habitants(self):
        return self.__nombre_habitants
    
    def get_nom(self):
        return self.__nom
    
    def ajouter_habitant(self):
        self.__nombre_habitants += 1
    
    def __str__(self):
        return f"Ville: {self.__nom}, Habitants: {self.__nombre_habitants}"


class Personne:
    def __init__(self, nom, age, instance_ville):
        self.__nom = nom
        self.__age = age
        self.__ville = instance_ville
    
    def ajouterPopulation(self):
        # if Ville.get_nom(Ville) == self.__ville:
        #     Ville.ajouter_habitant(Ville)
        self.__ville.ajouter_habitant()

if __name__ == "__main__":
    # Création des objets Ville
    paris = Ville("Paris", 1000000)
    marseille = Ville("Marseille", 861635)

    # Affichage du nombre d'habitants initial pour chaque ville
    print(f"Nombre d'habitants à Paris: {paris.get_habitants()}\n"
        f"Nombre d'habitants à Marseille: {marseille.get_habitants()}")

    # Création des objets Personne
    john = Personne("John", 45, paris)
    myrtille = Personne("Myrtille", 4, paris)
    chloe = Personne("Chloé", 18, marseille)

    # Chaque personne arrive dans sa ville, ce qui augmente la population
    john.ajouterPopulation()
    myrtille.ajouterPopulation()
    chloe.ajouterPopulation()

    # Affichage des nouvelles populations après les arrivées
    print(f"Nombre d'habitants à Paris après les arrivées: {paris.get_habitants()}\n"
        f"Nombre d'habitants à Marseille après l'arrivée de Chloé: {marseille.get_habitants()}")
