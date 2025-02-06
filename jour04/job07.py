class Personnage:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
        print(f"deplacement à gauche, x: {self.x}")
        return self.x
    
    def droite(self):
        self.x += 1
        print(f"deplacement à droite, x: {self.x}")
        return self.x
    
    def bas(self):
        self.y -= 1
        print(f"deplacement en bas, y: {self.y}")
        return self.y
    
    def haut(self):
        self.y += 1
        print(f"deplacement en haut, y: {self.y}")
        return self.y
    
    def position(self):
        print(f"Ma position (x, y): {self.x, self.y}")
        return self.x, self.y

if __name__ == "__main__":
    personnage1 = Personnage(4, 8)
    personnage1.droite()
    personnage1.bas()
    print(personnage1.position())