# Classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informations_vehicule(self):
        print(f"Marque : {self.marque}\n"
            f"Modèle : {self.modele}\n"
            f"Année : {self.annee}\n"
            f"Prix : {self.prix}€")
        
    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    '''Classe Voiture qui hérite de Vehicule'''
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informations_vehicule(self):
        super().informations_vehicule()
        print(f"Nombre de portes : {self.portes}")

    def demarrer(self):
        '''Surcharge de la méthode demarrer pour la classe Voiture'''
        print(f"{self.marque} {self.modele} : C'est parti, je roule en voiture !")


class Moto(Vehicule):
    '''Classe Moto qui hérite de Vehicule'''
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informations_vehicule(self):
        super().informations_vehicule()
        print(f"Nombre de roues : {self.roue}")

    def demarrer(self):
        '''Surcharge de la méthode demarrer pour la classe Moto'''
        print(f"{self.marque} {self.modele} : Vroom vroom, je roule en moto !")

if __name__ == "__main__":
    # Instanciation de la classe Voiture
    voiture = Voiture("Toyota", "Corolla", 2020, 20000)
    voiture.informations_vehicule()

    # Instanciation de la classe Moto
    moto = Moto("Yamaha", "MT-07", 2022, 8000)
    moto.informations_vehicule()

    voiture.demarrer()
    moto.demarrer()
