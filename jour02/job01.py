class Rectangle:
    def __init__(self, longueur = 0.0, largeur = 0.0):
        self.__longueur__ = longueur
        self.__largeur__ = largeur


    def get_longueur(self):
        return self.__longueur__
    
    def set_longueur(self, nouv_longueur):
        self.__longueur__ = nouv_longueur


    def get_largeur(self):
        return self.__largeur__
    
    def set_largeur(self, nouv_largeur):
        self.__largeur__ = nouv_largeur

    
if __name__ == "__main__":
    rectangle1 = Rectangle(10, 5)

    rectangle1.set_longueur(12)
    rectangle1.set_largeur(8)

    print(f"nouvelle longueur: {rectangle1.get_longueur()}, nouvelle largeur: {rectangle1.get_largeur()}")