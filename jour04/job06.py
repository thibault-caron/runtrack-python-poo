class Animal:
    def __init__(self, age = 0.0, prenom = None):
        self.age = age
        self.prenom = prenom

    def viellir(self):
        self.age += 1
        print(f"Nouvel age de l'animal: {self.age} ans")
        return self.age
    
    def nommer0(self):
        self.prenom = input("nouveau nom: ")
        print(f"l'animal se nomme {self.prenom}")
        return self.prenom
    
    def nommer(self, nommer_prenom):
        self.prenom = nommer_prenom
        print(f"l'animal se nomme {self.prenom}")
        return self.prenom

if __name__ == "__main__":
    animal1 = Animal()
    print(f"age de l'animal: {animal1.age}")
    animal1.viellir()
    animal1.nommer0()
    animal1.nommer("Luna")
    print(f"animal1 prenom: {animal1.prenom}")