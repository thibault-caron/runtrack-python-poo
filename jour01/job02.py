class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

if __name__ == "__main__":
    operation1 = Operation(12, 3)
    print(f"le nombre1 est {operation1.nombre1}")
    print(f"le nombre2 est {operation1.nombre2}")