class Student:
    def __init__(self, last_name, first_name, student_number):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__student_number = student_number
        self.__credits = 0
        self.__level = self.__student_eval()
    
    def get_credits(self):
        return self.__credits

    def get_last_name(self):
        return self.__last_name
    
    def get_first_name(self):
        return self.__first_name

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
    
    def add_credits(self, added_credits):
        if type(added_credits) is int and added_credits > 0:
            self.__credits += added_credits
            self.__level = self.__student_eval()
        else:
            print("Le namebre de crédits à ajouter doit être un nombre supérieur à zéro.")

    def student_info(self):
        print(f"\nNom: {self.__last_name},\nPrénom: {self.__first_name},\nNuméro étudiant: {self.__student_number},\nNiveau: {self.__level}\n")

    def __str__(self):
        return f"Nom: {self.__last_name}, Prénom: {self.__first_name}, Numéro étudiant: {self.__student_number}, Crédits: {self.__credits}, Niveau: {self.__level}"


if __name__ == "__main__":
    student = Student("Doe", "John", 145)

    student.add_credits("test")
    student.add_credits(-5)
    student.add_credits(-10)

    print(f"Le nombre de crédits de {student.get_first_name()} {student.get_last_name()} est de {student.get_credits()} points")

    student.student_info()