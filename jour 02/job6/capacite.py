import mysql.connector

try:
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1020",
        database="LaPlateforme"
    )
    print("Connexion à la base de données réussie.")

    # Création d'un curseur
    cursor = connection.cursor()

    # Exécution de la requête SQL pour calculer la capacité totale des salles
    query = "SELECT SUM(capacite) AS capacite_totale FROM salle"
    cursor.execute(query)

    # Récupération du résultat
    result = cursor.fetchone()

    # Affichage du résultat
    capacite_totale = result[0]
    print("La capacité de toutes les salles est de :", capacite_totale)

except mysql.connector.Error as error:
    print("Erreur lors de la connexion à la base de données:", error)

finally:
    # Fermeture du curseur et de la connexion à la base de données
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée.")
