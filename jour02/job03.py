class Livre:
    def __init__(self, titre = "titre", auteur = "auteur", nombre_pages = 0, disponible = True):
        self.__titre__ = titre
        self.__auteur__ = auteur
        self.__nombre_pages__ = nombre_pages
        self.__disponible__ = disponible


    def get_titre(self):
        return self.__titre__
    
    def set_titre(self, nouv_titre):
        self.__titre__ = nouv_titre


    def get_auteur(self):
        return self.__auteur__
    
    def set_auteur(self, nouv_auteur):
        self.__auteur__ = nouv_auteur


    def get_nombre_pages(self):
        return self.__nombre_pages__
    

    def set_nombre_pages(self, nouv_nombre_pages):
        if int(nouv_nombre_pages) == True and nouv_nombre_pages > 0:
            self.__nombre_pages__ = nouv_nombre_pages
        else:
            print("le nombre de page doit être un entier supperieur à 0")  


    def get_disponible(self):
        return self.__disponible__
    
    def set_disponible(self, nouv_disponible):
        self.__disponible__ = nouv_disponible


    def emprunter(self):
        if self.get_disponible() == True:
            self.set_disponible(False)
            print("Livre emprunté!")
        else:
            print(f"Erreur: disponibilité = {self.get_disponible()}")

    
    def rendre(self):
        if self.get_disponible() == False:
            self.set_disponible(True)
            print("Livre rendu!")
        else:
            print(f"Erreur: disponible = {self.get_disponible()}")

    
if __name__ == "__main__":
    livre1 = Livre("test", "thibault", 10)

print("test rendre():")
livre1.rendre()
print(f"disponible: {livre1.get_disponible()}")
print("test emprunter():")
livre1.emprunter()
print(f"disponible: {livre1.get_disponible()}")
print("test emprunter():")
livre1.emprunter()
print(f"disponible: {livre1.get_disponible()}")
print("test rendre():")
livre1.rendre()
print(f"disponible: {livre1.get_disponible()}")