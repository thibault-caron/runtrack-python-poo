import math

class Cercle:
    def __init__(self, rayon = 0.0):
        self.rayon = rayon

    def changer_rayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
        return self.rayon
    
    def afficher_infos(self):
        print(f"\nRayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon


if __name__ == "__main__":
    cercle1 = Cercle(4)
    cercle1.afficher_infos()

    cercle2 = Cercle(7)
    cercle2.afficher_infos()