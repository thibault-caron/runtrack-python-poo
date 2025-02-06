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

if __name__ == "__main__":
    # Instanciation de la classe Rectangle
    rectangle = Rectangle(10, 5)

    # Affichage du résultat de la méthode aire de la classe Rectangle
    print(f"L'aire du rectangle est : {rectangle.aire()}")
