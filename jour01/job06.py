class Animal:
    def __init__(self, age = 0.0, prenom = None):
        self.age = age
        self.prenom = prenom

    def viellir(self):
        self.age += 1
        print(f"Nouvel age de l'animal: {self.age} ans")
        return self.age
    
    def nommer(self):
        self.prenom = input("nouveau nom: ")
        print(f"l'animal se nomme {self.prenom}")
        return self.prenom

if __name__ == "__main__":
    animal1 = Animal()
    print(f"age de l'animal: {animal1.age}")
    animal1.viellir()
    animal1.nommer()