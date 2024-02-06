
# Modification de l'âge de Betty de 23 ans à 20 ans

UPDATE etudiant SET age = 20 WHERE nom = 'Spaghetti' AND prenom = 'Betty';


# Affichage des informations de Betty pour vérification

SELECT * FROM etudiant WHERE nom = 'Spaghetti' AND prenom = 'Betty';
