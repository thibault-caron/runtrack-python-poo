class Personne:

    def __init__(self, prenom = "Thibault", nom = "Caron"):
        self.prenom = prenom
        self.nom = nom

    def se_presenter(presente):
        print(f"Bonjour, je suis {presente.prenom} {presente.nom}")

if __name__ == "__main__":
    p1 = Personne().se_presenter()
    p2 = Personne("John", "Doe").se_presenter()
    p3 = Personne("Jean", "Dupond").se_presenter()