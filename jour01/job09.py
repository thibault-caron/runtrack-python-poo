class Produit:
    def __init__(self, nom = "nom", prix_HT = 0.0, TVA = 0.2):
        self.nom = nom
        self.prix_HT = prix_HT
        self.TVA = TVA
    

    def __str__(self):
        return f"Produit: (nom: {self.nom}, Prix Hors Taxes: {self.prix_HT}, TVA: {self.TVA}, Prix TTC: {self.calculer_prix_ttc()})"


    def calculer_prix_ttc(self):
        prix_ttc = self.prix_HT * (1 + self.TVA)
        return prix_ttc
    

    def afficher(self):
        return f"Nom: {self.nom},\nPrix Hors Taxes: {self.prix_HT},\nTVA: {self.TVA},\nPrix TTC: {self.calculer_prix_ttc()}\n"
    

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom
        return self.nom
    

    def modifier_prix(self, nouveau_prix):
        self.prix_HT = nouveau_prix
        return self.prix_HT
    

    def renvoi_nom(self):
        return self.nom
    

    def renvoi_prix_HT(self):
        return self.prix_HT
    

    def renvoi_TVA(self):
        return self.TVA


if __name__ == "__main__":
    produit1 = Produit("banana", 1.2)
    produit2 = Produit("Jouet", 20)

    print(f"{produit1.afficher()}")
    print(f"{produit2.afficher()}")

    print(f"Nouvel objet {produit1.renvoi_nom()} (ancien prix: {produit1.renvoi_prix_HT()} HT, {produit1.calculer_prix_ttc()} TTC) --> {produit1.modifier_nom("Poire")} (Prix: {produit1.modifier_prix(2.3)} HT, {produit1.calculer_prix_ttc()} TTC)")

    print(f"Nouvel objet {produit2.renvoi_nom()} (ancien prix: {produit2.renvoi_prix_HT()} HT, {produit2.calculer_prix_ttc()} TTC) --> {produit2.modifier_nom("Outils")} (Prix: {produit2.modifier_prix(12.5)} HT, {produit2.calculer_prix_ttc()} TTC)")

    print(Produit())
    print(produit1)