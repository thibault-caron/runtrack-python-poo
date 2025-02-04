class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False 
        self.__reservoir = 50  

    # Mutateurs (setters)
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    # Accesseurs (getters)
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    # Autres méthodes
    def demarrer(self):
        if self.__verifier_plein() > 5:  # Vérifie si le réservoir a plus de 5 unités de carburant
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer, réservoir presque vide.")

    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")
  
    def __verifier_plein(self):
        return self.__reservoir

    def afficher_info(self):
        print(f"\nMarque: {self.__marque}")
        print(f"Modèle: {self.__modele}")
        print(f"Année: {self.__annee}")
        print(f"Kilométrage: {self.__kilometrage} km")
        print(f"En marche: {'Oui' if self.__en_marche else 'Non'}")
        print(f"Réservoir: {self.__reservoir} litres")


if __name__ == "__main__":
   
    ma_voiture = Voiture("Toyota", "Corolla", 2020, 15000)

    ma_voiture.afficher_info()
    ma_voiture.demarrer()

    print(f"réduction carburant: {ma_voiture.get_reservoir()}L")
    ma_voiture.set_reservoir(3)
    ma_voiture.demarrer()
    ma_voiture.arreter()

    print("\nAprès modifications :")
    ma_voiture.afficher_info()
