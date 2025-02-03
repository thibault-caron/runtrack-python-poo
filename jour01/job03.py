class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        result = self.nombre1 + self.nombre2
        print(f"{self.nombre1} + {self.nombre2} = {result}")

if __name__ == "__main__":

    Operation(12, 3).addition()