class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est : {resultat}")


# Instanciation de la classe Operation avec des valeurs spécifiques
operation_instance = Operation(12, 3)

# Appel de la méthode addition pour effectuer l'addition et afficher le résultat en console
operation_instance.addition()
