class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom


# Instanciation de l'objet Animal
mon_animal = Animal()

# Affichage de l'âge initial de l'animal
print(f"L'age de l'animal {mon_animal.age} ans")

# Faire vieillir l'animal et afficher son âge après cela
mon_animal.vieillir()
print(f"L'age de l'animal {mon_animal.age} ans")

# Nommer l'animal et afficher son nom
mon_animal.nommer("Luna")
print(f"L'animal se nomme {mon_animal.prenom}")
