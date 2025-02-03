class Personne:

    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def se_presenter(prenom = "Thibault", nom = "Caron",):
        print(f"Bonjour, je suis {prenom} {nom}")

if __name__ == "__main__":

    Personne.se_presenter("John", "Doe")
    Personne.se_presenter("Jean", "Dupond")
    Personne.se_presenter()