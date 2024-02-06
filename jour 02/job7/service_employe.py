from typing import Self
import mysql.connector

class EmployeManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create(self, nom, prenom, salaire, id_service):
        try:
            query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
            values = (nom, prenom, salaire, id_service)
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Erreur lors de la création de l'employé:", err)

    def read(self):
        try:
            query = "SELECT * FROM employe"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print("Erreur lors de la lecture des employés:", err)

    def update(self, employe_id, salaire):
        try:
            query = "UPDATE employe SET salaire = %s WHERE id = %s"
            values = (salaire, employe_id)
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Erreur lors de la mise à jour de l'employé:", err)

    def delete(self, employe_id):
        try:
            query = "DELETE FROM employe WHERE id = %s"
            values = (employe_id,)
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Erreur lors de la suppression de l'employé:", err)

def __del__(self):
    if hasattr(self, 'connection'):
        if self.connection.is_connected():
            try:
                self.connection.close()
            except AttributeError:
                pass


# Exemple d'utilisation de la classe EmployeManager
if __name__ == "__main__":
    manager = EmployeManager(host="localhost", user="root", password="1020", database="entreprise")
    
    # Création d'un nouvel employé
    manager.create("Durand", "Marie", 3200, 1)

    # Lecture de tous les employés
    employes = manager.read()
    for employe in employes:
        print(employe)

    # Mise à jour du salaire d'un employé
    manager.update(2, 3000)

    # Suppression d'un employé
    manager.delete(3)
