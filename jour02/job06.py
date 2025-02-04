class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__liste_plats = []  
        self.__statut = "en cours" 

    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            print(f"La commande {self.__numero_commande} a été annulée.")
        else:
            print(f"La commande {self.__numero_commande} ne peut pas être annulée (statut: {self.__statut}).")

    def ajouter_plat(self, nom_plat, prix, statut_plat="en cours"):
        if self.__statut != "annulée":
            self.__liste_plats.append({"nom": nom_plat, "prix": prix, "statut": statut_plat})
        else:
            print("La commande est annulée, impossible d'ajouter un plat.")

    def __calculer_total(self):
        total = 0
        for plat in self.__liste_plats:
            total += plat["prix"]
        return total

    def calculer_tva(self):
        total = self.__calculer_total()
        # tva = total * 0.2  #si TVA non incluse dans le prix des plats
        tva = total - total / 1.2  #si TVA incluse dans le prix des plats
        return tva

    def afficher_commande(self):
        if self.__statut != "annulée":
            total = self.__calculer_total()
            tva = self.calculer_tva()
            print(f"Commande n° {self.__numero_commande} - Statut: {self.__statut}")
            print("Plats commandés:")
            for plat in self.__liste_plats:
                print(f"{plat["nom"]} à {plat["prix"]} - {plat["statut"]}")
            print(f"Total: {total} €, dont tva: {tva}") #", dont tva: {tva}" à retirer si TVA non incluse dans le prix des plats
            # print(f"TVA (20%): {tva} €")  #si TVA non incluse dans le prix des plats
            # print(f"Total à payer: {total + tva} €")  #si TVA non incluse dans le prix des plats

        else:
            print(f"La commande {self.__numero_commande} a été annulée et ne peut pas être affichée.")

if __name__ == "__main__":
    commande = Commande(1234)
    commande.afficher_commande()

    # Ajouter des plats à la commande
    commande.ajouter_plat("Pizza Margherita", 12.5)
    commande.ajouter_plat("Pasta Carbonara", 15.0)

    print("\nAprès ajout d'un plat :")
    commande.afficher_commande()

    # Annulation de la commande
    commande.annuler_commande()
    commande.ajouter_plat("Soupe du jour", 5.0)
    commande.afficher_commande()