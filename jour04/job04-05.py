import math

class Forme:
    def aire(self):
        return 0  

class Rectangle(Forme):
    '''Classe Rectangle qui hérite de la classe Forme'''
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        '''Méthode qui renvoie l'aire du rectangle'''
        return self.__largeur * self.__hauteur
    

class Cercle(Forme):
    '''Classe Cercle qui hérite de la classe Forme'''
    def __init__(self, radius):
        self.radius = radius  # Attribut radius

    # Surcharge de la méthode aire pour calculer l'aire du cercle
    def aire(self):
        return math.pi * (self.radius ** 2)  # L'aire du cercle (π * r²)

if __name__ == "__main__":
    # Instanciation de la classe Rectangle et Cercle
    rectangle = Rectangle(10, 5)
    cercle = Cercle(7)

    # Affichage du résultat de la méthode aire de la classe Rectangle et Cercle
    print(f"L'aire du rectangle est : {rectangle.aire()}")
    print(f"L'aire du cercle est : {cercle.aire()}")
