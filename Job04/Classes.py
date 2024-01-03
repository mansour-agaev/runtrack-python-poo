class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"


# Instanciation de plusieurs personnes avec des valeurs de construction
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

# Appel de la méthode SePresenter pour chaque personne afin de vérifier le bon fonctionnement
resultat1 = personne1.SePresenter()
resultat2 = personne2.SePresenter()

# Affichage du résultat
print(resultat1)
print(resultat2)
