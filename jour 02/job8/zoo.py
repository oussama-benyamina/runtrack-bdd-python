import mysql.connector

class Zoo:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1020",
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_animal(self, id_animal):
        query = "DELETE FROM animal WHERE id = %s"
        values = (id_animal,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def modifier_animal(self, id_animal, nom, race, id_cage, date_naissance, pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, id_animal)
        self.cursor.execute(query, values)
        self.conn.commit()

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        animaux = self.cursor.fetchall()
        for animal in animaux:
            print(animal)

    def afficher_animaux_cages(self):
        query = "SELECT c.id AS id_cage, a.* FROM cage c LEFT JOIN animal a ON c.id = a.id_cage"
        self.cursor.execute(query)
        animaux_cages = self.cursor.fetchall()
        for row in animaux_cages:
            print(row)

    def calculer_superficie_totale_cages(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        superficie_totale = self.cursor.fetchone()[0]
        print("Superficie totale des cages :", superficie_totale)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation de la classe Zoo
if __name__ == "__main__":
    zoo = Zoo()
    while True:
        print("1. Ajouter un animal")
        print("2. Supprimer un animal")
        print("3. Modifier un animal")
        print("4. Afficher tous les animaux")
        print("5. Afficher les animaux dans les cages")
        print("6. Calculer la superficie totale des cages")
        print("7. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            nom = input("Nom de l'animal : ")
            race = input("Race de l'animal : ")
            id_cage = input("ID de la cage : ")
            date_naissance = input("Date de naissance de l'animal : ")
            pays_origine = input("Pays d'origine de l'animal : ")
            zoo.ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)
        elif choix == "2":
            id_animal = input("ID de l'animal à supprimer : ")
            zoo.supprimer_animal(id_animal)
        elif choix == "3":
            id_animal = input("ID de l'animal à modifier : ")
            nom = input("Nouveau nom de l'animal : ")
            race = input("Nouvelle race de l'animal : ")
            id_cage = input("Nouvel ID de la cage : ")
            date_naissance = input("Nouvelle date de naissance de l'animal : ")
            pays_origine = input("Nouveau pays d'origine de l'animal : ")
            zoo.modifier_animal(id_animal, nom, race, id_cage, date_naissance, pays_origine)
        elif choix == "4":
            zoo.afficher_animaux()
        elif choix == "5":
            zoo.afficher_animaux_cages()
        elif choix == "6":
            zoo.calculer_superficie_totale_cages()
        elif choix == "7":
            break
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 7.")
