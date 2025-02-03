class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(nom, prenom):
        print(f"Bonjour, je suis {nom} {prenom}")

if __name__ == "__main__":

    Personne.se_presenter("Thibault", "Caron")
    Personne.se_presenter("John", "Doe")
    Personne.se_presenter("Jean", "Dupond")