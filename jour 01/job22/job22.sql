

# Récupération des informations de l'étudiant le plus jeune

SELECT * FROM etudiant WHERE age = (SELECT MIN(age) FROM etudiant);
