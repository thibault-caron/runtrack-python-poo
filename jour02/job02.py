class Livre:
    def __init__(self, titre = "titre", auteur = "auteur", nombre_pages = 0):
        self.__titre__ = titre
        self.__auteur__ = auteur

        if int(nombre_pages) == True and nombre_pages > 0:
            self.__nombre_pages__ = nombre_pages
        else:
            print("le nombre de page doit être un entier supperieur à 0 dans son instanciation")   
        

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

    
if __name__ == "__main__":
    livre1 = Livre("test", "thibault", 10)

    livre1.set_titre("nouveau test")
    livre1.set_nombre_pages(10.2)

    print(f"nouveau titre: {livre1.get_titre()}, nouveau nombre de pages: {livre1.get_nombre_pages()}")