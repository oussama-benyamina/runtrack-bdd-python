#Pour ajouter un élève nommé Martin Dupuis à votre table "etudiant", vous pouvez utiliser la commande suivante :

INSERT INTO etudiant (nom, prenom, age, email) VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

#Pour récupérer les membres d'une même famille,

SELECT * FROM etudiant WHERE nom = 'Dupuis';
