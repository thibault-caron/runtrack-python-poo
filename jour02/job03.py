class Livre:
    def __init__(self, titre = "titre", auteur = "auteur", nombre_pages = 0, disponible = True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = disponible


    def get_titre(self):
        return self.__titre
    
    def set_titre(self, nouv_titre):
        self.__titre = nouv_titre


    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, nouv_auteur):
        self.__auteur = nouv_auteur


    def get_nombre_pages(self):
        return self.__nombre_pages
    
    def set_nombre_pages(self, nouv_nombre_pages):
        if int(nouv_nombre_pages) == True and nouv_nombre_pages > 0:
            self.__nombre_pages = nouv_nombre_pages
        else:
            print("le nombre de page doit être un entier supperieur à 0")  

    
    def verification(self):
        if self.__disponible == True or self.__disponible == False:
            return self.__disponible
        else:
            print("Mauvaise valeur pour 'disponible'")
            return False
        
    def set_disponible(self, nouv_disponible):
        self.__disponible = nouv_disponible
        

    def emprunter(self):
        if self.verification() == True:
            self.set_disponible(False)
            print("Livre emprunté!")
        else:
            print(f"Erreur: disponibilité = {self.verification()}")

    
    def rendre(self):
        if self.verification() == False:
            self.set_disponible(True)
            print("Livre rendu!")
        else:
            print(f"Erreur: disponible = {self.verification()}")

    
if __name__ == "__main__":
    livre1 = Livre("test", "thibault", 10)

print("test rendre():")
livre1.rendre()
print(f"disponible: {livre1.verification()}")
print("test emprunter():")
livre1.emprunter()
print(f"disponible: {livre1.verification()}")
print("test emprunter():")
livre1.emprunter()
print(f"disponible: {livre1.verification()}")
print("test rendre():")
livre1.rendre()
print(f"disponible: {livre1.verification()}")