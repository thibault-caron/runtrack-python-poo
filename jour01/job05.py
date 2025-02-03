class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_les_points(x, y):
        print(f"Coordonnée de x: {x}\nCoordonnée de y: {y}")

    def afficher_x(x):
        print(f"Coordonnée de x: {x}")

    def afficher_y(y):
        print(f"Coordonnée de y: {y}")

    def changer_x(x):
        try:
            x = int(input(f"New y: "))
        except TypeError:
            print("TypeError: doit être un nombre entier")

    def changer_y(y):
        try:
            y = int(input(f"New y: "))
        except TypeError:
            print("TypeError: doit être un nombre entier")


if __name__ == "__main__":

    Point.afficher_les_points(0, 1)
    Point.changer_y(20)