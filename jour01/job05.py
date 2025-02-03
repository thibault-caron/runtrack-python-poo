class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def afficher_les_points(self):
        print(f"Coordonnée de x: {self.x}\nCoordonnée de y: {self.y}")

    def afficher_x(self):
        print(f"Coordonnée de x: {self.x}")

    def afficher_y(self):
        print(f"Coordonnée de y: {self.y}")

    def changer_x(self):
        try:
            self.x = int(input(f"Nouveau x: "))
        except TypeError:
            print("TypeError: doit être un nombre entier")
        print(f"la nouvelle ordonnée du point x est {self.x}")

    def changer_y(self):
        try:
            self.y = int(input(f"Nouveau y: "))
        except TypeError:
            print("TypeError: doit être un nombre entier")
        print(f"la nouvelle ordonnée du point y est {self.y}")


if __name__ == "__main__":
    Point().afficher_les_points()
    Point().afficher_x()
    Point().afficher_y()
    Point().changer_x()
    Point().changer_y()