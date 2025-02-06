class Rectangle:
    '''
    Classe Rectangle
    '''
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # 
    def perimetre(self):
        ''' Méthode pour calculer le périmètre '''
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        '''Méthode pour calculer la surface'''
        return self.__longueur * self.__largeur

    # Assesseurs (getters) pour longueur et largeur
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters) pour longueur et largeur
    def set_longueur(self, nouv_longueur):
        self.__longueur = nouv_longueur

    def set_largeur(self, nouv_largeur):
        self.__largeur = nouv_largeur


class Parallelepipede(Rectangle):
    '''Classe Parallelepipede qui hérite de Rectangle'''
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur  

    def volume(self):
        '''Méthode pour calculer le volume'''
        return self.get_longueur() * self.get_largeur() * self.__hauteur

    # Assesseur pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur pour la hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

if __name__ == "__main__":
    # Instanciation de la classe Rectangle
    rectangle = Rectangle(10, 5)

    # Vérification des méthodes de la classe Rectangle
    print(f"Périmètre du rectangle : {rectangle.perimetre()}")
    print(f"Surface du rectangle : {rectangle.surface()}")

    # Modification de la longueur et de la largeur
    rectangle.set_longueur(12)
    rectangle.set_largeur(6)

    # Vérification des nouvelles valeurs
    print(f"Nouveau périmètre du rectangle : {rectangle.perimetre()}")
    print(f"Nouvelle surface du rectangle : {rectangle.surface()}")

    # Instanciation de la classe Parallelepipede
    parallelepipede = Parallelepipede(10, 5, 8)

    # Vérification des méthodes de la classe Parallelepipede
    print(f"Volume du parallélépipède : {parallelepipede.volume()}") 
