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
    def aller_en_cours(self):
        print("Je vais en cours")

    def afficher_age(self):
        print(f"J'ai {self.age} ans.")

# Classe Professeur
class Professeur:
    '''Classe Professeur'''
    def __init__(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee  # Attribut privé

    def enseigner(self):
        print("Le cours va commencer")

# Instanciation d'une classe Personne et d'une classe Eleve
personne = Personne()
eleve = Eleve()

# Affichage de l'âge par défaut de l'élève
eleve.afficher_age()
