class Produit:
    def __init__(self, nom = "nom", prix_HT = 0.0, TVA = 0.2):
        self.nom = nom
        self.prix_HT = prix_HT
        self.TVA = TVA
    

    def __str__(self):
        return f"Produit({self.nom}, Hors Taxes: {self.prix_HT}, TVA: {self.TVA}, TTC: {self.calculer_prix_ttc()})"


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
    banana = Produit("banana", 1.2)
    jouet = Produit("Jouet", 20)

    print(f"{banana.afficher()}")
    print(f"{jouet.afficher()}")

    print(f"Nouvel objet {banana.renvoi_nom()} (ancien prix: {banana.renvoi_prix_HT()} HT, {banana.calculer_prix_ttc()} TTC) --> {banana.modifier_nom("Poire")} (Prix: {banana.modifier_prix(2.3)} HT, {banana.calculer_prix_ttc()} TTC)")

    print(f"Nouvel objet {jouet.renvoi_nom()} (ancien prix: {jouet.renvoi_prix_HT()} HT, {jouet.calculer_prix_ttc()} TTC) --> {jouet.modifier_nom("Outils")} (Prix: {jouet.modifier_prix(12.5)} HT, {jouet.calculer_prix_ttc()} TTC)")