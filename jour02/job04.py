class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()
    
    
    def get_credits(self):
        return self.__credits
    

    def get_nom(self):
        return self.__nom
    
    
    def get_prenom(self):
        return self.__prenom
    

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Le nombre de crédits à ajouter doit être un nombre supérieur à zéro.")


    def student_info(self):
        print(f"\nNom: {self.__nom},\nPrénom: {self.__prenom},\nNuméro étudiant: {self.__numero_etudiant},\nNiveau: {self.__level}\n")
    

    def __str__(self):
        return f"Nom: {self.__nom}, Prénom: {self.__prenom}, Numéro étudiant: {self.__numero_etudiant}, Crédits: {self.__credits}, Niveau: {self.__level}"


if __name__ == "__main__":
    student = Student("Doe", "John", 145)

    student.add_credits(3)
    student.add_credits(5)
    student.add_credits(10)

    print(f"Le nombre de crédits de {student.get_prenom()} {student.get_nom()} est de {student.get_credits()} points")

    student.student_info()