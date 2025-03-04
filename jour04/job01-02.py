class Personne:
    '''Classe Personne'''
    def __init__(self, age=14):
        self.age = age 

    def afficher_age(self):
        print(f"La personne a {self.age} ans.")

    def bonjour(self):
        print("Hello")

    def modifier_age(self, age):
        self.age = age


class Eleve(Personne):
    '''Classe Eleve qui hérite de Personne'''
    def __init__(self, age):
        super().__init__(age)

    def aller_en_cours(self):
        print("Je vais en cours")

    def afficher_age(self):
        print(f"J'ai {self.age} ans.")


class Professeur(Personne):
    '''Classe Professeur'''
    def __init__(self, age, matiere_enseignee="Mathématiques"):
        super().__init__(age)
        self.__matiere_enseignee = matiere_enseignee  # Attribut privé

    def enseigner(self):
        print("Le cours va commencer")

if __name__ == "__main__":
    # Instanciation d'une classe Personne et d'une classe Eleve
    personne = Personne()
    eleve = Eleve()

    # Affichage de l'âge par défaut de l'élève
    eleve.afficher_age()

    eleve.bonjour()  # L'élève dit bonjour
    eleve.aller_en_cours()  # L'élève va en cours
    eleve.modifier_age(15)  # L'âge de l'élève est redéfini à 15 ans
    eleve.afficher_age()  # Affiche l'âge de l'élève (15 ans)

    # Instanciation du professeur
    professeur = Professeur(age=40) 
    professeur.bonjour()  # Le professeur dit bonjour
    professeur.afficher_age()
    professeur.enseigner()  # Le professeur commence le cours