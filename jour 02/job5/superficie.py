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

    # Exécution de la requête SQL pour calculer la superficie totale des étages
    query = "SELECT SUM(superficie) AS superficie_totale FROM etage"
    cursor.execute(query)

    # Récupération du résultat
    result = cursor.fetchone()

    # Affichage du résultat
    superficie_totale = result[0]
    print("La superficie de La Plateforme est de", superficie_totale, "m2.")

except mysql.connector.Error as error:
    print("Erreur lors de la connexion à la base de données:", error)

finally:
    # Fermeture du curseur et de la connexion à la base de données
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée.")
