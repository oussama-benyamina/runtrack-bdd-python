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

    # Exécution de la requête SQL pour récupérer les noms et capacités de la table "salle"
    query = "SELECT nom, capacite FROM salle"
    cursor.execute(query)

    # Récupération des résultats
    result = cursor.fetchall()

    # Affichage des résultats
    print("Résultat :")
    for row in result:
        print(row)

except mysql.connector.Error as error:
    print("Erreur lors de la connexion à la base de données:", error)

finally:
    # Fermeture du curseur et de la connexion à la base de données
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée.")
