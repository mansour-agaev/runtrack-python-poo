class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2


# Instanciation de la classe Operation
operation_instance = Operation(12, 3)

# Impression de l'objet en console
print(f"Le nombre1 est {operation_instance.nombre1}")
print(f"Le nombre2 est {operation_instance.nombre2}")
