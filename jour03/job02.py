class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        """Affiche les détails du compte"""
        print(f"Compte n°: {self.__numero_compte}\n"
            f"Titulaire: {self.__prenom} {self.__nom}\n"
            f"Solde: {self.__solde} EUR\n"
            f"Droit au découvert: {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        """Affiche le solde du compte"""
        print(f"Le solde de votre compte est: {self.__solde} EUR")
    
    def versement(self, montant):
        """Ajoute le montant au solde du compte"""
        if montant > 0:
            self.__solde += montant
            print(f"{montant} EUR ont été ajoutés à votre compte.")
        else:
            print("Le montant du versement doit être positif.")
    
    def retrait(self, montant):
        """Effectue un retrait du compte, avec vérification du solde"""
        if montant <= 0:
            print("Le montant du retrait doit être positif.")
        elif self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur : Solde insuffisant et aucun découvert autorisé.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant} EUR effectué.")
            self.afficherSolde()

    def agios(self):
        """Applique des agios si le solde est négatif"""
        if self.__solde < 0:
            agios = abs(self.__solde) * 0.05  # Exemple d'agios de 5%
            self.__solde -= agios
            print(f"Agios appliqués : {agios:.2f} EUR")
            self.afficherSolde()
        else:
            print(f"Les Agios ne sont pas appliqués sur des solde positifs.\n"
                  "Solde du compte: {self.__solde:.2f} EUR")
    
    def virement(self, compte_dest, montant):
        """Effectue un virement vers un autre compte"""
        if montant <= 0:
            print("Le montant du virement doit être positif.")
        elif self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur : Solde insuffisant pour effectuer le virement.")
        else:
            self.__solde -= montant
            compte_dest.versement(montant)
            print(f"Virement de {montant} EUR effectué vers le compte {compte_dest.__numero_compte}.")
            self.afficherSolde()


if __name__ == "__main__":
    # Création de deux comptes bancaires
    compte1 = CompteBancaire("12345", "Dupont", "Jean", 1000, decouvert=True)
    compte2 = CompteBancaire("67890", "Martin", "Sophie", -150, decouvert=True)

    # Affichage des détails des comptes
    compte1.afficher()
    compte2.afficher()

    # Effectuer des versements et retraits
    compte1.versement(500)    # Versement de 500 EUR sur le compte1
    compte1.retrait(200)      # Retrait de 200 EUR du compte1
    compte2.retrait(100)      # Retrait de 100 EUR du compte2 (ce compte est à découvert)

    # Appliquer des agios sur le compte à découvert
    compte2.agios()

    # Faire un virement du compte1 vers le compte2 pour remettre celui-ci à zéro
    compte1.virement(compte2, 350)  # Virement de 350 EUR du compte1 vers le compte2

    # Afficher les comptes après le virement
    compte1.afficher()
    compte2.afficher()
