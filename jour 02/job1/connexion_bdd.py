import mysql.connector

# Informations de connexion à la base de don
host = "localhost"
user = "root"
password = "1020"
database = "LaPlateforme"

# Connexion à la base de données
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connexion à la base de données réussie.")

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = connection.cursor()

    # Exécution de la requête SQL pour récupérer tous les étudiants
    cursor.execute("SELECT * FROM etudiant")

    # Récupération des résultats de la requête
    result = cursor.fetchall()

    # Affichage des résultats dans la console
    print("\nListe des étudiant :")
    for row in result:
        print(row)

except mysql.connector.Error as error:
    print("Erreur lors de la connexion à la base de données :", error)

finally:
    # Fermeture de la connexion à la base de données
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée.")