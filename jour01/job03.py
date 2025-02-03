class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(nombre1, nombre2):
        result = nombre1 + nombre2
        print(f"{nombre1} + {nombre2} = {result}")

if __name__ == "__main__":

    Operation.addition(12, 3)