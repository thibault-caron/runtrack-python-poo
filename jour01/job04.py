class Peronne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(nom, prenom):
        print(f"Bonjour, je suis {nom} {prenom}")

if __name__ == "__main__":

    Peronne.se_presenter("Thibault", "Caron")
    Peronne.se_presenter("John", "Doe")
    Peronne.se_presenter("Jean", "Dupond")